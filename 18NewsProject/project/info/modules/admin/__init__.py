from flask import Blueprint, session, redirect, request, url_for

admin_blue = Blueprint('admin', __name__, url_prefix='/admin')

from info.modules.admin import views


@admin_blue.before_request
def check_admin():
    """如果不是管理员。直接跳到首页"""

    is_admin = session.get('is_admin', False)

    if not is_admin and not request.url.endswith(url_for('admin.login')):
        return redirect('/')
