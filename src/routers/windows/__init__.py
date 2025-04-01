from flask import Blueprint
window_app= Blueprint('window_app', __name__)
from . import Windowrouter  # 导入 Windowrouter 模块中的视图函数