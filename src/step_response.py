"""! @file step_response.py
Doxygen Style Doctring for the file
"""
import time
import micropython
micropython.alloc_emergency_exception_buf(100)
import cqueue   
import pyb
 
def timer_int(dummy):
    """! Doxygenstyle dostring for interrupt callback function
"""
    volt_queue.put(adc0.read())
    
def step_response():
    """! Doxygenstyle dostring for step response function
"""
    pinC0.value(1)
    timmy.callback(timer_int)
    while not volt_queue.full():
        pass
    timmy.deinit()
   
if __name__ == "__main__":
    """! Doxygenstyle dostring for main function
"""
    #The following code only runs if this file is run as the main script;
    #It does not run if this file is imported as a module:
    adc0 = pyb.ADC(pyb.Pin.board.PB0)
    QUEUE_SIZE = 200
    volt_queue = cqueue.IntQueue(QUEUE_SIZE)
    pinC0 = pyb.Pin(pyb.Pin.board.PC0, pyb.Pin.OUT_PP)
    pinC0.value(0) 
    time.sleep(2)
    timmy = pyb.Timer (1, freq = 100)
    step_response()
    for idx in range(QUEUE_SIZE):
        print(f'{10*idx}, {volt_queue.get()*3.3/4096}')
    print('END')
