import socketserver
import re

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()#获取接收到的数据，并使用strip()函数去掉头部和尾部的空行和空格
        print("{} wrote:".format(self.client_address[0]))#在屏幕上输出客户端地址
        data = str(self.data)                           #将二进制数据转为字符串
        if 'SECRET' in data:                            #如果有'SECRET'
            digits = re.findall(r"\d", data)            #使用正则表达式去匹配所有数据，得到一个列表，如['1','2','3']
            digit_str = ''.join(digits)                 #将它们连接起来
            self.request.sendall(bytes("Digits:{}   Count:{}".format(digit_str,len(digits)),"utf-8"))#向客户端返回信息(二进制数据),len()是获取长度的函数
            self.request.sendall(bytes(digit_str,"utf-8"))
        else:                                           #没有'SECRET'
            self.request.sendall(b'Secret code not found')#向客户端发送字符串  b’xxx‘表示将字符串转为二进制

if __name__ == "__main__":
    HOST, PORT = "10.10.11.5", 1234

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:#创建tcpsever
        server.serve_forever()                                        #启动