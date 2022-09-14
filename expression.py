import string
import uuid


class Expression:
    def __init__(self, op, n_1, n_2):
        self.__id: int = uuid.uuid4().int
        self.__op: string = op
        self.__n_1: float = n_1
        self.__n_2: float = n_2

    def solve_expression(self):
        if self.__op == "+":
            return self.__n_1 + self.__n_2
        if self.__op == "-":
            return self.__n_1 - self.__n_2
        if self.__op == "*":
            return self.__n_1 * self.__n_2
        if self.__op == "/":
            return self.__n_1 / self.__n_2

    def to_string(self):
        result = f"Expression Result: {self.__n_1} {self.__op} {self.__n_2} = {self.solve_expression()}\n"
        return result
