import random
import re
from datetime import datetime

from flask import render_template, request, abort, current_app, make_response, json, jsonify, session

from info import redis_store, constants, db
from info.libs.yuntongxun.sms import CCP
from info.models import User
from info.modules.passport import passport_blue
from info.utils.captcha.captcha import captcha
from info.utils.response_code import RET


@passport_blue.route('/register', methods=['POST'])
def register():
    params_dict = json.loads(request.data)
    mobile = params_dict.get('mobile')
    smscode = params_dict.get('sms_code')
    password = params_dict.get('password')

    # 验证参数
    if not all([mobile, smscode, password]):
        return jsonify(error=RET.PARAMERR, errmsg='参数有误')

    # 验证手机号是否正确
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(error=RET.PARAMERR, errmsg='手机号码格式不正确')

    # 从redis出取出验证码
    try:
        real_sms_code = redis_store.get('SMS_' + mobile)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg='数据查询失败')

    # 表示验证码过期,一定要记住从redis取出后进行decode，否则怎么死的都不知道
    if not real_sms_code:
        return jsonify(error=RET.NODATA, errmsg='手机验证码错误或者已过期')
    else:
        real_sms_code = real_sms_code.decode()

    # 对比验证码
    if real_sms_code != smscode:
        return jsonify(error=RET.DATAERR, errmsg='验证码输入错误')

    # 进行用户注册
    user = User()
    user.mobile = mobile
    user.nick_name = mobile
    user.last_login = datetime.now()
    # TODO 对密码进行处理

    # 添加到数据库
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(error=RET.DBERR, errmsg='数据保存失败')

    # 往session中保存状态表示当前已登录
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name

    # 返回响应
    return jsonify(error=RET.OK, errmsg='注册成功')


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
        return jsonify(error=RET.PARAMERR, errmsg='参数有误')

    # 验证手机号是否正确
    if not re.match('1[35678]\\d{9}', mobile):
        return jsonify(error=RET.PARAMERR, errmsg='手机号码格式不正确')

    # 从redis出取出验证码
    try:
        real_image_code = redis_store.get('ImageCodeId_' + image_code_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(error=RET.DBERR, errmsg='数据查询失败')

    if not real_image_code:
        # 表示验证码过期
        return jsonify(error=RET.NODATA, errmsg='图片验证码已过期')
    else:
        # 如果能够取出来值进行解码，否则输出是b'XXXX'永远不会想等，删除redis中缓存的内容
        real_image_code = real_image_code.decode()

    # 对比验证码
    # print("real_image_code: %s, image_code: %s" % (real_image_code.upper(), image_code.upper()))
    if real_image_code.upper() != image_code.upper():
        return jsonify(error=RET.DATAERR, errmsg='验证码输入错误')

    # 验证码正确，发送短信验证码，随机生成6位数,06d表示不够6位前面补上0
    # sms_code_str = "%06d" % random.randint(0, 999999)
    sms_code_str = "888888"

    # 发送短信验证码,假设验证码发送成功，并且向redis存入一个验证码=888888
    # result = CCP().send_template_sms(mobile, [sms_code_str, constants.SMS_CODE_REDIS_EXPIRES / 5], '1')
    result = 0

    if result != 0:
        # 代表发送失败
        return jsonify(error=RET.THIRDERR, errmsg='短信发送失败')

    # 6. redis中保存短信验证码内容, 等待用户提交表单进行验证
    try:
        redis_store.set("SMS_" + mobile, sms_code_str, constants.SMS_CODE_REDIS_EXPIRES)
    except Exception as e:
        current_app.logger.error(e)
        # 保存短信验证码失败
        return jsonify(errno=RET.DBERR, errmsg="redis保存短信验证码失败")

    return jsonify(error=RET.OK, errmsg='发送成功')


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



