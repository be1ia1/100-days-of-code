"""Send wish letter if date is birthday"""
import datetime as dt
import glob
from random import choice
import smtplib
import pandas as pd

EMAIL = "belial.agula@gmail.com"
with open('secret.txt', encoding="utf-8") as fo:
    PASSWORD = fo.read()


def send_email(body_text, to_email):
    """Send via gmail"""
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject: Happy Birthday!\n\n{body_text}")


now = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")

happy_birthday = birthdays.loc[(birthdays["month"] == now.month) & (
    birthdays["day"] == now.day)]

if not happy_birthday.empty:
    b_name = happy_birthday.name.values[0]
    b_email = happy_birthday.email.values[0]
    base_letter_file = choice(glob.glob("letter_templates/*"))
    with open(base_letter_file, encoding="utf-8") as fo:
        text = fo.read()
    text = text.replace('[NAME]', b_name)
    send_email(text, b_email)
