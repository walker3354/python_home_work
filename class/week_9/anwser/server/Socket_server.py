from threading import Thread
import socket
from Parser import Parser


class SocketServer(Thread):
    def __init__(self, host, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)

    def serve(self):
        self.start()

    def run(self):
        while True:
            connection, address = self.server_socket.accept()
            print("{} connected".format(address))
            self.new_connection(connection=connection, address=address)

    def new_connection(self, connection, address):
        Thread(
            target=self.receive_message_from_client,
            kwargs={"connection": connection, "address": address},
            daemon=True,
        ).start()

    def receive_message_from_client(self, connection, address):
        keep_going = True
        try:
            while keep_going:
                try:
                    message = connection.recv(1024).strip().decode()
                except Exception as e:
                    print("Exeption happened {}, {}".format(e, address))
                    keep_going = False
                else:
                    if not message:
                        keep_going = False
                    return_value = Parser(message, address).parse_raw_message()
                    connection.send(return_value.encode())
        except:
            pass
        connection.close()
        print("{} close connection".format(address))
