"""
import pytest
import logging
from src import create_app, db
from src.models.authmodel import User
from src.services.authservice import register_user, login_user, update_user_password, delete_user
from .config import TestConfig

@pytest.fixture(scope='module')
def test_client():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()

def test_register_user(test_client):
    logging.info('测试注册用户')
    success, message = register_user('testuser', 'password')
    assert success
    assert message == "新用户创建成功"
    user = User.query_user('testuser')
    assert user is not None
    assert user.check_password('password')

def test_login_user(test_client):
    logging.info('测试用户登录')
    register_user('testuser', 'password')
    success, message = login_user('testuser', 'password')
    assert success
    assert message == "登录成功"

def test_update_user_password(test_client):
    logging.info('测试更新用户密码')
    register_user('testuser', 'password')
    success, message = update_user_password('testuser', 'newpassword')
    assert success
    assert message == "密码更新成功"
    user = User.query_user('testuser')
    assert user.check_password('newpassword')

def test_delete_user(test_client):
    logging.info('测试删除用户')
    register_user('testuser', 'password')
    success, message = delete_user('testuser')
    assert success
    assert message == "用户删除成功"
    user = User.query_user('testuser')
    assert user is None
"""




# test_auth.py
import requests

url = 'http://127.0.0.1:5000/auth/register'  # 确保 URL 与您的蓝图注册匹配
headers = {'Content-Type': 'application/json'}
data = {
    "account": "testuser",
    "password": "testpassword"
}

response = requests.post(url, headers=headers, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
