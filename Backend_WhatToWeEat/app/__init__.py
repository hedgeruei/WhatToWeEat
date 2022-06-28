"""

    app 初始化

    create by : jay
    create at : 2022/06/28

"""

from flask import Flask

from config import config

def creat_app(config_name : str) -> Flask:
    """ 創建 app 實例 """

    app = Flask(__name__, instance_relative_config = True)
    config[config_name].init_app(app)

    # register blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app