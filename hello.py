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
from flask_migrate import Migrate

# get file path and file directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# 設置flask-wtf
app.config['SECRET_KEY'] = 'hard to guess string'

# setting database -- sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# set use less memory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app 利用 Jinja2 的模板繼承並擴充此套件
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # 資料庫遷移用


class Role(db.Model):
    # 模型定義
    # Define Role Modle's (角色) Table
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)  # set pkey=id
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')  # 關係連結

    def __repr__(self):
        return '<Role %r>' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    # 連結到<roles>.<id>
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class NameForm(FlaskForm):
    # 定義表單類別
    # validators 驗證函式, DataRequired() 保證送出的欄位不是空值
    name = StringField('What is Your name? ', validators=[DataRequired()])
    password = StringField('Please Enter your Password ? ',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.shell_context_processor
# 添加shell(殼層)環境,
def make_shell_context():
    # Shell環境處理常式回傳: "字典"--包含資料庫實例與模型
    return dict(db=db, User=User, Role=Role)


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
        # 使用filter_by()查詢資料庫
        user = User.query.filter_by(username=form.name.data,).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.Commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ' '
        return redirect(url_for('index'))
    # 使用轉譯模板, 附帶參數傳送(瀏覽器資訊, 表單, name變數)
    return render_template('index.html', current_time=current_time, form=form, name=session.get('name'), known=session.get('known', False))


@app.route('/user/<name>')     # 動態路由
# 自訂User網頁
def user(name):
    return render_template('user.html', name=name)
