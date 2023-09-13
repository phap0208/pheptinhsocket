import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.1.9', 12345))
server_socket.listen(1)

print("Đang chờ kết nối từ client...")

client_socket, client_address = server_socket.accept()
print(f"Đã kết nối tới {client_address}")

while True:
    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()

    # Kiểm tra nếu dữ liệu không rỗng
    if data:
        operator, num1, num2 = data.split(',')
        num1 = float(num1)
        num2 = float(num2)

        # Thực hiện phép tính
        if operator == 'add':
            result = num1 + num2
        elif operator == 'sub':
            result = num1 - num2
        elif operator == 'mul':
            result = num1 * num2
        elif operator == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Không thể chia cho 0"

        # Gửi kết quả về client
    client_socket.send(str(result).encode())
