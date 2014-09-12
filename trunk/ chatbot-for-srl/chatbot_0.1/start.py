'''
@author: Administrator
'''
import aiml
k = aiml.Kernel()
'''
k.learn("std-startup.xml")
k.respond("load aiml b")

while True: 
    print k.respond(raw_input("> "))


print k.numCategories()
print k.respond('who is your father?')
'''
k.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
#k.saveBrain("standard.brn")
#k.loadBrain('standard.brn')

userNum=raw_input('Plz input the user number.')
userName=[];
for x in range(int(userNum)):
    userName.append(raw_input('Plz input user name:'))
    
count=int(userNum)

while True:
    print  k.respond(raw_input('>'), userName[(count%int(userNum))])
    count+=1

