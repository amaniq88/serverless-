from http.server import BaseHTTPRequestHandler
from datetime import datetime
from hijri_converter import Hijri, Gregorian



class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers() 
    ###############################


# Convert a Hijri date to Gregorian
    g = Hijri(1403, 2, 17).to_gregorian()

# Convert a Gregorian date to Hijri
    h = Gregorian(1982, 12, 2).to_hijri()
    self.wfile.write(g.encode())
    self.wfile.write(h.encode())




    return

