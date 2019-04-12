from flask import Blueprint

profile_blue = Blueprint('profile', __name__, url_prefix='/user')

from . import views