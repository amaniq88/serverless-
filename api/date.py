from email import message
from http.server import BaseHTTPRequestHandler
from datetime import datetime
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = "******  crrent Time is  ***** "
    self.wfile.write(message.encode())
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())



    return