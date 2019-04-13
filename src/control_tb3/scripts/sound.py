# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:44:22 2018

@author: is028
"""
#!/usr/bin/env pythom
# -*- coding: utf-8 -*-

from subprocess import call
from time import sleep

def play(path):
    call(["aplay", path])

def repeat(path, time):
	for i in range(time):
		print(i)
		call(["aplay", path])
		sleep(5)

# volume revel : 0~5
def set_volume(revel):
	init = 50
	volume = init + revel * 10
	try:
		if (volume <= 100) and (volume >= 0):
			print(4)
			call(["amixer", "-D", "pulse", "sset", "Master",
 				str(volume)+"%"])
	except ValueError:
		pass


if __name__ == '__main__':
	#play("/home/yume/デスクトップ/chaim.wav")
	set_volume(2)
	repeat("/home/turtlebot3-raspi/catkin_ws/src/chaim.wav",3)
	print(3)
