from main import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Create Database Fields (建立資料表欄位)


class Todo(db.Model):
    # __table__name = 'user_table'，若不寫則看 class name
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(80))

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return '<Todo %r>' % self.content


class Role(db.Model):
    # 模型定義
    # Define Role Modle's (角色) Table
    # __table__name = 'user_table'，若不寫則看 class name
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


# Create Forms Class  (建立表單類別)


class NameForm(FlaskForm):
    # 定義Name表單類別
    # validators 驗證函式, DataRequired() 保證送出的欄位不是空值
    name = StringField('What is your name? ', validators=[DataRequired()])
    submit = SubmitField('Submit')
