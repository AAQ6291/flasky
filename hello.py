# Flash_boostrap 包含所有Bootstrap檔案 & 基礎結構模板
# Flask_moment 解析、驗證、操作、格式化日期
import os  # 調用操作系統命令--建立,刪除,查詢文件
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy  # set database using SQLAlchemy

# get file path and file directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 設置flask-wtf
app.config['SECRET_KEY'] = 'hard to guess string'
# set use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# setting database -- sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app 利用 Jinja2 的模板繼承並擴充此套件
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)


class Role(db.Model):
    # 模型定義
    # Define Role Modle's (角色) Table
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)  # set pkey=id
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')  # 關係連結

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # 連結到<roles>.<id>
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    # 定義表單類別
    # validators 驗證函式, DataRequired() 保證送出的欄位不是空值
    name = StringField('What is your name? ', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
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
def user(name):
    return render_template('user.html', name=name)
