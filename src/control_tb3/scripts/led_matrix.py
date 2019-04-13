#!/usr/bin/env python
import rospy
import serial
import time
from std_msgs.msg import Int16MultiArray
import math


def callback(data):
    led_array = list(data.data)
    number = len(led_array)
    if number == 1:
        if led_array[0] == 0:
            data_str = "AA5521700010e"
            print "led off"
            ser.write(data_str)
        elif led_array[0] == 9:
            ser.close()
            print "led end"
        else:
            data_str = "AA5521" + str(led_array[0])
            data_str += "00010e"
            ser.write(data_str)
    else:
        data_str = "AA552" + str(led_array[0])
        del led_array[0]
        count = 1
        for i in led_array:
            if count % 2 == 1:
                data_str += str(i)
            else:
                data_str += str(i).zfill(5)
            count += 1
        data_str += "700010e"
        ser.write(data_str)
        print "led on"




def led_matrix():

    rospy.init_node('LED_matrix', anonymous=True)

    rospy.Subscriber('led_array', Int16MultiArray, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        ser.close()
        print("ShutDown")


def main():
    led_matrix()


if __name__ == '__main__':
    ser = serial.Serial("/dev/ttyACM1",9600)
    time.sleep(7)
    for i in range(1,7): 
        i = str(i)
        data = open("/home/turltebot3-raspi/catkin_ws/src/led_array/sample"+ i + ".txt", "r")
        data_str = 'AA55'
        for text in data:
            text = text.split(",")
        data_str += ''.join(text)
        ser.write(data_str)
        time.sleep(2)
    ser.write("AA5517")
    print "*complete to register led pattern*"

    main()
