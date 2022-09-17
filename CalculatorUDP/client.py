import json
import socket
from uuid import uuid4


def get_exp_input():
    operators = ["+", "-", "*", "/"]
    valid_input = False

    while (not valid_input):
        user_input = input(
            "Insert an expression in the following format (Number OPERATOR Number): ")
        try:
            data_args = user_input.split()
            op = data_args[1]
            n_1 = float(data_args[0])
            n_2 = float(data_args[2])

            if len(data_args) != 3:
                print("Input Error: Wrong number of arguments passed")
                print(
                    f"Expression expected 3 arguments but received {len(data_args)} instead\n")
                continue

            if op not in operators:
                print("Input Error: Invalid operator")
                print(f"Valid Operators: {operators}\n")
                continue

            valid_input = True
        except:
            valid_input = False
            if (user_input == "q"):
                return [], True
            print("Input Error: Wrong Expression Format")

    return [op, n_1, n_2], False


def initialize():
    while True:
        exp, leave = get_exp_input()
        if leave:
            break
        data = {
            "id": uuid4().int,
            "op": exp[0],
            "n_1": exp[1],
            "n_2": exp[2]
        }

        message = json.dumps(data)

        try:
            s.sendto(bytes(message, 'utf-8'), (HOST, PORT))
            data, address = s.recvfrom(1024)
            print("Waiting for the expression's result...")
            exp_solution = data.decode("utf-8")

        except:
            print("Time for response for the expression exceeded")
            break

        solution_deserialized = json.loads(exp_solution)
        print(solution_deserialized["result"])


HOST = "localhost"
PORT = 6789
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(20.0)  # tempo que o cliente espera uma resposta do servidor
initialize()
s.close()
print("Closing application...")
