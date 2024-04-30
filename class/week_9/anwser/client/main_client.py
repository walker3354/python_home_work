from AddStu import AddStu
from PrintAll import PrintAll
from ModifyStu import ModifyStu
from DelStu import DelStu
from Socket_client import Socket_client


class StdMenu:
    def __init__(self):
        self.socket = Socket_client()
        self.action_list = {
            "add": AddStu,
            "show": PrintAll,
            "modify": ModifyStu,
            "del": DelStu,
        }

    def print_menu(self):
        print("\nadd: Add a student's name and score")
        print("del: Delete a student")
        print("modify: Modify a student's score")
        print("show: Print all")
        print("exit: Exit")
        selection = input("Please select: ")
        return selection

    def select_func(self):
        select_result = "initial"
        while select_result != "exit":
            select_result = self.print_menu()
            try:
                self.action_list[select_result](self.socket).execute()
            except Exception as e:
                print(f"{e} please try again!")


if __name__ == "__main__":
    client = StdMenu()
    client.select_func()
