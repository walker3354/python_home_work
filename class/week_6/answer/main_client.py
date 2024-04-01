from AddStu import AddStu
from PrintAll import PrintAll
import socket
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class StdMenu:
    def __init__(self):
        self.action_list = {"add": self.add_student, "show": self.show_student}
        self.socket = Socket_client(host, port)

    def print_menu(self):
        print()
        print("add: Add a student's name and score")
        print("show: Print all")
        print("exit: Exit")
        selection = input("Please select: ")
        return selection

    def select_func(self):
        select_result = "initial"
        while select_result != "exit":
            select_result = self.print_menu()
            try:
                self.action_list[select_result]()
            except Exception as e:
                print(f'{e} please try again!')

    def add_student(self):
        parameters = AddStu().execute()
        self.socket.send_command('add', parameters)
        respone_data = self.socket.wait_response()
        print(f"The client received data => {respone_data}")
        if respone_data['status'] == 'OK':
            print(f"Add {parameters} success")
        else:
            print(f"Add {parameters} fail")

    def show_student(self):
        self.socket.send_command('show', {})
        history = self.socket.wait_response()["parameters"]
        PrintAll().execute(history)


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


if __name__ == '__main__':
    client = StdMenu()
    client.select_func()
