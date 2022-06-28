"""

    app 主視圖

    create by : jay
    creata at : 2022/06/28

"""

from . import main

@main.route("/")
def index():
    return "<h1>Hello, World</h1>"