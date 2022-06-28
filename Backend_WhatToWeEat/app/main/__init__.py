"""

    建立 app 主藍圖

    create by : jay
    create at : 2022/06/28

"""

from flask import Blueprint

main = Blueprint("main", __name__)

from . import views