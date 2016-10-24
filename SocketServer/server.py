# coding=utf-8
__author__ = 'eric'


import SocketServer
import datetime

class myMonitorHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        while True:
            recv_data = self.request.recv(1024)
            print(len(recv_data))
            if not len(recv_data):
                print("break")
                break
            print("From %s:%s %s" % (self.client_address,datetime.datetime.now(),recv_data.decode("utf8")))

if __name__ == "__main__":
    host,port = '',18001

    server = SocketServer.ThreadingTCPServer((host,port),myMonitorHandler)
    print("服务端开始启动")
    server.serve_forever()
