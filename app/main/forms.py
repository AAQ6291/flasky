from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    # 定義表單類別
    # validators 驗證函式, DataRequired() 保證送出的欄位不是空值
    name = StringField('What is Your name? ', validators=[DataRequired()])
    password = StringField('Please Enter your Password ? ', validators=[DataRequired()])
    submit = SubmitField('Submit')
