from PyQt6 import QtCore
from PyQt6.QtCore import pyqtSignal


class Execute(QtCore.QThread):
    return_sig = pyqtSignal(dict)

    def __init__(self, command, client_socket, parameters):
        super().__init__()
        self.command = command
        self.client_socket = client_socket
        self.parameters = parameters

    def run(self):
        self.client_socket.send_command(self.command, self.parameters)
        response = self.client_socket.wait_response()
        print(response)
        self.return_sig.emit(response)
