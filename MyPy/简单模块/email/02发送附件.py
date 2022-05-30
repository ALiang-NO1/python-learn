from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    print('name:', name, '; addr:', addr)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# from_addr = input('From: ')
from_addr = '3467166174@qq.com'
password = input('Password: ')
# to_addr = input('to: ')
to_addr = '3467166174@qq.com'
# smtp_server = input('SMTP server: ')  # smtp.qq.com pop.qq.com mail.qq.com
smtp_server = 'pop.qq.com'  # smtp.qq.com pop.qq.com mail.qq.com

msg = MIMEMultipart()  # 创建邮件对象

msg.attach(MIMEText('hello send by Python by aLiang', 'plain', 'utf-8'))  # 正文是MIMEText

with open(r'E:\图片\小图\HBX.png', 'rb') as f:  # 从本地读取一个文件作为附件
    mime = MIMEBase('image', 'png', filename='HBX.png')
    mime.add_header('Content-Disposition', 'attachment', filename='HBX.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())  # 读入附件内容
    encoders.encode_base64(mime)  # 编码
    msg.attach(mime)

msg['From'] = _format_addr('Python迷 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候......', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print('发送成功！')