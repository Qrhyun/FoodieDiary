from flask import Blueprint, request, jsonify
from src.services.authservice import register_user, login_user
from . import authrouter  # 导入authrouter蓝


@authrouter.route('/register', methods=['POST'])
def register():
    # 注册用户
    # 从请求的JSON数据中获取用户名和密码
    data = request.get_json()
    account = data.get('account')
    password = data.get('password')

    if not account or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    # 调用注册用户服务
    success, message = register_user(account, password)
    # 返回注册结果，错误是400
    return jsonify({'message': message}), (200 if success else 400)


@authrouter.route('/login', methods=['POST'])
def login():
    # 用户登录
    # 从请求的JSON数据中获取用户名和密码
    data = request.get_json()
    account = data.get('account')
    password = data.get('password')

    if not account or not password:
        return jsonify({'message': '用户名和密码不能为空'}), 400

    # 调用用户登录服务
    success, message = login_user(account, password)
    # 返回登录结果，错误是401
    return jsonify({'message': message}), (200 if success else 401)