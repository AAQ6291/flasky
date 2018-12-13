# os -- 調用操作系統命令--建立,刪除,查詢文件
import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

# get file path and file directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Set Database & Create APP
app = Flask(__name__)
# set use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# setting database -- sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

db = SQLAlchemy(app)


class NameForm(FlaskForm):
    # 定義表單類別
    # validators 驗證函式, DataRequired() 保證送出的欄位不是空值
    name = StringField('What is your name? ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
# 自訂404錯誤網頁
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
# 自訂500錯誤網頁
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    # 瀏覽器資訊
    user_agent = request.headers.get('User-Agent')
    # 傳送時間 current_time
    current_time = datetime.utcnow()
    # 表單定義
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Look like you have change your name! ')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    # 使用轉譯模板, 附帶參數傳送(瀏覽器資訊, 表單, name變數)
    return render_template('index.html', user_agent=user_agent, current_time=current_time, form=form, name=session.get('name'))


@app.route('/user/<name>')     # 動態路由
# 自訂User網頁
def user(name):
    return render_template('user.html', name=name)
