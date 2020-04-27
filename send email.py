import smtplib

gmail_user = "you@gmail.com"
gmail_password = "PASSWORD"

sent_from = gmail_user
deliver = ['email1@gmail.com', 'email2@gmail.com', 'email3@gmail.com', 'email4@gmail.com', 'email5@gmail.com']
subject = 'Test Message'
body = "Hey guys, just wanted to try sending this email to see if I am succesful in sending the email.\n\n- Me"

message = 'Subject: {}\n\n{}'.format(subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)

    for to in deliver:
        server.sendmail(sent_from, to, message)
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')
