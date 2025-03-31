from src.models.authmodel import User
from src import db

def register_user(username, password):
    # 注册用户
    user = User.query.filter_by(username=username).first()  # 检查用户名是否已存在
    if user:
        return False, "您的用户已经存在，请登录"  # 用户名已存在，返回失败消息
    new_user = User(username=username)  # 创建新用户实例
    new_user.set_password(password)  # 设置用户密码
    db.session.add(new_user)  # 将新用户添加到数据库会话
    db.session.commit()  # 提交会话，保存新用户
    return True, "新用户创建成功"  # 返回成功消息

def login_user(username, password):
    # 用户登录
    user = User.query.filter_by(username=username).first()  # 查找用户名对应的用户
    if user and user.check_password(password):  # 检查用户是否存在且密码正确
        return True, "登录成功"  # 登录成功，返回成功消息
    return False, "错误的用户名或者密码"  # 用户名或密码无效，返回失败消息