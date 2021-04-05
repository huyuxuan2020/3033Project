#!/usr/bin/python
import os
import smtplib
import qrcode
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import random

mail_host="smtp.qq.com"
mail_user="425310997@qq.com"
mail_pass="XXXXXX"   #password
 
 
sender = '425310997@qq.com'
receivers = ['zshldota2@gmail.com']

R=random.randint(1, 9)
#need to use real user's password

msg = MIMEMultipart()
msg['Subject'] = 'subject'
msg['From'] = 'e@mail.cc'
msg['To'] = 'e@mail.cc'

text = MIMEText("this is your QR code:")
image = MIMEImage(qrcode.make(R))
msg.attach(text)
msg.attach(image)
 
 
 
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print "Successfully"
except smtplib.SMTPException:
    print "Error"
