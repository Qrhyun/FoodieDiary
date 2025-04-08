"""
import logging
class TestConfig:
    DEBUG = True  # 开启调试模式
    SECRET_KEY = '1234'  # 用于保护会话的密钥

    # 数据库配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://food:1234@47.115.226.248/FoodieDiary_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用对模型修改的跟踪
    SQLALCHEMY_ECHO = True  # 开启SQLAlchemy的调试模式

    # 启用日志记录
    LOGGING_LEVEL = logging.DEBUG
"""