
from flask import Blueprint, request, jsonify
from src.services.authservice import register_user, login_user
from . import authrouter  # 导入authrouter蓝图

@authrouter.route('/register', methods=['GET'])
def register():
    # 注册用户
    # 从请求参数中获取用户名和密码
    username = request.args.get('username')
    password = request.args.get('password')
    # 调用注册用户服务
    success, message = register_user(username, password)
    # 返回注册结果，错误是400
    return jsonify({'message': message}), (200 if success else 400)

@authrouter.route('/login', methods=['GET'])
def login():
    # 用户登录
    # 从请求参数中获取用户名和密码
    username = request.args.get('username')
    password = request.args.get('password')
    # 调用用户登录服务
    success, message = login_user(username, password)
    # 返回登录结果，错误是401
    return jsonify({'message': message}), (200 if success else 401)