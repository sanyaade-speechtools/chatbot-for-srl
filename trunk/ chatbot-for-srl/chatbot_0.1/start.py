'''
@author: Administrator
'''
import aiml
import talking
k = aiml.Kernel()

talker=talking.Talk(k)
talker.loadBrain('standard.brn')
#talker.init()
talker.startTalking()
#k.saveBrain("standard.brn")
#k.loadBrain('standard.brn')
'''
userNum=raw_input('Plz input the user number.')
userName=[];
for x in range(int(userNum)):
    userName.append(raw_input('Plz input user name:'))
    
count=int(userNum)

while True:
    print  k.respond(raw_input('>'), userName[(count%int(userNum))])
    count+=1

'''