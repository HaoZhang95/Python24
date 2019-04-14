import re
from datetime import datetime

from flask import request, abort, current_app, make_response, json, jsonify, session

from info import redis_store, constants, db
from info.models import User
from info.modules.passport import passport_blue
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET


@passport_blue.route('/logout', methods=['POST'])
def logout():
    # 推出登陆就是从redis中删除session
    session.pop('user_id', None)
    session.pop('mobile', None)
    session.pop('nick_name', None)
    # 不清除admin，会在管理员和普通用户切换过程中，能够以普通用户身份来登陆管理员
    session.pop('is_admin', None)
    return jsonify(errno=RET.OK, errmsg='退出成功')


@passport_blue.route('/login', methods=['POST'])
def login():
    # 获取参数
    params_dict = request.json
    mobile = params_dict.get('mobile')
    password = params_dict.get('password')

    # 校验参数
    if not all([mobile, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数有误')

    # 检验密码
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式不正确')

    # 查询当前的用户是否存在
    try:
        user = User.query.filter(User.mobile == mobile).first()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询失败')

    if not user:
        return jsonify(errno=RET.NODATA, errmsg='用户不存在')

    if not user.check_passowrd(password):
        return jsonify(errno=RET.DATAERR, errmsg='密码输入错误')

    # 保存用户登录状态到session
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name

    # 但是登陆的时候，最后一次的数据需要更新，并且写入到数据库才算数，去更新数据库中的最后一次登陆时间
    # 如果视图函数中对模型的属性进行修改的话，需要commit到数据库，为了方便，在SQLALchemy中的teardowb中进行统一设置
    user.last_login = datetime.now()
    # try:
    #     db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     current_app.logger.error(e)

    # 返回响应
    return jsonify(errno=RET.OK, errmsg='登陆成功')


@passport_blue.route('/register', methods=['POST'])
def register():
    params_dict = json.loads(request.data)
    mobile = params_dict.get('mobile')
    smscode = params_dict.get('sms_code')
    password = params_dict.get('password')

    # 验证参数
    if not all([mobile, smscode, password]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数有误')

    # 验证手机号是否正确
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式不正确')

    # 从redis出取出验证码
    try:
        real_sms_code = redis_store.get('SMS_' + mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询失败')

    # 表示验证码过期,一定要记住从redis取出后进行decode，否则怎么死的都不知道
    if not real_sms_code:
        return jsonify(errno=RET.NODATA, errmsg='手机验证码错误或者已过期')
    else:
        real_sms_code = real_sms_code.decode()

    # 对比验证码
    if real_sms_code != smscode:
        return jsonify(errno=RET.DATAERR, errmsg='验证码输入错误')

    # 进行用户注册
    user = User()
    user.mobile = mobile
    user.nick_name = mobile
    # 第一次注册的时候最后一次登录信息就直接伴随着模型的创建写入到了数据库
    user.last_login = datetime.now()
    # 对密码进行处理,在user的数据模型类中自动加密，将加密解锁设置到user.password_hash
    user.password = password

    # 添加到数据库
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg='数据保存失败')

    # 往session中保存状态表示当前已登录
    """
        这里的session是使用的是Config类中的存储在redis中的session，下面这几个变量值都是存在一个相同的session——id下面的
        并不是在redis分开存储了3个，而是在一个session_id下，值为一个字典，字典里面包含这3个变量
    """
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name

    # 返回响应
    return jsonify(errno=RET.OK, errmsg='注册成功')


@passport_blue.route('/sms_code', methods=['POST'])
def send_sms_code():
    # 获取参数
    # params_dict = json.loads(request.data)
    params_dict = request.json
    mobile = params_dict.get('mobile')
    image_code = params_dict.get('image_code')
    image_code_id = params_dict.get('image_code_id')

    # 验证参数
    if not all( [mobile, image_code, image_code_id] ):
        return jsonify(errno=RET.PARAMERR, errmsg='参数有误')

    # 验证手机号是否正确
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(errno=RET.PARAMERR, errmsg='手机号码格式不正确')

    # 从redis出取出验证码
    try:
        real_image_code = redis_store.get('ImageCodeId_' + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询失败')

    if not real_image_code:
        # 表示验证码过期
        return jsonify(errno=RET.NODATA, errmsg='图片验证码已过期')
    else:
        # 如果能够取出来值进行解码，否则输出是b'XXXX'永远不会想等，删除redis中缓存的内容
        real_image_code = real_image_code.decode()

    # 对比验证码
    # print("real_image_code: %s, image_code: %s" % (real_image_code.upper(), image_code.upper()))
    if real_image_code.upper() != image_code.upper():
        return jsonify(errno=RET.DATAERR, errmsg='验证码输入错误')

    # 验证码正确，发送短信验证码，随机生成6位数,06d表示不够6位前面补上0
    # sms_code_str = "%06d" % random.randint(0, 999999)
    sms_code_str = "888888"

    # 发送短信验证码,假设验证码发送成功，并且向redis存入一个验证码=888888
    # result = CCP().send_template_sms(mobile, [sms_code_str, constants.SMS_CODE_REDIS_EXPIRES / 5], '1')
    result = 0

    if result != 0:
        # 代表发送失败
        return jsonify(errno=RET.THIRDERR, errmsg='短信发送失败')

    # 6. redis中保存短信验证码内容, 等待用户提交表单进行验证
    try:
        redis_store.set("SMS_" + mobile, sms_code_str, constants.SMS_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        # 保存短信验证码失败
        return jsonify(errno=RET.DBERR, errmsg="redis保存短信验证码失败")

    return jsonify(errno=RET.OK, errmsg='发送成功')


@passport_blue.route('/image_code')
def get_image_code():
    """生成图片验证码"""

    # 1- 取到验证码中的uuid参数, url中问号后面的参数
    image_code_id = request.args.get('cur_id', None)

    # 2- 判断uuid是否合格
    if not image_code_id:
        return abort(403)

    # 3- 生成验证码
    name, text, image = captcha.generate_captcha()

    # 4- 保存K-V到redis
    try:
        redis_store.set('ImageCodeId_' + image_code_id, text, constants.IMAGE_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        abort(500)

    # 5- 返回验证码给客户端,设置数据返回的类型，以便浏览器更加智能的识别，否则默认就是text/html
    response = make_response(image)
    response.headers['Content-Type'] = 'image/jpg'
    return response



