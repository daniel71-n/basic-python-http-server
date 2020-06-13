#!/usr/bin/python

import http.server
import socketserver
import os
import os.path

if os.path.exists('files/'): #check if there's a /files/ subdirectory in the cwd. That's the directory that's listed for clients and where files get uploaded
    pass
else:
   try:
       os.mkdir('files/')  #if files/ doesn't exist, create it.
   except:
        print("Failed to create 'files' subdirectory")


PORT = 54321
    
myhandler = http.server.CGIHTTPRequestHandler


                       


server = http.server.HTTPServer(("", PORT), myhandler)


while True:
    print('serving on port', PORT)
    server.serve_forever()

server.shutdown()




