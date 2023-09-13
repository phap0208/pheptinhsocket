# ver1
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.9', 12345))


num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))

operations = ['add', 'sub', 'mul', 'div']

for operation in operations:
    # Gửi dữ liệu tới máy chủ
    client_socket.send(f"{operation},{num1},{num2}".encode())

    # Nhận kết quả từ máy chủ và in ra màn hình
    result = client_socket.recv(1024).decode()
    print(f"Kết quả ({operation}): {result}")

# Đóng kết nối
client_socket.close()

