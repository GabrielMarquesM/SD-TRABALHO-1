import json
import socket

import expression as exp

i = 0
HOST = ''
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

while True:
    i += 1
    print(f"Waiting for expression... \n")
    data, address = s.recvfrom(1024)

    host, port = address

    exp_deserialized = json.loads(data.decode('utf-8'))
    e = exp.Expression(**exp_deserialized)

    print(f"Expression No {i} received!")
    print(f"Address: {host} | Port: {port}")
    try:
        print("Sending Expression Result...")
        s.sendto(bytes(e.to_string(), 'utf-8'), (host, port))
        print("Result sent succesfully")
    except:
        print(f"Timeout for sending Result of Expression No {i}")
    print()
