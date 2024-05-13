from StudentManage import StudentManage
import json


class Parser:
    def __init__(self, raw_message, address):
        self.message = json.loads(raw_message)
        self.client_address = address
        self.act_list = {'show':StudentManage().show,
                         'query':StudentManage(self.message['parameters']).query,
                         'add':StudentManage(self.message['parameters']).add,
                         'modify':StudentManage(self.message['parameters']).modify,
                         'delete':StudentManage(self.message['parameters']).delete}

    def parse_raw_message(self):
        print(self.message)
        print(f"\tserver received: ('command':{self.message['command']}, 'parameters':{
              self.message['parameters']}) from {self.client_address}")
        return_value = self.act_list[self.message['command']]()
        return json.dumps(return_value)
