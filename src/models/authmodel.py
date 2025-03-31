from src import db
#从 src 模块中导入 db 对象，这通常是一个 SQLAlchemy 数据库实例。
from werkzeug.security import generate_password_hash, check_password_hash
#从 werkzeug.security 模块中导入两个函数，用于生成和检查密码的哈希值。
class User(db.Model):
    # 定义用户模型类，继承自SQLAlchemy的db.Model，db.Column是SQLAlchemy 中用于定义数据库列的函数
    id = db.Column(db.Integer, primary_key=True)  # 用户ID，主键
    username = db.Column(db.String(80), unique=True, nullable=False)  # 用户名，唯一且不能为空
    password_hash = db.Column(db.String(120), nullable=False)  # 密码哈希值，不能为空

    def set_password(self, password):
        # 设置用户密码，生成并存储密码的哈希值
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # 检查输入的密码是否与存储的哈希值匹配
        return check_password_hash(self.password_hash, password)