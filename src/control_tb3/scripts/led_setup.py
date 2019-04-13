#!/usr/bin/env python

import serial

def main():
	try:
		while True:
			ser = serial.Serial('/dev/ttyACM1', 9600)
	except KeyboardInterrupt:
		pass
    

if __name__ == '__main__':
    main()
