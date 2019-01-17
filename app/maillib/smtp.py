# 使用Google的SMPT發送Mail
#  _*_ coding: UTF-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方 SMTP 服務: Google SMTP Server：smtp.gmail.com
mail_host = 'smtp.gmail.com'
mail_user = 'chinxxxxxweb@gmail.com'
mail_pass = '-----------------'

# Add the From: and To: headers at the start!
msg = MIMEText('content')
msg['Subject'] = 'Python EMail Send Test , Use by gmail send this mail  ......'
msg['From'] = mail_user
msg['To'] = 'angelak.tw@gmail.com'

try:
    # 一般SMTP Port=25, google SMTP PORT =465
    smtpobj = smtplib.SMTP_SSL(mail_host, 465)
    smtpobj.ehlo()
    smtpobj.login(mail_user, mail_pass)
    smtpobj.send_message(msg)
    print("郵件發送成功!!!! ")
except smtpobj.SMTPException:
    print("Error : 無法發送郵件 !!!! ")
smtpobj.quit()
