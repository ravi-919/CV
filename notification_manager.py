import requests
from twilio.rest import Client
from flight_data import FlightData
import smtplib
from flight_data import FlightData

MY_EMAIL = 'jairavi306@gmail.com'
MY_PASSWORD = 'Remos@18'

TWILIO_ACCOUNT_SID = "ACcbccbbf3c893054ea303abf2f90d53eb"
AUTH_TOKEN = "9928765e5652200f660125c33d6a8dfd"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_ACCOUNT_SID, AUTH_TOKEN)

    # def send_sms(self, message):
    #     message = self.client.messages.create(body=message,
    #                                      from_="+17198515630",
    #                                      to="+917744887221")

    def send_emails(self, flight: FlightData, destination):
        flight = flight
        pound = '₤'
        if flight.price < destination["lowestPrice"]:
            message = f"Subject:New Low Price Flight!\n\nLow Price alert! Only {pound} {flight.price} "\
                  f"to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}" \
                  f"-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
                 f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                                    msg=f"{message}\n{link}".encode('utf-8'))
