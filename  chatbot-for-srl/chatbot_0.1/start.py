'''
@author: Administrator
'''
import aiml
import talking
import mobile
k = aiml.Kernel()

talker=talking.Talk(k)
talker.loadBrain('standard.brn')
#talker.init()
m=mobile.mobile(talker)
m.startMobile()
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
my name is eko
I am a man
do you know Daisy? 
she is now in USA and I really miss her.
do you like Daisy?  
'''