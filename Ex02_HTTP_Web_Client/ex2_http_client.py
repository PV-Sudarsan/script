import socket

host = "example.com"
port = 80

# Create TCP socket and connect to web server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# Send HTTP GET request
request = "GET / HTTP/1.1\r\nHost: " + host + "\r\nConnection: close\r\n\r\n"
s.send(request.encode())

# Receive the full response
data = b""
while True:
    part = s.recv(1024)
    if not part:
        break
    data = data + part
s.close()

# Separate header and body, save body to file
header, body = data.split(b"\r\n\r\n", 1)
f = open("Download.html", "wb")
f.write(body)
f.close()

print(header.decode())
print("Successfully Downloaded.")
