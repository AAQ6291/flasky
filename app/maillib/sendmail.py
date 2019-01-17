import smtplib
from email.mime.text import MIMEText

gmail_user = 'chin6eb@gmail.com'
gmail_password = '----------------'  # your gmail password

msg = MIMEText('content')
msg['Subject'] = 'Test'
msg['From'] = gmail_user
msg['To'] = 'anxxxx@gmail.com'

# 一般SMTP Port=25, google SMTP PORT =465
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()

print('Email sent!')
