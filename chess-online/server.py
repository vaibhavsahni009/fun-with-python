import socket
from _thread import *
import sys

# private ip of server machine and port to run on network
server = "192.168.1.2"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print('Waiting for connection , server started')


def threaded_client(conn):
    conn.send(str.encode("connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved: ", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))

        except:
            break

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("connected to ", addr)

    start_new_thread(threaded_client, (conn,))
