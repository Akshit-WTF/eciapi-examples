from http.server import BaseHTTPRequestHandler, HTTPServer
import json


hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = json.loads(body)

        if (body["error"] == "true"):
            print("There was an error!")
            # Your own error handling code!
        else:
            print(body["jobId"])
            print(body["data"])
            # Your own code!

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        return


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
