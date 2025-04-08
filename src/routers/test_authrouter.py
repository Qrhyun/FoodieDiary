


import pytest
from unittest.mock import patch, MagicMock
from src.routers.authrouter import register, login
from src import create_app

# 模拟服务层的函数
def mock_register_user(account, password):
    return True, '新用户创建成功'

def mock_login_user(account, password):
    return True, '登录成功'

@pytest.fixture
def app():
    return create_app()

# 测试注册函数
def test_register(app):
    data = {
        'account': 'testuser',
        'password': '1234'
    }
    # 模拟请求对象
    with app.test_request_context('/register', method='POST', json=data):
        # 模拟服务层函数
        with patch('src.services.authservice.register_user', side_effect=mock_register_user):
            with app.app_context():
                response = register()
                assert response.status_code == 200
                assert response.get_json() == {'message': '新用户创建成功'}

# 测试登录函数
def test_login(app):
    data = {
        'account': 'testuser',
        'password': 'testpassword'
    }
    # 模拟请求对象
    with app.test_request_context('/login', method='POST', json=data):
        # 模拟服务层函数
        with patch('src.services.authservice.login_user', side_effect=mock_login_user):
            with app.app_context():
                response = login()
                assert response.status_code == 200
                assert response.get_json() == {'message': '登录成功'}