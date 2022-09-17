import socket
import threading

HOST = "localhost"
PORT = 6789

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.close()
