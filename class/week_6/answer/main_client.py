from AddStu import AddStu
from PrintAll import PrintAll
from Socket_client import Socket_client

host = "127.0.0.1"
port = 20001


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
        respone_data = self.socket.wait_response()
        print(f"The client received data => {respone_data}")
        history = respone_data["parameters"]
        PrintAll().execute(history)


if __name__ == '__main__':
    client = StdMenu()
    client.select_func()
