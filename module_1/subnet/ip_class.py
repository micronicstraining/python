# Given an IP address print out IP address class
# See table with first octet, class, example ip table
# https://www.techopedia.com/6/28587/internet/8-steps-to-understanding-ip-subnetting/4

ip_address = '192.168.4.3'

# Unpack ip address by octets
first, sec, third, fouth = ip_address.split('.')

# Convert first to an integer
first_octet = int(first)

# Add if statements which print IP address class based on first octet
# Hint: Can you use the following comparison logic:
#      lower <= first_octet <= upper
