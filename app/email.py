from threading import Thread
from flask import current_app, render_template
from flask_mail import Mail, Message
from . import mail


def send_async_email(app, msg):
    # 支援非同步email
    with app.app_context():
        mail.send(msg)


def send_mail(to, subject, template, **kwargs):
    # 支援非同步email
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['FLASKY_MAIL_SENDER', recipients=[to]])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(temple, '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
