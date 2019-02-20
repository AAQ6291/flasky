from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from . import db, login_manager
from flask_login import UserMixin

# Create Database Fields (建立資料表欄位)
#在User模型中作 密碼雜湊化
#UserMixin幫我們記錄了四種用戶狀態：

class Role(db.Model):
    # 模型定義
    # Define Role Modle's (角色) Table
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)  # set pkey=id
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role', lazy='dynamic')  # 關係連結

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(80), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # 連結到<roles>.<id>

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username        

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
