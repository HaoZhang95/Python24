from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField

app = Flask(__name__)
app.secret_key = 'Hao'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    return render_template('demo1.html')


@app.route('/demo2')
def demo2():
    return render_template('demo2.html')


@app.route('/demo3', methods=['POST', 'GET'])
def demo3():
    """不适用WTForms表单进行的传统验证方法"""

    # 判断是不是提POST交的页面还是GET进行的页面获取
    if request.method == "POST":
        # 取到表单中提交上来的三个参数
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        if not all([username, password, password2]):
            # 向前端界面弹出一条提示(闪现消息)
            # 因为flash要用到session,所以需要为app设置secret_key否则报不可靠链接错误
            flash("参数不足")
        elif password != password2:
            flash("两次密码不一致")
        else:
            # 假装做注册操作
            print(username, password, password2)
            return "success"

    return render_template('demo3.html')


# 自定义注册表单，集成自flaskform,其使用是以对象的形式，需要定义不同的对象属性
class RegisterForm(FlaskForm):
    username = StringField(label='用户名:', render_kw={'placeholder': '请输入用户名'})
    password = PasswordField(label='密码:')
    password2 = PasswordField(label='确认密码:')
    submit = SubmitField(label='提交')


@app.route('/demo4')
def demo4():

    # 把WTF对象实例化，传递到模板中进行调用渲染
    register_form = RegisterForm()
    return render_template('demo3.html', register_form=register_form)


if __name__ == '__main__':
    app.run()
