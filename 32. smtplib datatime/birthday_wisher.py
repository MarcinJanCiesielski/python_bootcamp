##################### Extra Hard Starting Project ######################


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import csv
import datetime as dt
import random
import secret
templates = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]

def generate_message(name, template):
    PATTERN_TO_REPLACE = "[NAME]"
    whishes = ""
    with open(template, encoding="utf8", mode="r") as template:
        ws = template.read()
        whishes = ws.replace(PATTERN_TO_REPLACE, name)
        message = "Subject:Best Whishes\n\n" + whishes

        return message

def send_email(email, message):
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=secret.my_email, password=secret.password)
        connection.sendmail(from_addr=secret.my_email, to_addrs=email, msg=message)

def check_jubilee():
    jubilees = []
    now = dt.datetime.now()
    with open("./birthdays.csv", encoding="utf8", mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if int(row["month"]) == now.month and int(row['day']) == now.day:
                jubilees.append(row)

    return jubilees

jubilees = check_jubilee()
for jubilee in jubilees:
    msg = generate_message(jubilee["name"], random.choice(templates))
    send_email(jubilee["email"], msg)
