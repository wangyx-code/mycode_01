import sys
from socket import *
from threading import Thread

class FtpHandle:
    ADDR = ("127.0.0.1",8888)
    def __init__(self):
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect(FtpHandle.ADDR)
    def do_list(self):
        # 发送请求
        self.sock.send(b"LIST")
        # 等待响应
        result = self.sock.recv(128).decode()
        if result == "OK":
            files = self.sock.recv(1024)
            print(files.decode())
        else:
            print("无文件")

    def do_get(self):
        # 发送请求
        msg = input("请输入需要下载文件的名称：")
        file_name = "GET " + msg
        self.sock.send(file_name.encode())
    #     获取响应
        result = self.sock.recv(128).decode()
        if result == "OK":
            new_file = open(msg,"wb")
            while True:
                data = self.sock.recv(1024)
                if data == b"##":
                    break
                new_file.write(data)
            new_file.close()
            print("下载成功")
        else:
            print("没有找到该文件")

    def do_put(self):
        # 判断文件是否存在
        msg = input("请输入需要上传文件的名称：")
        try:
            file = open(msg,"rb")
        except Exception:
            print("找不到文件")
            return
        # 发送请求
        file_name = "PUT " + msg
        self.sock.send(file_name.encode())
    #     等待响应
        result = self.sock.recv(128).decode()
        if result == "OK":
            pass
        else:
            print("文件已存在")

    def do_exit(self):
        self.sock.send(b"EXIT")
        sys.exit("服务结束")


class FtpView:
    def __init__(self):
        self.__ftpheadle = FtpHandle()

    def __display_menu(self):
        print("1>查看文件")
        print("2>下载文件")
        print("3>上传文件")
        print("4>退   出")
        print("")

    def __select_menu(self):
        number = input("请输入序号>>>>")
        if number == "1":
            self.__ftpheadle.do_list()
        if number == "2":
            self.__ftpheadle.do_get()
        if number == "3":
            self.__ftpheadle.do_put()
        if number == "4":
            self.__ftpheadle.do_exit()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()
if __name__ == '__main__':
    ftpview = FtpView()
    ftpview.main()