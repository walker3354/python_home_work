from Socket_client import Socket_client


class DelStu:

    def __init__(self):
        self.socket = Socket_client()
        self.student_name = ""

    def check_student_name(self):
        self.socket.send_command("query", {"name": self.student_name})
        if self.socket.wait_response()["status"] == "OK":
            self.confirm_del()
        else:
            print("student no find")

    def input_student_name(self):
        self.student_name = input("Please input a student's name: ")
        self.check_student_name()

    def confirm_del(self):
        if input("Confirm to delete (y/n): ").lower() == "y":
            self.socket.send_command("delete", {"name": self.student_name})
            if self.socket.wait_response()["status"] == "OK":
                print("Delete success")
            else:
                print("Delete fail")
        else:
            print("Leaving del system....")
