# 使用Google的SMPT發送Mail
#  _*_ coding: UTF-8 _*_

import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 第三方 SMTP 服務: Google SMTP Server：smtp.gmail.com
mail_host = 'smtp.gmail.com'
mail_user = 'chinxxxxb@gmail.com'
mail_pass = '-----------------'

# Add the From: and To: headers at the start!
msg = MIMEText(
    'Python EMail Send Test , Use by gmail send this mail  ...... ', 'plain', 'utf-8')
msg['From'] = Header('Python smtplib ', 'utf-8')
msg['To'] = Header('Gmail Send Test! 郵件發送測試!')

subject = 'Python SMTP 郵件發送測試'
msg['Subject'] = Header(subject, 'utf-8')

try:
    smtpobj = smtplib.SMTP_SSL()
    smtpobj.connect(mail_host, 465)  # SMTP Port=25
    smtpobj.login(mail_user, mail_pass)
    smtpobj.sendmail(mail_user, 'angela_kuo@liveabc.com', msg.as_string())
    print("郵件發送成功!!!! ")
except smptlib.SMTPException:
    print("Error : 無法發送郵件 !!!! ")
smtpobj.quit()
