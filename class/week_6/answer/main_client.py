from AddStu import AddStu
from PrintAll import PrintAll
from StudentInfoProcessor import StudentInfoProcessor
import socket
import json

host = "127.0.0.1"
port = 20001
BUFFER_SIZE = 1940


class Socket_client:

    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))
        self.student_dict = StudentInfoProcessor().read_student_file()
        self.action_list = {"add": AddStu, "show": PrintAll}

    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        print(f"The client sent data => ('command': '{
              command}'), ('parameters': {parameters})")
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print(raw_data)
        if raw_data == 'closing':
            return False
        return True

    def select_func(self):
        select_result = "initial"
        while select_result != "exit":
            select_result = self.print_menu()
            try:
                self.student_dict, parameters = self.action_list[select_result](
                    self.student_dict).execute()
                self.send_command(select_result, parameters)
            except Exception as e:
                print(e)
        StudentInfoProcessor().restore_student_file(self.student_dict)

    def print_menu(self):
        print()
        print("add: Add a student's name and score")
        print("show: Print all")
        print("exit: Exit")
        selection = input("Please select: ")
        return selection


if __name__ == '__main__':
    client = Socket_client(host, port)

    keep_going = True
    while keep_going:
        client.select_func()
        keep_going = client.wait_response()
