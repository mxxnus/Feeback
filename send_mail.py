import smtplib
from email.mime.text import MIMEText


def send_mail(customer, source, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'c8f562b31c324a'
    password = 'd268cd422f17c7'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Source: {source}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Social Sneaker Feedback'
    msg["From"] = sender_email
    msg['To'] = receiver_email

    # send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
