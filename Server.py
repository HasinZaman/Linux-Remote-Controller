from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import json
import socket
import importlib
import sys

baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\Linux-Remote-Controller"

sys.path.append('{0}\\pages'.format(baseDir))

pages = []

for (dirPath, dirNames, fileNames) in os.walk("pages"):
    pages = [file.split(".")[0] for file in fileNames]
    del pages[pages.index("Page")]
    break

for i1 in range(len(pages)):
    pages[i1] = importlib.import_module("{0}".format(pages[i1]))

class Server(BaseHTTPRequestHandler):
    def __makeButton(self, pageName):
        tmp = ""
        tmp += "<button onclick='window.location.href=\"{0}\";'>".format(pageName)
        tmp += pageName
        tmp += "</button>"
        return tmp

    def do_GET(self):
        requestedFile = None
        if self.path == '/' or self.path == '/index.html':
            self.path = '/index.html'
            requestedFile = open(self.path[1:],mode = "r").read().split("CONTENT")

            content = "".join([self.__makeButton(page.page.name) for page in pages])
            
            requestedFile = "{0}{1}{2}".format(requestedFile[0], content, requestedFile[1])

            requestedFile = bytes(requestedFile, 'utf-8')
            self.send_response(200)
        elif os.path.exists(self.path[1:]) and self.path.split(".")[-1] != "html":
            requestedFile = open(self.path[1:],mode = "rb").read()
                    
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
                
        elif os.path.exists("pages//{0}//{0}.html".format(self.path[1:])):
            print("pages//{0}//{0}.html".format(self.path[1:]))
            requestedFile = open("pages//{0}//{0}.html".format(self.path[1:]), mode = "rb").read()
            self.send_response(200)
        else:
             requestedFile = "File not found"
             self.send_response(404)    
        self.end_headers()
        self.wfile.write(requestedFile)

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

        cond = False
        i1 = 0
        while not cond and i1 < pages.length:
            pages[i1].page.action(data, self)
            i1+=1
        
        self.send_response(404)
            
        self.end_headers()

        response = None
        if cond == True:
            response = "1"
        elif cond == False:
            response = "0"

        self.wfile.write(response.encode())
        pass

host = None
if not os.path.exists("setting.txt"):
    #new settings
    with open("{0}\\setting.txt".format(baseDir),"w") as file:
        print("Insert server IP address:")
        host = input()
        file.write(host)
else:
    #loading settings
    print("Reading Settings")
    with open("{0}\\setting.txt".format(baseDir),"r") as file:
        host = file.read()
        print(host)

httpd = HTTPServer((host, 8080), Server)
httpd.serve_forever()
