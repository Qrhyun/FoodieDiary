from flask import Blueprint

# 创建一个名为 personal_query 的蓝图
personal_query_app = Blueprint('personal_query', __name__)

from . import Personal_Queryrouter  # 导入 Personal_Queryrouter 模块中的视图函数