from flask import Flask
from .extensions import db # 从 models 模块导入 db 对象
from .models import authmodel
from config import Config
def init_app(app):
    # 初始化应用程序，绑定数据库
    db.init_app(app)

def create_app():
    # 创建 Flask 应用程序实例
    app = Flask('FoodieDiary')
    app.config.from_object('config.Config')  # 假设你有一个配置文件 config.py

    with app.app_context():
        # 在应用程序上下文中初始化应用程序
        init_app(app)
        # 导入并注册 authrouter 蓝图
        from .routers import authrouter as auth_blueprint
        app.register_blueprint(auth_blueprint)
        # 导入并注册 personal_query_app 蓝图
        from .routers.customers import personal_query_app
        app.register_blueprint(personal_query_app)
        # 返回应用程序实例
        return app