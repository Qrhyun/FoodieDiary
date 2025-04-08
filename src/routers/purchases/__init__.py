from flask import Blueprint
# 创建一个名为purchase的蓝图
purchase_app = Blueprint('purchase', __name__)

from . import Purchase  # 导入 purchases 模块中的视图函数