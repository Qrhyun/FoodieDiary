from src import create_app #从 src 模块中导入 create_app 函数

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)