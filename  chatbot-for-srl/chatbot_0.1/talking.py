#coding:utf-8
'''
Created on 2014年9月15日

@author: loseair123
'''
import teach
class Talk(object):
    def __init__(self,kernal):
        self._kernal=kernal
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
            if inputText=='exit':
                #k.saveBrain("standard.brn")
                #k.loadBrain('standard.brn')
                self.saveBrain("standard.brn")
                print 'Exit successfully!'
                break
            elif inputText=='bad answer':
                teacher=teach.Teacher(self._kernal)
                teacher.teach()
            else:
                print self._kernal.respond(inputText)
            
            