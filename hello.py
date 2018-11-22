from flask import Flask, request, render_template
from flask import make_response  # 回傳一個回應物件
from flask import abort          # 處理錯誤狀態
# Flash_boostrap 包含所有Bootstrap檔案 & 基礎結構模板
from flask.extend.bootstrap import Bootstrap

app = Flask(__name__)
# app 利用 Jinja2 的模板繼承並擴充此套件
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    # 瀏覽器資訊
    user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser id {}</p>'.format(user_agent)
    # return '<h1>Hello World!</h1>'

    # 使用轉譯模板, 附帶參數傳送
    return render_template('index.html', user_agent=user_agent)


@app.route('/user/<name>')     # 動態路由
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
