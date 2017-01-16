IP_ADDRESS = input('IP Address: ') 


for octet in IP_ADDRESS.split('.'):
    print(bin(int(octet)) + ' ')

