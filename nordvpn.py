import os
import time
import random

t=int(input("Enter the change ip time(sec):"))
iplst=['Albania','Greece','Portugal','Argentina','Hong_Kong','Romania','Australia','Hungary','Serbia','Austria','Iceland','Singapore','Belgium','Slovakia','Bosnia_And_Herzegovina','Indonesia','Slovenia','Brazil','Ireland','South_Africa','Bulgaria','Israel','South_Korea','Canada','Italy','Spain','Chile','Japan','Sweden','Costa_Rica','Latvia','Switzerland','Croatia','Luxembourg','Taiwan','Cyprus','Malaysia','Thailand','Czech_Republic','Mexico','Turkey','Denmark','Moldova','Ukraine','Estonia','Netherlands','United_Kingdom','Finland','New_Zealand','United_States','France','North_Macedonia','Vietnam','Georgia','Norway','Germany','Poland']
while(True):
 os.system("echo 'New IP'")
 os.system("nordvpn connect "+random.choice(iplst))
 time.sleep(3*t/4)
 os.system("nordvpn status")
 time.sleep(t/4)
 os.system("echo 'Changing IP'")

 

