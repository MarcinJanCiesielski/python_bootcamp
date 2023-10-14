import smtplib
import secret

MAIL_PROVIDER_SMTP_ADDRESS = "smtp-mail.outlook.com"
MY_EMAIL = secret.my_email
MY_PASSWORD = secret.password

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def prepare_message(self, product_name: str, price: float) -> str:
        msg = f"Subject:New Low Price product\n\n!Low price alert! Only {price}zł for product {product_name}."

        return msg

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=message.encode('utf-8')
                )
