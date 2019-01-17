# 主藍圖中的錯誤處理函式
from flask import render_template
from . import main


@main.app_errorhandler(404)
# 自訂404錯誤網頁
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
# 自訂500錯誤網頁
def internal_server_error(e):
    return render_template('500.html'), 500
