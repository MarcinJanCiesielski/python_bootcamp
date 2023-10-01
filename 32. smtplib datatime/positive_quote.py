import random
import smtplib
import datetime as dt
import secret

with open("./quotes.txt", encoding="utf8", mode="r") as q:
    quotes = q.readlines()

message="Subject:Quotation\n\n" + random.choice(quotes)

now = dt.datetime.now()

if now.weekday() == 6:
    with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
        connection.starttls()
        connection.login(user=secret.my_email, password=secret.password)
        connection.sendmail(
            from_addr=secret.my_email,
            to_addrs=secret.to_email,
            msg=message)
