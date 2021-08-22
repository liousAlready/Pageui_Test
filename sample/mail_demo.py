# -*- coding: utf-8 -*-
# @Time : 2021/8/13 15:46
# @Author : Limusen
# @File : mail


import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_server = 'smtp.qq.com'  # 邮件服务器地址
smtp_sender = '1650503480@qq.com'  # 邮箱名
smtp_sender_password = "tnmwuuycifiedcah"  # 授权码

smtp_receiver = '1650503480@qq.com,812527673@qq.com'  # 收件人
smtp_cc = '1695403591@qq.com'  # 抄送人
smtp_subject = "自动化测试报告（测试版）"  # 邮件主题
smtp_body = '测试邮件'  # 邮件正文
smtp_file = "a"

msg = MIMEText(smtp_body, 'html', "utf-8")  # 邮件信息对象
msg['form'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

smtp = smtplib.SMTP()
smtp.connect(smtp_server)  # qq邮箱默认 465
smtp.login(user=smtp_sender, password=smtp_sender_password)
smtp.sendmail(smtp_sender, smtp_receiver.split(',') + smtp_cc.split(','), msg.as_string())
