ip_address = '192.168.4.3'

first_octet, *_ = ip_address.split('.')
first_octet = int(first_octet)

if 0 <= first_octet <= 126:
    print('Class A')
elif 128 <= first_octet <= 191:
    print('Class B')
elif 192 <= first_octet <= 223:
    print('Class C')
elif 224 <= first_octet <= 239:
    print('Class D')
elif 240 <= first_octet <= 255:
    print('Class E')
else:
    print('Invalid first octet')

