import socket 
import subprocess

ip = input("Enter IP: ")
port = int(input("Enter port: "))

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#creates a ipv4 socket
    s.connect((ip, port))#connects to the ip and port
    cmdlet = input("$")
    while cmdlet!= "exit":
        s.send(cmdlet.encode("utf-8")) #sends the cmdlet to the server
        results = s.recv(1024).decode("utf-8")#receives the results from the server
        print(results)
        cmdlet = input("$")#resets the cmdlet


    s.close()
except:
    print("Connection failed")
