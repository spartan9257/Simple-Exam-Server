from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path
import http.server
import socketserver
import logging
import cgi

#Create a user defined file for data output
#Validate the user input
valid_response = False
while(not valid_response):
    out_file = input("Enter user-data filename (include .txt): ")
    if out_file.find(".txt") > -1:
        break
    else:
        print("Invalid input! Must include .txt (fileName.txt)")
#If the file doesn't already exist, create it.
if path.exists(out_file) == False:
    file = open(out_file, "x")
    file.close()

#To connect to the server localhost:8080
#Or ip_address:8080
PORT = 8080

#Class that handles HTTP GET and POST requests
class ServerHandler(http.server.SimpleHTTPRequestHandler):

    #Sends the index.html file in response to HTTP GET
    def do_GET(self):
        logging.error(self.headers)
        http.server.SimpleHTTPRequestHandler.do_GET(self)
    
    #Accepts HTTP POST data, saves it to the user defined file
    def do_POST(self):
        logging.error(self.headers)
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        for item in form.list:
            print(item)
            logging.error(item)
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        
        #Looks for HTML POST values and saves them to the file
        #the "string" must match an elements name in the html file
        with open(out_file, "a+") as file:
            file.write(str(form.getvalue(str("firstname"))) + ",")
            file.write(str(form.getvalue(str("lastname"))) + ",")
            file.write(str(form.getvalue(str("email"))) + ",")
            file.write(str(form.getvalue(str("q1"))) + ",")
            file.write(str(form.getvalue(str("q2"))) + ",")
            file.write(str(form.getvalue(str("q3"))) + ",")
            file.write(str(form.getvalue(str("q4"))) + ",")
            file.write(str(form.getvalue(str("q5"))) + ",")
            file.write("\n")     
        file.close()

#initializes the server
Handler = ServerHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()