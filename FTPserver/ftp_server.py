import os
from socket import *
from threading import Thread
from time import sleep

Ftp = "/home/tarena/WYX_code/month02/FTPserver/FTP/"
class Function:
    def __init__(self, connfd):
        self.connfd = connfd
    def request(self, data):
        tmp = data.split(" ",2)
        if tmp[0] == "LIST":
            self.do_list()
        elif tmp[0] == "GET":
            self.do_get(tmp[1])
        elif data[0] == "PUT":
            self.do_put(tmp[1])
        elif data == "EXIT":
            pass

    # 查看文件列表
    def do_list(self):
        file_list = os.listdir(Ftp)
        if file_list:
            self.connfd.send(b"OK")
            sleep(0.1)
            files = "\n".join(file_list)
            self.connfd.send(files.encode())
        else:
            self.connfd.send(b"FAIL")

    def do_get(self, file_name):
        try:
            file = open(Ftp+file_name,'ab')
        except Exception:
            self.connfd.send(b"FAIL")
        else:
            self.connfd.send(b"OK")
            while True:
                data = file.read(1024)
                if not data:
                    break
                self.connfd.send(data)
            sleep(0.2)
            self.connfd.send(b"##")
            self.connfd.close()
        # if file_name in os.listdir(Ftp):
        #     self.connfd.send(b"OK")
        #     name = Ftp+file_name
        #     old_file = open(name,"a")
        #     while True:
        #         data = old_file.read(128)
        #         if not data:
        #             break
        #         self.connfd.send(data.encode())
        #     old_file.close()
        # else:
        #     self.connfd.send(b"FAIL")

    def do_put(self, param):
        if os.path.exists(param):
            pass


class MyThread(Thread):
    def __init__(self, connfd=None,daemon = True):
        super().__init__()
        self.connfd = connfd
        self.func = Function(connfd)
    # 重写run方法
    def run(self):
        while True:
            data = self.connfd.recv(1024)
            if not data:
                break
            self.func.request(data.decode())
        self.connfd.close()

class FtpServer:
    def __init__(self, host=None, port=None):
        self.__host = host
        self.__port = port
        self.__ADDR = (self.__host,self.__port)
        self.sock = self.__create_sock()

    # 创建套接字
    def __create_sock(self):
        tcp_sock = socket(AF_INET,SOCK_STREAM)
        tcp_sock.bind(self.__ADDR)
        return tcp_sock


    # 创建主函数用于持续接收连接
    def main(self):
        self.sock.listen(5)
        while True:
            connfd,addr = self.sock.accept()
            print("connect from:",addr)
            thread = MyThread(connfd)
            thread.start()
if __name__ == '__main__':
    ftpserver = FtpServer(host = "0.0.0.0",port = 8888)
    ftpserver.main()