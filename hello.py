from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    # 瀏覽器資訊
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser id {}</p>'.format(user_agent)
    # return '<h1>Hello World!</h1>'


@app.route('/user/<name>')     # 動態路由
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
