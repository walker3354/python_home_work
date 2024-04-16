import socket
import json
BUFFER_SIZE = 1940


class Socket_client:

    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        print(f"The client sent data => ('command': '{
              command}'), ('parameters': {parameters})")
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        return json.loads(raw_data)
