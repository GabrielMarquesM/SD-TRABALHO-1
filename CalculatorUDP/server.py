import json
import socket

from expression import Expression


def initialize():
    i = 0
    while True:
        i += 1
        print(f"Waiting for expression... \n")

        data, address = s.recvfrom(1024)
        host, port = address

        exp_deserialized = json.loads(data.decode('utf-8'))
        exp = Expression(**exp_deserialized)

        print(f"Expression No {i} received!")
        print(f"Message ID: {exp.get_id()}")
        print(f"Address: {host} | Port: {port}")

        data = {"result": exp.to_string()}
        message = json.dumps(data)

        try:
            print("Sending Expression Result...")
            s.sendto(bytes(message, 'utf-8'), (host, port))
            print("Result sent succesfully")
        except:
            break
        print()


HOST = ''
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
initialize()
s.close()
