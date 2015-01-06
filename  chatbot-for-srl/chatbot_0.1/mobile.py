# coding:utf-8
'''
Created on 2014年10月4日

@author: loseair123
'''
import socket
import threading
import time

class mobile(object):
    _learnflag=0;
    def __init__(self, talker):
        self._talker=talker
        
    def startTcp(self):
        print 'Start TCP...'
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        s.bind(('172.29.33.49', 55555));
        s.listen(5)
        print 'Waiting for connection...'
        def tcplink(sock, addr):
            print 'Accept new connection from %s:%s...' % addr
            sock.send('Welcome!\n')
            
            while True:
                data = sock.recv(1024)
                time.sleep(1)
                if data == 'exit' or not data:
                    sock.send(self._talker.responseForMobile(data)+'\n')
                    break
                elif data=='bad answer':
                    print 'learnflag=',self._learnflag
                    sock.send('So I guess it is time for learning,what should I say?\n')
                    self._learnflag=1
                    continue
                if self._learnflag==1:
                    print 'learnflag=',self._learnflag
                    self._talker.learnForMobile(data) 
                    sock.send('Okay,I remember that,try to ask me again.\n')
                    self._learnflag=0
                    continue
                response=self._talker.responseForMobile(data)+'\n';
                sock.send(response)    
            sock.close()
            print 'Connection from %s:%s closed.' % addr
        while True:
        # 接受一个新连接:
            sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
            t = threading.Thread(target=tcplink, args=(sock, addr))
            t.start()
            
    def startMobile(self):
        print 'Start Mobile...'
        t = threading.Thread(target=self.startTcp)
        t.start();