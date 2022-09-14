import json
import socket

validInput = False

while (validInput == False):
    validInput = True
    user_input = input(
        "Insert an expression in the following format (Number OPERATOR Number): ")
    try:
        data_args = user_input.split()
        # Falta checar se o operador é valido
        op = data_args[1]
        n_1 = int(data_args[0])
        n_2 = int(data_args[2])
    except:
        validInput = False
        print("Wrong Expression Format")

data = {
    "op": op,
    "n_1": n_1,
    "n_2": n_2
}

message = json.dumps(data)

HOST = "localhost"
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(10)  # tempo que o cliente espera uma resposta do servidor

try:
    s.sendto(bytes(message, 'utf-8'), (HOST, PORT))
    data, address = s.recvfrom(1024)
    print("Waiting for the expression's result...")
    print(data.decode("utf-8")
          )

except:
    print("Time for response for the expression exceeded")
