from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = '''
    Welcome to the MY first application of the serverless function .... 
    will give some updated usefull infromation

                  ******  crrent Time is  *****   
                    
    '''
    self.wfile.write(message.encode())

    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())



    return