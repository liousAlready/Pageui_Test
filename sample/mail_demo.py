# -*- coding: utf-8 -*-
# @Time : 2021/8/13 15:46
# @Author : Limusen
# @File : mail


import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, '..', 'reports/禅道-测试报告V1.0.zip')

smtp_server = 'smtp.qq.com'  # 邮件服务器地址
smtp_sender = '1650503480@qq.com'  # 邮箱名
smtp_sender_password = "tnmwuuycifiedcah"  # 授权码

smtp_receiver = '1650503480@qq.com'  # 收件人
smtp_cc = '1695403591@qq.com'  # 抄送人
smtp_subject = "自动化测试报告（测试版）"  # 邮件主题
smtp_body = '测试邮件'  # 邮件正文
smtp_file = file_path

# msg = MIMEText(smtp_body, 'html', "utf-8")  # 邮件信息对象
# msg['form'] = smtp_sender
# msg['to'] = smtp_receiver
# msg['Cc'] = smtp_cc
# msg['subject'] = smtp_subject

msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    # / Users / liuqingjun / PycharmProjects / PO_UI_Test_Framework /reports/禅道自动化测试报告V2.3/禅道自动化测试报告.zip
    mime = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', smtp_file.split('/')[-1]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body, "html", "utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject

smtp = smtplib.SMTP()
smtp.connect(smtp_server)  # 465
smtp.login(user=smtp_sender, password=smtp_sender_password)
smtp.sendmail(smtp_sender, smtp_receiver.split(',') + smtp_cc.split(','), msg.as_string())
