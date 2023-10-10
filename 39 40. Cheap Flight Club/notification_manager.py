import smtplib
import secret
from flight_data import FlightData

MAIL_PROVIDER_SMTP_ADDRESS = "smtp-mail.outlook.com"
MY_EMAIL = secret.my_email
MY_PASSWORD = secret.password

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def prepare_message(self, flight: FlightData) -> str:
        msg = f"Low price alert! Only {flight.price}zł to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            msg += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
        return msg

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
