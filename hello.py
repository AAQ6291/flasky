from flask import Flask, request, render_template
from flask import make_response  # 回傳一個回應物件
from flask import abort          # 處理錯誤狀態

app = Flask(__name__)


@app.route('/')
def index():
    # 瀏覽器資訊
    user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser id {}</p>'.format(user_agent)
    # return '<h1>Hello World!</h1>'

    # 使用轉譯模板, 附帶參數傳送
    return render_template('index.html', user_agent=user_agent)


@app.route('/user/<name>')     # 動態路由
def get_user(name):
    user = load_user(name)
    if not user:
        abort(404)
    return render_template('user.html', name=name)


def load_user(name):
    # return '<h1>Hello, {}!</h1>'.format(name)
    # return render_template('user.html', name=name)
    return name
