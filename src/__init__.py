import logging
from flask import Flask
from config import Config
from .extensions import db # 从 models 模块导入 db 对象
from .models import authmodel
from .models.customers import Personal_Querymodel
from .models.windows import Windowmodel
from .routers import authrouter
from .routers.customers import Personal_Queryrouter
from .routers.windows import Windowrouter
from .services import authservice
from .services.customers import Personal_Query
from .services.windows import Window



def init_app(app):
    # 初始化应用程序，绑定数据库
    db.init_app(app)

def create_app(config_class=Config):
    # 创建 Flask 应用程序实例
    app = Flask('FoodieDiary')
    app.config.from_object(config_class)  # 假设你有一个配置文件 config.py
    # 配置日志记录
    logging.basicConfig(level=app.config['LOGGING_LEVEL'])
    logger = logging.getLogger(__name__)
    logger.info('应用程序启动')

    with app.app_context():
        # 在应用程序上下文中初始化应用程序
        init_app(app)
        db.create_all()  # 创建所有定义的表
        # 导入并注册 authrouter 蓝图
        from .routers import authrouter_app as auth_blueprint
        app.register_blueprint(auth_blueprint)
        # 导入并注册 personal_query_app 蓝图
        from .routers.customers import personal_query_app
        app.register_blueprint(personal_query_app)
        # 导入并注册 window_app 蓝图
        from .routers.windows import window_app
        app.register_blueprint(window_app)
        # 返回应用程序实例
        for rule in app.url_map.iter_rules():
            print(f"Endpoint: {rule.endpoint}, URL: {rule}")
        return app
