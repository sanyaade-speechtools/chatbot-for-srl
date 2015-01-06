#coding:utf-8
'''
Created on 2014年9月15日

@author: loseair123
'''
class Teacher(object):
    def __init__(self,kernal):
        self._kernal=kernal
    def getKernal(self):
        return self._kernal
    def teach(self):
        inputHistoryList = self._kernal.getPredicate('_inputHistory')
        lastestInput=inputHistoryList.pop()
        print 'So it is time for you to teach me how to answer that question \'',lastestInput,'\''
        #Andriod is an OS
        inputText=raw_input('>')
        UpperlastestInput=lastestInput.upper()
        self._kernal._brain.add((u''+UpperlastestInput, u'*', u'*'), 
                                ['template', {}, ['text', {'xml:space': 'default'}, u''+inputText]])
        # self._brain.add((u'HOW ARE YOU', u'*', u'*'), ['template', {}, ['text', {'xml:space': 'default'}, u'\nFINE THANK YOU!\n']])
        print 'Okay!I have remebered that,please try to ask me\'',lastestInput,'\'again.'    
        
    def teachByMobile(self,inputText):
        print 'teachByMobile',inputText
        inputHistoryList = self._kernal.getPredicate('_inputHistory')
        lastestInput=inputHistoryList.pop()
        #print 'So it is time for you to teach me how to answer that question \'',lastestInput,'\''
        #Andriod is an OS
        UpperlastestInput=lastestInput.upper()
        self._kernal._brain.add((u''+UpperlastestInput, u'*', u'*'), 
                                ['template', {}, ['text', {'xml:space': 'default'}, u''+inputText]])
        # self._brain.add((u'HOW ARE YOU', u'*', u'*'), ['template', {}, ['text', {'xml:space': 'default'}, u'\nFINE THANK YOU!\n']])
