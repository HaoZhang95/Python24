from flask import render_template, redirect, g, request, jsonify

from info.modules.profile import profile_blue
from info.utils.common import user_login_data
from info.utils.response_code import RET


@profile_blue.route("/pic_info", methods=['GET', 'POST'])
@user_login_data
def pic_info():

    # get请求进行头像的获取
    if request.method == 'GET':
        return render_template('news/user_pic_info.html', data={"user_info": g.user.to_dict()})


@profile_blue.route("/base_info", methods=['GET', 'POST'])
@user_login_data
def base_info():
    """一个url根据不同的请求方法去执行不同的动作"""

    # get请求进行资料的获取
    if request.method == 'GET':
        return render_template('news/user_base_info.html', data={"user_info": g.user.to_dict()})

    # 获取参数
    nick_name = request.json.get("nick_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")

    # 验证参数
    if not all([nick_name, signature, gender]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if gender not in ('WOMAN', 'MAN'):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 模型的修改
    user = g.user
    user.nick_name = nick_name
    user.gender = gender
    user.signature = signature

    return jsonify(errno=RET.OK, errmsg="用户信息修改成功")


@profile_blue.route('/info')
@user_login_data
def user_info():

    user = g.user

    if not user:
        return redirect("/")

    data = {
        "user_info": user.to_dict(),
    }
    return render_template("news/user.html", data=data)
