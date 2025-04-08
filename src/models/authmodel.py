"""
from ..extensions import db
#从 src 模块中导入 db 对象，这通常是一个 SQLAlchemy 数据库实例。
from werkzeug.security import generate_password_hash, check_password_hash
#从 werkzeug.security 模块中导入两个函数，用于生成和检查密码的哈希值。
class User(db.Model):
    # 定义用户模型类，继承自SQLAlchemy的db.Model，db.Column是SQLAlchemy 中用于定义数据库列的函数
    id = db.Column(db.Integer, primary_key=True)  # 用户ID，主键
    account = db.Column(db.String(80), unique=True, nullable=False)  # 用户名，唯一且不能为空
    password_hash = db.Column(db.String(120), nullable=False)  # 密码哈希值，不能为空

    def set_password(self, password):
        # 设置用户密码，生成并存储密码的哈希值
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # 检查输入的密码是否与存储的哈希值匹配
        return check_password_hash(self.password_hash, password)

        # 插入数据

    def insert_user(account, password):
        new_user = User(account=account)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        # 查询数据

    def query_user(account):
        user = User.query.filter_by(account=account).first()
        if user:
            print(f'Found user: {user.account}')
        return user

        # 更新数据

    def update_user_password(account, new_password):
        user = User.query.filter_by(account=account).first()
        if user:
            user.set_password(new_password)
            db.session.commit()

        # 删除数据

    def delete_user(account):
        user = User.query.filter_by(account=account).first()
        if user:
            db.session.delete(user)
            db.session.commit()
"""

from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(20), nullable=False)  # 限定哈希值为20位

    def set_password(self, password):
        # 生成哈希值并截取前20位

        #full_hash = generate_password_hash(password, method='pbkdf2:sha256')
        self.password_hash = password

    def check_password(self, password):
        # ���成哈希值并截取前20位进行匹配
        #full_hash = generate_password_hash(password,method='pbkdf2:sha256')
        #print(full_hash[-20:])
        #print(self.password_hash)
        return self.password_hash == password

    @staticmethod
    def insert_user(account, password):
        new_user = User(account=account)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

    @staticmethod
    def query_user(account):
        return User.query.filter_by(account=account).first()

    @staticmethod
    def update_user_password(account, new_password):
        user = User.query.filter_by(account=account).first()
        if user:
            user.set_password(new_password)
            db.session.commit()

    @staticmethod
    def delete_user(account):
        user = User.query.filter_by(account=account).first()
        if user:
            db.session.delete(user)
            db.session.commit()