from http.server import BaseHTTPRequestHandler
from platform import platform
from unicodedata import name
from urllib import parse
from datetime import datetime , date 
import requests, json

class handler(BaseHTTPRequestHandler):

	def do_GET(self):
		# Enter your API key here
		api_key = "d4d48bc4478ea6f2ed41d2d7135001cd"

		# base_url variable to store url
		base_url = "http://api.openweathermap.org/data/2.5/weather?"

		# Give city name
		city_name = "Amman"

		# complete_url variable to store
		# complete url address
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name

		# get method of requests module
		# return response object
		response = requests.get(complete_url)

		# json method of response object
		# convert json format data into
		# python format data
		x = response.json()

		# Now x contains list of nested dictionaries
		# Check the value of "cod" key is equal to
		# "404", means city is found otherwise,
		# city is not found
		if x["cod"] != "404":

			# store the value of "main"
			# key in variable y
			y = x["main"]

			# store the value corresponding
			# to the "temp" key of y
			current_temperature = y["temp"]

			# store the value corresponding
			# to the "pressure" key of y
			current_pressure = y["pressure"]

			# store the value corresponding
			# to the "humidity" key of y
			current_humidity = y["humidity"]

			# store the value of "weather"
			# key in variable z
			z = x["weather"]

			# store the value corresponding
			# to the "description" key at
			# the 0th index of z
			weather_description = z[0]["description"]
			self.send_response(200)
			self.send_header('Content-type', 'text/plain')
			self.end_headers()

			
			# print following values
			message = f" Temperature (in kelvin unit) = {str(current_temperature)} \n atmospheric pressure (in hPa unit) = {str(current_pressure)} \n humidity (in percentage) = {str(current_humidity)} \n description = {str(weather_description)}"
			self.wfile.write(message.encode())

		else:
			message = "City NOT found"
			self.wfile.write(message.encode())
		return

