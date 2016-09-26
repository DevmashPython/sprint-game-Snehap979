import msvcrt
import time
 
finish=7
count=0
print"press some key"
raw_input()
e_time=time.time()
print "press a for right"
while 1:
 	key=msvcrt.getch()
 	if key=='a':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break
print "type s to go down"

while 1:			
	key=msvcrt.getch()
	if key=='s':
		count=count+1
		print "                         |"       
		if count==finish:
			count=0
			break

print "press a to go right     ",

while 1:
	key=msvcrt.getch()
	if key=='a':
		count=count+1
		print "-->",
        if count==finish:
        	count=0
        	break
time_elapsed=time.time()-e_time
print"\ncongrats.time taken is:" + str(time_elapsed)		