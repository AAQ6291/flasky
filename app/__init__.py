# <<< 完成 app 的初始化! >>>

# Flash_boostrap 包含所有Bootstrap檔案 & 基礎結構模板
# Flask_moment 解析、驗證、操作、格式化日期
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy  # set database using SQLAlchemy
from config import config
from datetime import datetime
from flask_login import LoginManager

# app 利用 Jinja2 的模板繼承並擴充此套件
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# 傳送時間 current_time
current_time = datetime.utcnow()

#Flask_Login 初始化
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    # from_object : 接收 "config.py" 定義的組態類別
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # 完成app初始化
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 註冊藍圖
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # 註冊身分驗證藍圖
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    ## url_prefix：定義所有的路由都會加上"前置詞"(在此為 --> /auth), 如/login路由會註冊為/auth/login

    return app
