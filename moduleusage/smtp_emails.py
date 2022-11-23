import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# "noreplaypivoxupdates@yahoo.com"  # "bhargv.tanguturi@pivoxlabs.com"
username = "noreplaypivoxnotifications@gmail.com"
password = "pivox$123"
mail_from = "noreplaypivoxnotifications@gmail.com"
mail_to = "bhargavreddy033@gmail.com"
mail_subject = "Test Subject"
mail_body = "This is a test message"

mimemsg = MIMEMultipart()
mimemsg['From'] = mail_from
mimemsg['To'] = mail_to
mimemsg['Subject'] = mail_subject
mimemsg.attach(MIMEText(mail_body, 'plain'))
# 'smtp.mail.yahoo.com' # smtp-mail.outlook.com
connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
connection.starttls()
connection.login(username, password)
connection.send_message(mimemsg)
connection.quit()
