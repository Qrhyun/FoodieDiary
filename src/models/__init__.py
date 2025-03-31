#从当前包中的 authmodel 模块导入 User 类
from .authmodel import User
#导入和定义 db 对象
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()