#coding:utf-8
'''
Created on 2014年9月15日

@author: loseair123
'''
import teach
import socket
import threading
class Talk(object):
    def __init__(self,kernal):
        self._kernal=kernal
        #这里的action要在C++映射成不同的动作100 happy 101 node 106 
        self._actionDict={'sad':100,'happy':101,'angry':100,'sorry':100,
                          'hug':100,'bye':106,'nod':106,'leg':101,
                          'handsome':106,'miss':100}
    def getKernal(self):
        return self._kernal
    def init(self):
        #k.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
        self._kernal.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    def loadBrain(self,brainName):
        self._kernal.loadBrain(brainName)
    def saveBrain(self,brainName):
        self._kernal.saveBrain(brainName)
    def resetBrain(self):
        self._kernal.resetBrain()
    def startTalking(self):
        while True:
            inputText=raw_input('>')
            action=self.findActionInDict(inputText)
            if inputText=='exit':
                self.saveBrain("standard.brn")
                print 'Exit successfully!'
                break
            elif action:
                response=self._kernal.respond(inputText);
                message=str(action)+response;
                t = threading.Thread(target=self.sendMessage(message+'\0', '172.29.35.247',5050), name='SendMessageThread')
                t.start()
                t.join()
                print response
            elif inputText=='bad answer':
                teacher=teach.Teacher(self._kernal)
                teacher.teach()
            else:
                response=self._kernal.respond(inputText);
                message='000'+response;
                t = threading.Thread(target=self.sendMessage(message+'\0', '172.29.35.247',5050), name='SendMessageThread')
                t.start()
                t.join()
                print response
   
    def sendMessage(self,message,ipAddr,port):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(message,(ipAddr, port))
        s.close()     
        
    def findActionInDict(self,inputText):
        for d,x in self._actionDict.items():
            if inputText.find(d)!=-1:
                #print 'Action:',d
                #print 'ActionCode',x
                return x
            

            