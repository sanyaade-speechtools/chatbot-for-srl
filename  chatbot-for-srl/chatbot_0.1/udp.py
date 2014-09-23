#coding:utf-8
'''
Created on 2014年9月22日

@author: loseair123
'''
import socket
import time


def udpSend(text,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto('101',('172.29.35.247', port))
    s.close()
    print 'send','1'
    time.sleep(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto('102',('172.29.35.247', port))
    s.close()
    print 'send','2'
    time.sleep(1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto('103',('172.29.35.247', port))
    s.close()

udpSend('', 5050)
'''
for x in range(3):
    time.sleep(1)
    print 'send',x
    udpSend(str(x)+'\0', 5555)
'''

