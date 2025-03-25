"""
from flask import Flask, render_template
from src.customers.Personal_Query import personal_query_app
from src.windows.window import window_app

app = Flask(__name__, template_folder='templates')

# Register blueprints
app.register_blueprint(personal_query_app, url_prefix='/personal_query')
app.register_blueprint(window_app, url_prefix='/window')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personal_query')
def index_personal_query():
    meal = []
    return render_template('customers/ui/recent_meal.html', meal=meal)

@app.route('/window')
def index_window():
    return render_template('windows/ui/window.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
"""

from flask import Flask

# 假设 Personal_Query 和 window 是在 src 目录下的模块
from src.customers.Personal_Query import personal_query_app
from src.windows.window import window_app

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(personal_query_app, url_prefix='/personal_query')
app.register_blueprint(window_app, url_prefix='/window')

@app.route('/')
def index():
    # 首页返回简单的欢迎信息
    return "Welcome to Foodie Diary!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)