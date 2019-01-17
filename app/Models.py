from . import db

# Create Database Fields (建立資料表欄位)


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
