import socket
import threading
from sys import argv
import select

FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ENTER = '\n'
SERVERPORT = 8080
servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.bind((argv[2], int(argv[1])))
def client_to_serv(conn):
    # msg_length = conn.recv(2048).decode(FORMAT)
    # if msg_length:
    #     msg_length = int(msg_length)
    #     msg = conn.recv(msg_length).decode(FORMAT)
    #     if msg[-2:] == ENTER:
    #         connected = False
        
    #     print(f"[{addr}] {msg}")
    #     conn.send("Msg received".encode(FORMAT))
    request = (conn.recv(4096).decode().split('\n')[0]+'\n').encode()
    if request is None:
        return None
    print(request)
    return request
def communicate(conn, sockserv):
    inputs = [conn, sockserv]
    buff_size = 4096
    i = True
    while True and i:
        readable, writable, errs=select.select(inputs, [], inputs)
        if errs:
            break
        for soc in readable:
            data = soc.recv(buff_size)
            if data:
                if soc is conn:
                    sockserv.send(data)
                if soc is sockserv:
                    conn.send(data)
            else:
                i=False
                break
    conn.close()
    sockserv.close()
    
# Running for each client
def handle_client(conn, addr, sockserv):
    print(f"[NEW CONNECTION] {addr} connected.")
    request = client_to_serv(conn)
    if request:
        sockserv.connect((argv[3], SERVERPORT))
        sockserv.send(request)
        communicate(conn, sockserv)
        sockserv.close()
def start():
    servsock.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        try:
            sockserv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sockserv.bind((argv[2],0))
            conn, addr = servsock.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr, sockserv))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
        except Exception as e:
            print(e)
print("[STARTING] server is starting...")
start()