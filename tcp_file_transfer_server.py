import socketserver
import time
import os


# 定义一个类
class EddyFtpserver(socketserver.BaseRequestHandler):
    # 定义接收文件方法
    def recvfile(self, filename):
        print("Starting reve file!\n")

        f = open(filename, 'wb')#创建文件，方式为只读，二进制流

        while True:
            data = self.request.recv(4096)      #循环接收数据
            if data == b'EOF':                  #如果收到b'EOF'
                print("Receive file success!")
                break                           #结束，跳出循环
            else:
                print(str(data,'utf-8'))        #否则，在屏幕上打印收到的数据
            f.write(data)                       #将数据写入文件
        f.close()
        print('\n')
        print('Connection closed')




    # SocketServer的一个方法
    def handle(self):
        print("get connection from :", self.client_address)
        filename = 'recieve.txt'        #指定文件名
        self.recvfile(filename)         #调用函数





if __name__ == "__main__":
    host = '10.10.11.6'
    port = 1234
    # 实例化
    s = socketserver.ThreadingTCPServer((host, port), EddyFtpserver)
    s.serve_forever()