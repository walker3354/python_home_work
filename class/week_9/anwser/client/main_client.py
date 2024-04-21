from AddStu import AddStu
from PrintAll import PrintAll
from ModifyStu import ModifyStu
from DelStu import DelStu


class StdMenu:
    def __init__(self):
        self.action_list = {
            "add": AddStu().execute,
            "show": PrintAll().execute,
            "modify": ModifyStu().execute,
            "del": DelStu().execute,
        }

    def print_menu(self):
        print()
        print("add: Add a student's name and score")
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
                self.action_list[select_result]()
            except Exception as e:
                print(f"{e} please try again!")


if __name__ == "__main__":
    client = StdMenu()
    client.select_func()
