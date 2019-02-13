# python 中用 "from . import <some-module>"語法來表示相對匯入
from flask import render_template
from . import auth

@auth.route('/login')
def login:
    return render_template('auth/login.html')
    #render_template --> 預設模板路徑為：相對於"app\templates" 下
