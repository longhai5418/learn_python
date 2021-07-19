#!/usr/bin/python
# -*- coding: UTF-8 -*-
import http.server
import socketserver


class MyBaseRequestHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print("GET:",self.address_string(),
                          self.log_date_time_string(),
                          args)

PORT = 8081

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), MyBaseRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
