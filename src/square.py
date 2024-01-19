"""! @file squre.py
Doxygen Style Doctring for the file
"""
import utime

pinC0 = pyb.Pin (pyb.Pin.board.PC0, pyb.Pin.OUT_PP)

while True:
    pinC0.high ()
    utime.sleep(5)
    pinC0.low ()
    utime.sleep(5)
    

