from src.models.authmodel import User
from src import db

def register_user(account, password):
    # 注册用户
    user = User.query_user(account)  # 使用模型中的方法查询用户
    if user:
        return False, "您的用户已经存在，请登录"  # 用户名已存在，返回失败消息
    User.insert_user(account, password)  # 使用模型中的方法插入新用户
    return True, "新用户创建成功"  # 返回成功消息

def login_user(account, password):
    # 用户登录
    user = User.query_user(account)  # 使用模型中的方法查询用户
    if user and user.check_password(password):  # 检查用户是否存在且密码正确
        return True, "登录成功"  # 登录成功，返回成功消息
    return False, "错误的用户名或者密码"  # 用户名或密码无效，返回失败消息

def update_user_password(account, new_password):
    # 更新用户密码
    User.update_user_password(account, new_password)  # 使用模型中的方法更新密码
    return True, "密码更新成功"  # 返回成功消息

def delete_user(account):
    # 删除用户
    User.delete_user(account)  # 使用模型中的方法删除用户
    return True, "用户删除成功"  # 返回成功消息