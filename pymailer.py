"""Minimal send_mail functionality with Python."""
import smtplib
from email.mime.text import MIMEText

def send_mail(from_addr, to_addr, subject, message):
    """Send an email."""
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    if type(to_addr) != type([]):
        to_addr = [to_addr]
    s = smtplib.SMTP('localhost')
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.quit()

if __name__ == "__main__":
    send_mail("from@example.com", "to@example.com", "Hello World!", "Email via Python.")