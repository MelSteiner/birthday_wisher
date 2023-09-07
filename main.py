import pandas
import smtplib
import datetime as dt
import random

MY_EMAIL = "####"
PASSWORD = "****"
letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient="records")

now = dt.datetime.now()
day_today = now.day
month_today = now.month


for person in birthdays:
    if person['month'] == month_today and person['day'] == day_today:
        print_name = person['name']
        with open(f"./Letter_templates/{random.choice(letters)}") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", print_name)

        print(letter)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)

            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=person['email'],
                msg=f"Subject:It is your birthday!\n\n{letter}"
            )
