"""Send quote from quotes.txt every Sunday"""
import smtplib
import datetime as dt
from random import choice

EMAIL = "belial.agula@gmail.com"
with open('secret.txt', encoding="utf-8") as fo:
    PASSWORD = fo.read()

with open("quotes.txt", encoding="utf-8") as fo:
    quotes = fo.readlines()

def send_email(body_text):
    """Send quote via gmail"""
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs="gula@pr.km.ua",
                            msg=f"Subject: Hello\n\n{body_text}")

now = dt.datetime.now()
if now.isoweekday() == 7:
    send_email(choice(quotes))
