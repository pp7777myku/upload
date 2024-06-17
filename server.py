import socket
import serial

# 设置串口参数
ser = serial.Serial('COM11', 115200)

# 创建文本文件
text_filename = 'received_data.txt'
text_file = open(text_filename, 'w')

try:
    while True:
        try:
            # 从串口读取数据
            data = ser.readline().decode().strip()
            print(f"从串口接收到数据: {data}")

            # 将数据写入文本文件
            text_file.write(data + '\n')
            text_file.flush()

        except KeyboardInterrupt:
            print("停止生成数据")
            break

finally:
    # 关闭文本文件
    text_file.close()

# 创建一个TCP/IP套接字
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 与服务器建立连接
server_address = ('localhost', 12345)
server_socket.connect(server_address)
