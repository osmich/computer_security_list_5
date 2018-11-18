from scapy.all import *
from socket import AF_INET, SOCK_DGRAM, socket
from traceback import print_exc

# ans, unans = traceroute("4.2.2.1",l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="thesprawl.org")))

# sniff(iface="ath0",prn=lambda x:x.sprintf("{Dot11Beacon:%Dot11.addr3%\t%Dot11Beacon.info%\t%PrismHeader.channel%\t%Dot11Beacon.cap%}"))

answer = sr1(IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1,qd=DNSQR(qname='www.thepacketgeek.com')), verbose=0)
print(answer[DNS].summary())
# print(answer[DNS])
# sock = socket(AF_INET, SOCK_DGRAM)
# sock.bind(('0.0.0.0', 1053))
# request, addr = sock.recvfrom(4096)
# print(DNS(request))

# response = DNS(
#             id=dns.id, ancount=1, qr=1,
#             an=DNSRR(rrname=str(query), type='A', rdata=str(head), ttl=1234))
#         print(repr(response))
        # sock.sendto(bytes(response), addr)
response = DNS(
            id=12, ancount=1, qr=1,
            an=DNSRR(rrname=str("test.1.2.3.4.example.com"), type='A', rdata=str("head"), ttl=1234))
        print(repr(response))
