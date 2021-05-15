import tkinter as tk
import socket
import threading

# socket===inicio=======================

#   Definição da host
host = 'localhost'
port = 8080

#   Criação do socket TCP/IP
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host, port))