"""

    app 主程式

    create by : jay
    create at : 2022/06/28

"""

import os

from app import creat_app

app = creat_app(os.environ.get("FLASK_CONFIG") or "default")
