# -*- coding: utf-8 -*-
"""Count Down Calculator

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ejNXvM2FaevwUjswN-2Ybxe7l5JNolTJ
"""

#Python Countdown Calculator

import time
def countdown(time_sec):
  while time_sec:
    mins, secs = divmod(time_sec, 60)
    timeformat = '{:02d}:{:02d}'. format(mins,secs)
    print(timeformat, end ='\r')
    time.sleep(1)
    time_sec -=1

    print("stop")
  num=int(input("Set the timer to sec"))

  countdown(num)