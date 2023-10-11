from http.server import BaseHTTPRequestHandler, HTTPServer
import hashlib
import copy
import re
class MyRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        modified_request = copy.copy(self)
        modified_request.headers = copy.copy(self.headers)
        
        # Remove Cookie header from the copy
        if 'Cookie' in modified_request.headers:
            del modified_request.headers['Cookie']
        temp = str(modified_request.headers)
        # Calculate SHA-256 hash of modified request
        request_hash = hashlib.sha256(temp.encode()).hexdigest()
        print("Calculated Hash", request_hash)
        # Check for Cookie header
        print(self.headers)
        if 'Cookie' in self.headers:
            cookies = self.headers['Cookie'].split('; ')
            #print(cookies)
            # Check for _gid value
            for cookie in cookies:
                #print(cookie)
                name, value = cookie.split('=')
                if name == '_gat' and value == '27':
                    print("Covert request")
                    # Look for PHPSESSID value   
                    for cookie in cookies:
                        name, value = cookie.split('=')
                        if name == 'PHPSESSID':
                            print("Request Hash", value)
                            # Check if hash matches PHPSESSID value
                            if value == request_hash:
                                print("HASH Matched")
                                if 'User-Agent' in self.headers:
                                    cmess = self.headers['User-Agent']
                                    pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
                                    match = re.search(pattern, cmess)
                                    if match:
                                        cmess = match.group()
                                        components = cmess.split('.')
                                        ascii_characters = [chr(int(component)) for component in components]
                                        result = ''.join(ascii_characters)
                                        print("Covert Message = ", result)
                                    return
                else:
                    print("Not a Covert Request")          
        print("HASH Not Matched")
        
def run():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print('Starting server...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
