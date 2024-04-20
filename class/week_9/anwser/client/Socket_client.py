import socket
import json
BUFFER_SIZE = 1940

host = "127.0.0.1"
port = 20001


class Socket_client:

    def __init__(self, host=host, port=port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        print(f"The client sent data => ('command': '{
              command}'), ('parameters': {parameters})")
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = json.loads(data.decode())
        print(f"The client received data => {raw_data}")
        return raw_data
