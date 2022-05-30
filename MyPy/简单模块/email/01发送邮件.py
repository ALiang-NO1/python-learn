import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = input('邮件服务地址：')  # 设置服务器地址
mail_user = input('账号：')  # 发邮件的账户名
mail_pass = input('密码：')  # 授权码

receivers = ['3467166174@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个设置格式，plain：文本，html：HTML格式，第三个 utf-8 设置编码
message = MIMEText('email 测试————亮', 'plain', 'utf-8')
message['From'] = Header("3467166174@qq.com")  # 邮件中的发件人
message['To'] = Header("3467166174@qq.com")  # 邮件中的收件人

subject = 'python测试邮件'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.set_debuglevel(1)  # 打印出和 SMTP 服务器交互的所有信息

    # smtpObj.ehlo()  # 向邮箱发送SMTP 'ehlo' 命令
    # smtpObj.starttls()
    smtpObj.login(mail_user, mail_pass)
    # 发件人邮箱账号、收件人邮箱账号、发送邮件
    smtpObj.sendmail(mail_user, receivers, message.as_string())
    print("邮件发送成功")

except smtplib.SMTPException as e:
    print("Error: 无法发送邮件,", e)