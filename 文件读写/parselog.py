import os
import sys


# "   xyz   ".strip()            # returns "xyz"  
# "   xyz   ".lstrip()           # returns "xyz   "  
# "   xyz   ".rstrip()           # returns "   xyz"  
# "  x y z  ".replace(' ', '')   # returns "xyz"

config_path ='%s\\keyword.config' %sys.path[0]
f1_path ='%s\\1.log' %sys.path[0]
f2_path ='%s\\android.log' %sys.path[0]

def parselog():
	with open(config_path,"r",encoding='UTF-8') as config:
		config_content = config.readlines()
		key1 = config_content[0].replace('key1=','').strip()
		key2 = config_content[1].replace('key2=','').strip()
		print(key1)
		print(key2)

	with open(f1_path,"r",encoding='UTF-8')  as f1,open(f2_path,"a",encoding='UTF-8')  as f2:
		lines = []
		for line in f1.readlines():
			if (line.find(key1)!=-1 or line.find(key2)!=-1):
				lines.append(line)
		f2.writelines(lines)

if __name__ == '__main__':
	parselog()