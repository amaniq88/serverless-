from http.server import BaseHTTPRequestHandler
from platform import platform
from unicodedata import name
from urllib import parse
from datetime import datetime , date 
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    s = self.path
    urlcomponent = parse.urlsplit(s)
    qslist = parse.parse_qsl(urlcomponent.query)
    dice = dict(qslist)
    name = dice.get("name")

    if name:
      message = f"the Query ID is {name}"
    else:
      message = "NO Query added to the URL .... parse not possible "
    message += f"\n Dear visitor  "
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())


    message1 = '''
    Welcome to the MY first application of the serverless function .... 
    will give some updated usefull infromation

                  ******  crrent Time is  *****   

    '''
    self.wfile.write(message1.encode())

    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
 



    return


