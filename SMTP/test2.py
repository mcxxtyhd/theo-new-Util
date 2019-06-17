
import smtplib

from email.mime.text import MIMEText

from email.header import Header

sender = '353950534@qq.com' #发送邮箱地址

pwd = 'iwnnqbxzonyjbiad' #授权码

receivers = ('353950534@qq.com')#目标邮箱地址

# 三个参数：第一个为文本内容，第二个为plain设置文本格式，第三个为utf-8编码

message = MIMEText("Python发送邮件","plain",'utf-8')

message ['From'] =' a <发送邮箱地址>'

message ['To'] =' b <目标邮箱地址>'

#邮件主题

subject = "这是subject"

message["Subject"] = Header(subject,"utf-8")

try:

    #SMTP服务器和SSL协议端口号，使用非本地服务器，需要建立ssl连接。

    smtpObj = smtplib.SMTP_SSL("smtp.qq.com",465)

    smtpObj.login(sender,pwd)

    smtpObj.sendmail(sender,receivers,message.as_string())

    print("邮件发送成功")

except smtplib.SMTPException as e:

    print("Error：无法发送邮件.Case:%s"%e)