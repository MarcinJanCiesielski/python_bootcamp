import smtplib
import secret

with smtplib.SMTP("smtp-mail.outlook.com", port=587) as connection:
    connection.starttls()
    connection.login(user=secret.my_email, password=secret.password)
    connection.sendmail(
        from_addr=secret.my_email,
        to_addrs=secret.to_email,
        msg="Subject:Hello\n\nThis is the body os my email."
        )
