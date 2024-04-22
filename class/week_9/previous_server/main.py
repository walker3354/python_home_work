from Socket_server import SocketServer

host = "127.0.0.1"
port = 20001

if __name__ == "__main__":
    server = SocketServer(host, port)
    server.daemon = True
    server.serve()
    while True:
        command = input()
        if command == "finish":
            break

    server.server_socket.close()
    print("leaving ....... ")
