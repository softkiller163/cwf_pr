import socket
import smtplib
import sys

code = 0

message = ("""To: weifeng.chen@newtouch.cn
From: weifeng.chen@newtouch.cn
Subject:SMTP test
Hello smtp""")

server = 'mail.newtouch.cn'

try:
    s = smtplib.SMTP(server)
    try:
        s.login('yourname', "yourpass")
    except (smtplib.SMTPException) as e:
        print('Auth fail')
    print("Auth Succ")
    s.sendmail('weifeng.chen@newtouch.cn', 'weifeng.chen@newtouch.cn', message)
    code = s.ehlo()
except (smtplib.SMTPException) as e:
    print('send err2 %d' % code)
    print(e)
else:
    print('send OK {:}'.format(*code))





