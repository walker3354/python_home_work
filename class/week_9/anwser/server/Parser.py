from Std_storage import Std_storage
import json


class Parser:
    def __init__(self, raw_message, address):
        self.message = json.loads(raw_message)
        self.client_address = address
        self.act_list = {'add': Std_storage(self.message['parameters']).add,
                        'show': Std_storage().show,'query':Std_storage()}

    def parse_raw_message(self):
        print(self.message)
        print(f"\tserver received: ('command':{self.message['command']}, 'parameters':{
              self.message['parameters']}) from {self.client_address}")
        return_value = self.act_list[self.message['command']]()
        return json.dumps(return_value)
