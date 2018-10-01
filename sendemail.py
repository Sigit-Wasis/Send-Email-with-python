***
Konfig di bawah ini digunakan untuk mengirim email melalui python
***

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "sigitghotic2001@gmail.com" # email pengirim
toaddr = "sigitqodr2018@gmail.com" # email tujuan

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "qodr" # judul pesan
 
body = "menjadi seorang programmer itu seru" # isi pesan

msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "barakallah") # password pengirim
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()