import sys

# Read the first 2 bytes from the DNS request that netcat
# is piping in on stdin. These byte are the request ID and
# must be included at the start of the response so that the
# requester can match the response up with its original request
# req_id = sys.stdin.read(2)
req_id = 12#b'110011'
# Convert the bytes to hex
req_id_hex_str = ''.join(["%02X" % ord(c) for c in str(req_id)])
# This is hex for the DNS response body "robertheaton.com
# is at IP address 104.18.32.191". To give yourself some
# confidence that I'm telling the truth, run:
#
# python -c "print bytearray.fromhex('$COPY_THE_HEX_STRING_HERE')"
#
# in a terminal.
resp_body_str = "818000010002000000000c726f62657274686561746f6e03636f6d0000010001c00c000100010000012b0004681220bfc00c000100010000012b0004681221bf"

# Construct a DNS response, convert it to bytes, and write
# it to stdout so that netcat's --exec option sends it back
# to your smartphone
full_resp_body_bytes = bytearray.fromhex(req_id_hex_str + resp_body_str)
# sys.stdout.write(full_resp_body_bytes)
print(bytearray.fromhex(str(full_resp_body_bytes)))