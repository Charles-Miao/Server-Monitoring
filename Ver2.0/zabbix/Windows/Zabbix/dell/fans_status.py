import os
import re

def check_chassis_fans_status():
	conent=os.popen("omreport chassis").readlines()
	for index in range(len(conent)):
		if ": Fans" in conent[index]:
			fans_status=re.split(r'[:]',conent[index])[0].strip()	
	return(fans_status)

if __name__ == '__main__':
	if check_chassis_fans_status()=="Ok":
		print(1)
	else:
		print(0)
