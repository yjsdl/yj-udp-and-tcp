import socket	
	
def main():
    # 1.创建套接字(socket)
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2.绑定本地信息(bind)
    tcp_server_socket.bind(("",7890))

    # 3.让默认的套接字由主动变为被动(listen)
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来。。。")
        # 4.等待客户端的连接(accept)
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来。。"% str(client_addr))
        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端传送过来的请求是:%s" % recv_data.decode("utf-8"))
        # 回送一部分数据给客户端
        new_client_socket.send("hahahaha",encode("utf-8"))
        # 关闭套接字
        new_client_socket.close()
        print("已经服务完毕")
    tcp_server_socket.close()

if __name__ == "__main__":
	main()

