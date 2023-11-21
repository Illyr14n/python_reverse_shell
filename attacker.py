import socket 
import subprocess

ip = input("Enter IP: ")
port = int(input("Enter port: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates a ipv4 socket
    s.connect((ip, port))#connects to the ip and port
    cmdlet = input("$")
    while True:
        cmdlet = input("$ ")
        if cmdlet.lower() == "exit":
            break

        s.send(cmdlet.encode("utf-8"))
        results = s.recv(1024).decode("utf-8")
        print(results)

    s.close()
except Exception as e:
    print("Connection failed:", str(e))
