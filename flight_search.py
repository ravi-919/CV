import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "Gf2OrNVwB7nhjPoX_tBQGI53Lm5lmVJ9"
LOCATION_ENDPOINT = f"{TEQUILA_ENDPOINT}/locations/query"
SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"


class FlightSearch:

    def get_destination_code(self, city_name):
        self.city_name = city_name

        params = {
            "term": self.city_name,
            "location_types": "city"
        }

        header = {
            "apikey": TEQUILA_API_KEY,
        }

        response = requests.get(url=LOCATION_ENDPOINT, params=params, headers=header)
        print(response)

        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        city_code = response.json()['locations'][0]['code']
        return city_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time, destination_city):
        header = {
            "apikey": TEQUILA_API_KEY
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }

        response = requests.get(url=SEARCH_ENDPOINT, params=query, headers=header)

        try:
            data = response.json()['data'][0]
            print(f"{destination_city_code}: £{data['price']}")
        except IndexError:
            query['max_stopovers'] = 1
            response = requests.get(url=SEARCH_ENDPOINT, params=query, headers=header)
            try:
                data = response.json()['data'][0]
                print(f"{destination_city_code}: £{data['price']}")
            except IndexError:
                print(f"Sorry, No flights found for {destination_city}")
                return None
            else:
                flight_data = FlightData(price=data['price'],
                                         origin_city=data["route"][0]["cityFrom"],
                                         origin_airport=data["route"][0]["flyFrom"],
                                         destination_city=data["route"][0]["cityTo"],
                                         destination_airport=data["route"][0]["flyTo"],
                                         out_date=data["route"][0]["local_departure"].split("T")[0],
                                         return_date=data["route"][1]["local_departure"].split("T")[0],
                                         stop_overs=1,
                                         via_city=data["route"][0]["cityTo"])

                return flight_data
        else:
            flight_data = FlightData(price=data['price'], origin_city=data["route"][0]["cityFrom"], origin_airport=
            data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])
            return flight_data