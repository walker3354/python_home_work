from WorkWidgets.MainWidget import MainWidget
from PyQt6.QtWidgets import QApplication
from Socket_client import Socket_client
import sys

host = "127.0.0.1"
port = 20001

if __name__ == "__main__":
    socket_client = Socket_client(host=host, port=port)
    app = QApplication([])
    main_window = MainWidget(socket_client)
    main_window.setFixedSize(750, 450)
    main_window.show()
    sys.exit(app.exec())
