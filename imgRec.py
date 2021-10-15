import random
import socket, select
from time import gmtime, strftime
from random import randint

imgcounter = 1
basename = "opencv_frame_0%s.png"

HOST = '192.168.1.12'
PORT = 8888

connected_clients_sockets = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

connected_clients_sockets.append(sock)

while True:

    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])

    for sock in read_sockets:

        if sock == sock:

            sockfd, client_address = sock.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:

                data = sock.recv(4096)
                txt = str(data)

                if txt.startswith('SIZE'):
                    tmp = txt.split()
                    size = int(tmp[1])

                    print('got size')

                    sock.send("GOT SIZE")

                elif txt.startswith('BYE'):
                    sock.shutdown()

                elif data:

                    myfile = open(basename % imgcounter, 'wb')

                    data = sock.recv(40960000)
                    if not data:
                        myfile.close()
                        break
                    myfile.write(data)
                    myfile.close()

                    sock.send("GOT IMAGE")
                    sock.shutdown()
            except:
                sock.close()
                connected_clients_sockets.remove(sock)
                continue
        imgcounter += 1
sock.close()