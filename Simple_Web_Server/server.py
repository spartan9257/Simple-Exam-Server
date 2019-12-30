from http.server import HTTPServer, BaseHTTPRequestHandler
from os import path
import cgi, csv, logging, socketserver, http.server

#Create a user defined file for data output
#Validate the user input
valid_response = False
while(not valid_response):
    out_file = input("Enter user data filename: ")
    if out_file.find(".") > -1:
        print("Invalid input! Must exclude file extention from name.")
    else:
        break
out_file = out_file + ".csv"
#If the file doesn't already exist, create it.
if path.exists("Exam Results\\" + out_file) == False:
    file = open("Exam Results\\" + out_file, "x")
    file.close()

#for simplicity Im updating the output file name with its foler
out_file = "Exam Results\\" + out_file




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
        
        #Looks for HTML POST values and saves them to the CSV file,
        #the "string" must match an elements name in the html file
        fields = []
        fields.append(str(form.getvalue(str("firstname"))))
        fields.append(str(form.getvalue(str("lastname"))))
        fields.append(str(form.getvalue(str("email"))))
        fields.append(str(form.getvalue(str("q1"))))
        fields.append(str(form.getvalue(str("q2"))))
        fields.append(str(form.getvalue(str("q3"))))
        fields.append(str(form.getvalue(str("q4"))))
        fields.append(str(form.getvalue(str("q5"))))
        #Save all the fields to the output file
        with open(out_file, "a+", newline="") as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)

#initializes the server
Handler = ServerHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()