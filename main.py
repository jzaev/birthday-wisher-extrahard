
import pandas as pd
import datetime as dt
import random
import smtplib


def send_email(text, email):
    my_email = "juryzaev@gmail.com"
    my_password = input("input Google email password")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject: Happy monday\n\n{text}")
        connection.close()


def today_congratulations():
    with open("birthdays.csv") as birthday_file:
        birthdays = pd.read_csv(birthday_file)
    today_month = dt.datetime.now().month
    today_day = dt.datetime.now().day
    bd_persons = birthdays.query("month == @today_month and day == @today_day")
    # bd_persons = bd_persons[birthdays.day == dt.datetime.now().day]

    for row in bd_persons.iterrows():
        with open(f"letter_templates/letter_{random.choice([1, 2, 3])}.txt") as letter_file:
            send_email(letter_file.read().replace("[NAME]", row[1]["name"]), row[1]["email"])


today_congratulations()
