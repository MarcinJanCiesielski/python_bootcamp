import pandas as pd
from flight_search import FlightSearch
from flight_data import FlightData

DEPARTURES_SHEET_NAME = "Departures"
DESTINATIONS_SHEET_NAME = "Destinations"
USERS_SHEET_NAME = "Users"

IATA_CODE_COLUMN_NAME = "IATA Code"
PRICE_COLUMN_NAME = "Lowest Price"
CITY_COLUMN_NAME = "City"
FROM_CITY_COLUMN_NAME = "From City"
TO_CITY_COLUMN_NAME = "To City"
FROM_DATE_COLUMN_NAME = "From Date"
TO_DATE_COLUMN_NAME = "To Date"
STOPOVER_COLUMN_NAME = "Stopover Count"
VIA_CITY_COLUMN_NAME = "Via City"

FNAME_COLUMN_NAME = "First Name"
LNAME_COLUMN_NAME = "Last Name"
EMAIL_COLUMN_NAME = "e-mail"

class DataManager:
    #This class is responsible for talking to the Excel Sheet.
    def __init__(self, path: str) -> None:
        self.path = path
        self.departures = pd.read_excel(self.path, sheet_name=DEPARTURES_SHEET_NAME)
        self.destinations = pd.read_excel(self.path, sheet_name=DESTINATIONS_SHEET_NAME)
        self.users = pd.read_excel(self.path, sheet_name=USERS_SHEET_NAME)
        self.populate_iata_codes("departures")
        self.populate_iata_codes("destinations")

    def get_iata_codes(self, data: pd.DataFrame) -> list:
        return data[IATA_CODE_COLUMN_NAME].tolist()

    def get_departures_iata_codes(self) -> list:
        return self.get_iata_codes(self.departures)

    def get_destination_iata_price(self) -> list:
        destinations = self.get_iata_codes(self.destinations)
        destinations_dicts = []
        for destination_iata in destinations:
            dest_dict = self.destinations[self.destinations[IATA_CODE_COLUMN_NAME] == destination_iata].to_dict(orient="records")[0]
            destinations_dicts.append(dest_dict)
        return destinations_dicts

    def populate_iata_codes(self, data_name: str) -> None:
        fs = FlightSearch()
        if data_name == "departures":
            data = self.departures
        elif data_name == "destinations":
            data = self.destinations

        city_to_update = data[data[IATA_CODE_COLUMN_NAME].isnull()]
        for index, row in city_to_update.iterrows() :
            iata_code = fs.get_iata_code(row[CITY_COLUMN_NAME])
            data.loc[index, [IATA_CODE_COLUMN_NAME]] = iata_code
        self.write_data_to_excel()

    def get_users(self) -> list:
        users = []
        for index, row in self.users.iterrows():
            users.append(row.to_dict())
        return users

    def update_flight_price(self, iata_code: str, flight: FlightData) -> None:
        airport_row = self.destinations[self.destinations[IATA_CODE_COLUMN_NAME] == iata_code.upper()]
        index = airport_row.index.values[0]
        self.destinations.loc[index, [PRICE_COLUMN_NAME]] = flight.price
        self.destinations.loc[index, [FROM_CITY_COLUMN_NAME]] = f"{flight.origin_city}-{flight.origin_airport}"
        self.destinations.loc[index, [TO_CITY_COLUMN_NAME]] = f"{flight.destination_city}-{flight.destination_airport}"
        self.destinations.loc[index, [FROM_DATE_COLUMN_NAME]] = flight.out_date
        self.destinations.loc[index, [TO_DATE_COLUMN_NAME]] = flight.return_date
        self.destinations.loc[index, [STOPOVER_COLUMN_NAME]] = flight.stop_overs
        self.destinations.loc[index, [VIA_CITY_COLUMN_NAME]] = flight.via_city

        self.write_data_to_excel()

    def add_new_user(self, fname: str, lname: str, email: str) -> None:
        new_user_dict = {
            FNAME_COLUMN_NAME: [fname],
            LNAME_COLUMN_NAME: [lname],
            EMAIL_COLUMN_NAME: [email],
        }
        new_user_df = pd.DataFrame.from_dict(new_user_dict)
        self.users = pd.concat([self.users, new_user_df], ignore_index=True)
        self.write_data_to_excel()

    def write_data_to_excel(self) -> None:
        with pd.ExcelWriter(path=self.path, mode="w") as excel_writer:
            self.destinations.to_excel(excel_writer, index=False, sheet_name=DESTINATIONS_SHEET_NAME)
            self.departures.to_excel(excel_writer, index=False, sheet_name=DEPARTURES_SHEET_NAME)
            self.users.to_excel(excel_writer, index=False, sheet_name=USERS_SHEET_NAME)
