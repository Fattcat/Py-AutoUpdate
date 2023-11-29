import os
from import sleep
import socket

userName = socket.gethostname()

for i in range(20):
  print(f"Hellooo", userName)
