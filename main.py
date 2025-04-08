# main.py
import sys
from pathlib import Path
from src import create_app


# 获取项目根目录的绝对路径
project_root = Path(__file__).resolve().parent.parent

# 将项目根目录添加到 sys.path
sys.path.insert(0, str(project_root))

# 创建 Flask 应用实例
app = create_app()

# 运行应用
if __name__ == '__main__':
    app.run(debug=True)