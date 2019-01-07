from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
# cgi = Common Gateway Interface, deciphers message sent from server
import cgi

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
            output = ""
            output += "<html><body>"
            output += "<h1>Hello!</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            # self.wfile.write(X) sends 'X' back to the requester 
            self.wfile.write(output)
            print message
            return
        
        if self.path.endswith("/hola"):
            self.send_response(200)
            # This tells what type of content is returned. In this case, HTML
            self.send_header('Content-type', 'text/html')
            #Sends blank line indicating end of headers
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Hola!</h1>"
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            # self.wfile.write(X) sends 'X' back to the requester 
            self.wfile.write(output)
            print message
            return
        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        try:
            self.send_response(303)
            self.end_headers()
            # cgi.parse_header parses html header
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            #then checks to see if it is form data being received
            if ctype == 'multipart/form-data':
                #fields then collects all fields in the form
                fields=cgi.parse_multipart(self.rfile, pdict)
                # messagecontent stores all fields in a vector
                messagecontent = fields.get('message')

            #what we will send back
            output = ""
            output += "<html><body>"
            output += "<h2> Okay, how about this: </h2>"
            output += "<h1> %s </h1>" % messagecontent[0]
            # adds post request and header type to prompt user to input data (first <>)
            # input field named message to coincide with message field extracted from messagecontent
            output += '''<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>'''
            output += "</body></html>"
            self.wfile.write(output)
            print output

        except:
            pass
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
