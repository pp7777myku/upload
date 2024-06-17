import socket

# 创建一个TCP/IP套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 与服务器建立连接
server_address = ('localhost', 50001)
client_socket.connect(server_address)

while True:
    try:
        # 接收从服务器发送的数据
        data = client_socket.recv(1024).decode()
        print(f"接收到数据: {data}")
    
    except KeyboardInterrupt:
        print("停止接收数据")
        break

# 关闭连接
client_socket.close()
