import os
import platform

host = input("Enter the host to ping: ")

param = "-n" if platform.system().lower() == "windows" else "-c"

command = f"ping {param} 4 {host}"
response = os.system(command)

if response == 0:
    print(f"Host {host} is reachable.")
else:
    print(f"Host {host} is not reachable.")
