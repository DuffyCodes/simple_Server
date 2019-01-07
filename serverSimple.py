from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

#determines which code to execute depending on http request received
class WebServerHandler(BaseHTTPRequestHandler):
    #do_GET handles all get requests
    def do_GET(self):
        # .path is inherited from self (HTTPBase)
        if self.path.endswith("/hello"):
            self.send_response(200)
            # This tells what type of content is returned. In this case, HTML
            self.send_header('Content-type', 'text/html')
            #Sends blank line indicating end of headers
            self.end_headers()
            message = ""
            message += "<html><body>Hello!</body></html>"
            # self.wfile.write(X) sends 'X' back to the requester 
            self.wfile.write(message)
            print message
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

# Instantiate server and specify which port it will listen on
def main():
    # Catch block follows
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Web Server running on port %s" % port
        # serve_forever() keeps server constantly listening un til Ctrl^C
        server.serve_forever()
    # Following stops web server
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()
        
# immediately runs main method when interpreter runs script
if __name__ == '__main__':
    main()
