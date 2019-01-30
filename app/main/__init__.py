# 建立藍圖blueprint
# python 中用 "from . import <some-module>"語法來表示相對匯入
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors