#coding:utf-8
'''
Created on 2014年9月22日

@author: loseair123
'''
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 5050))
num=12345
s.send('give me a hug\0');

