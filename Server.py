from http.server import HTTPServer, BaseHTTPRequestHandler
from os.path import exists
import os
import json
import socket
import importlib
import sys

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        file_to_open = None
        try:
            if exists(self.path[1:]):
                file_to_open = open(self.path[1:],mode = "rb").read()
                
                self.send_response(200)
                
                if self.path[-3:] == "svg":
                    self.send_header('Content-type', 'image/svg+xml')
                    
                elif self.path[-3:] == "gif":
                    self.send_header('Content-type', 'image/gif')
                    
                elif self.path[-4:] == "jpeg" or self.path[-3:] == "jpg":
                    self.send_header('Content-type', 'image/jpeg')
                    
                elif self.path[-3:] == "png":
                    self.send_header('Content-type', 'image/png')
                    
                elif self.path[-4:] == "html":
                    self.send_header('Content-type', 'text/html')
                    
                elif self.path[-3:] == "css" or self.path[-7:-4] == "css" :
                    self.send_header('Content-type', 'text/css')
            else:
                file_to_open = "File not found"
                self.send_response(404)

            
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(file_to_open)


    def dataPrepare(self,dataRaw):
        content_length = int(dataRaw.headers['Content-Length'])
        
        data = dataRaw.rfile.read(content_length).decode("utf-8").split("&")

        dataReturn = {}
        for i in range(len(data)):
            temp = data[i].split("=")
            dataReturn[temp[0]]=temp[1]

        return dataReturn

    def action(self):
        pass
            
    def do_POST(self):
        

        data = self.dataPrepare(self)

        #response = False

        print(data["action"])
        
        self.send_response(404)
            
        self.end_headers()

        if response == True:
            response = "1"
        elif response == False:
            response = "0"

        self.wfile.write(response.encode())
        pass

host = None
if not exists("setting.txt"):
    #new settings
    with open("setting.txt","w") as file:
        print("Insert server IP address:")
        host = input()
        file.write(host)
else:
    #loading settings
    print("Reading Settings")
    with open("setting.txt","r") as file:
        host = file.read()
        print(host)

httpd = HTTPServer((host, 8080), Server)
httpd.serve_forever()
