from scapy.all import *

RESP  = "HTTP/1.1 200 OK\r\n"
RESP += "Server: exampleServer\r\n"
RESP += "Content-Length: 6\r\n"
RESP += "\r\n"
RESP += "A body"

IP(src="10.10.1.207", dst="10.10.1.60")/TCP(sport=80, dport=3389, flags="A")/RESP