from socket import *
from select import select
import re

class Handle(object):
    def __init__(self, connfd,htmls):
        self.connfd = connfd
        self.htmls = htmls

    # 接收并解析请求
    def request(self):
        data = self.connfd.recv(1024).decode()
        pattern = r"[A-Z]+\s+(?P<info>/\S*)"
        result = re.match(pattern,data)
        if result:
            info = result.group("info")
            self.send_html(info)

    def send_html(self, info):
        if info == "/":
            filename = self.htmls+"/index.html"
        else:
            filename = self.htmls+info
        try:
            file = open(filename,"rb")
        except Exception:
            response = """HTTP/1.1 404 NOT FOUND
            Content-Type:text/html
            
            Sorry...
            """
            response = response.encode()
        else:
            response = """HTTP/1.1 200 OK
            Content-Type:text/html

            """
            response = response.encode()+file.read()
        finally:
            self.connfd.send(response)



class WebServer:
    def __init__(self, host=None, port=None, htmls=None):
        self.host = host
        self.port = port
        self.htmls = htmls
        self.rlist = []
        self.wlist = []
        self.xlist = []
        self.sock = self.__create_socket()

    def __create_socket(self):
        sock = socket(AF_INET,SOCK_STREAM)
        self.adress = (self.host,self.port)
        sock.bind(self.adress)
        return sock

    def start(self):
        self.sock.listen(5)
        self.sock.setblocking(False)
        print("监听端口：",self.port)
        self.rlist.append(self.sock)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r == self.sock:
                    self.connect()
                else:
                    self.handle = Handle(r,self.htmls)
                    self.handle.request()
                    self.rlist.remove(r)
                    r.close()
            # for w in ws:
            #     self.mysend(w)


    def connect(self):
        connfd,addr = self.sock.accept()
        print("connect from>",addr)
        connfd.setblocking(False)
        self.rlist.append(connfd)

    # def handle(self,connfd):
    #     request = connfd.recv(1024).decode()
    #     if not request:
    #         self.rlist.remove(connfd)
    #         connfd.close()
    #     self.wlist.append(connfd)

    # def mysend(self,connfd):
    #     pass



if __name__ == '__main__':
        webserver = WebServer(host = "0.0.0.0",port=8889,htmls = "static")
        webserver.start()