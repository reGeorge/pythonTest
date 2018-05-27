# import multiprocessing
from multiprocessing import Process
# import time
import os

i = 1
def control():
	p = Process(target=action)
	p.daemon = False
	p.start()

	cmd = input('输入1结束本次记录日志操作')


def action():
	# name1 = input('name')
	print('action')
	os.popen('adb logcat')

if __name__ == '__main__':
	while i<10:
		control()
		i+=1