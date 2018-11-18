import dns.resolver
import scapy.all as scapy
import netifaces as ni

ip = packet.getlayer(scapy.IP)
        udp = packet.getlayer(scapy.UDP)

        # Ignore packets containing data we aren't interested
        # in.
        if hasattr(packet, 'qd') and packet.qd is not None:
            queried_host = packet.qd.qname[:-1].decode("utf-8")
            if queried_host is None:
                print("queried_host is None, dropping request")
                return

            # If the queried_host is one of the domains we want
            # to spoof, return the spoof_ip.
            if queried_host in spoof_domains:
                print("!!!! Spoofing DNS request for %s by %s !!!!"
                        % (queried_host, ip.src))
                resolved_ip = spoof_ip
            # Else use dns.resolver to make a real DNS "A record"
            # request, and return the result of that.
            

            # Build the DNS answer
                dns_answer = scapy.DNSRR(
                    rrname=queried_host + ".",
                    ttl=330,
                    type="A",
                    rclass="IN",
                    rdata=resolved_ip)
                # Build the DNS response by constructing the IP
                # packet, the UDP "datagram" that goes inside the
                # packet, and finally the DNS response that goes
                # inside the datagram.
                dns_response = \
                    scapy.IP(src=ip.dst, dst=ip.src) / \
                    scapy.UDP(
                        sport=udp.dport,
                        dport=udp.sport
                    ) / \
                    scapy.DNS(
                        id = packet[scapy.DNS].id,
                        qr = 1,
                        aa = 0,
                        rcode = 0,
                        # qd = packet.qd,
                        qd = 8090,
                        an = dns_answer
                    )

                print("Resolved DNS request for %s to %s for %s" %
                    (queried_host, resolved_ip, ip.src))

            # Use scapy to send our response back to your phone.
                scapy.send(dns_response, iface=iface)