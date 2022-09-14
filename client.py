import json
import socket


def get_exp_input():
    operators = ["+", "-", "*", "/"]
    valid_input = False

    while (not valid_input):
        valid_input = True
        user_input = input(
            "Insert an expression in the following format (Number OPERATOR Number): ")
        try:
            data_args = user_input.split()
            # Falta checar se o operador é valido
            op = data_args[1]
            n_1 = float(data_args[0])
            n_2 = float(data_args[2])

            if len(data_args) != 3:
                valid_input = False
                print("Input Error: Wrong number of arguments passed")
                print(
                    f"Expression expected 3 arguments but received {len(data_args)} instead\n")
            if op not in operators:
                valid_input = False
                print("Input Error: Invalid operator")
                print(f"Valid Operators: {operators}\n")

        except:
            valid_input = False
            print("Input Error: Wrong Expression Format")
    return op, n_1, n_2


HOST = "localhost"
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.settimeout(10)  # tempo que o cliente espera uma resposta do servidor

while True:
    op, n_1, n_2 = get_exp_input()

    data = {
        "op": op,
        "n_1": n_1,
        "n_2": n_2
    }

    message = json.dumps(data)

    try:
        s.sendto(bytes(message, 'utf-8'), (HOST, PORT))
        data, address = s.recvfrom(1024)
        print("Waiting for the expression's result...")
        print(data.decode("utf-8")
              )

    except:
        print("Time for response for the expression exceeded")
