from flask import Blueprint
# 创建一个名为 authrouter 的蓝图
authrouter = Blueprint('authrouter', __name__)
from . import authrouter  # 导入authrouter模块中的视图函数