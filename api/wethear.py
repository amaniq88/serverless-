from http.server import BaseHTTPRequestHandler
import requests, json


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers() 
    ###############################
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "Amman"
    API_KEY = "d4d48bc4478ea6f2ed41d2d7135001cd"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
      # getting data in the json format
    data = response.json()
      # getting the main dict block
    main = data['main']
      # getting temperature
    temperature = main['temp']
      # getting the humidity
    humidity = main['humidity']
      # getting the pressure
    pressure = main['pressure']
      # weather report
    report = data['weather']
      # self.wfile.write(f"{CITY:-^30}".encode())
    message = "******  crrent Time is  ***** "
    self.wfile.write(message.encode())
      # print(f"Temperature: {temperature}")
      # print(f"Humidity: {humidity}")
      # print(f"Pressure: {pressure}")
      # print(f"Weather Report: {report[0]['description']}")
    # else:
    #   # showing the error message
    #   print("Error in the HTTP request")

    return

