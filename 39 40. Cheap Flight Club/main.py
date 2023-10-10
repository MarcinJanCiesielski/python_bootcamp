#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import datetime as dt
import data_manager as dm
from flight_search import FlightSearch
import notification_manager as nm

data_manager = dm.DataManager("./my_flights.xlsx")
flight_search = FlightSearch()
notification_manager = nm.NotificationManager()

departures_iata_codes = data_manager.get_departures_iata_codes()
destinations = data_manager.get_destination_iata_price()

today = dt.date.today()
ninety_days = dt.timedelta(days=(6*30))
six_month_from_today = today + ninety_days

for departure_iata in departures_iata_codes:
    for destination in destinations:
        flight = flight_search.check_flights(
            departure_iata,
            destination[dm.IATA_CODE_COLUMN_NAME],
            from_time=today,
            to_time=six_month_from_today
        )

        if flight is None:
            continue

        if flight.price < destination[dm.PRICE_COLUMN_NAME]:
            users = data_manager.get_users()
            emails = [row[dm.EMAIL_COLUMN_NAME] for row in users]
            message = notification_manager.prepare_message(flight)

            data_manager.update_flight_price(destination[dm.IATA_CODE_COLUMN_NAME], flight)

            notification_manager.send_emails(emails, message)
