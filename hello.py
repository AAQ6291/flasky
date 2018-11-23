from flask import Flask, request, render_template
from flask import make_response  # 回傳一個回應物件
from flask import abort          # 處理錯誤狀態
from flask_script import Manager  # 提供外不指令

# Flash_boostrap 包含所有Bootstrap檔案 & 基礎結構模板
from flask_bootstrap import Bootstrap
from flask_moment import Moment

app = Flask(__name__)
manager = Manager(app)
moment = Moment(app)
# app 利用 Jinja2 的模板繼承並擴充此套件
bootstrap = Bootstrap(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    # 瀏覽器資訊
    user_agent = request.headers.get('User-Agent')

    # 使用轉譯模板, 附帶參數傳送
    return render_template('index.html', user_agent=user_agent)


@app.route('/user/<name>')     # 動態路由
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
