from flask import Blueprint
# 创建一个名为 authrouter 的蓝图
authrouter_app = Blueprint('Authrouter', __name__)
from . import authrouter# 导入authrouter模块中的视图函数


from .customers import personal_query_app
from .windows import window_app