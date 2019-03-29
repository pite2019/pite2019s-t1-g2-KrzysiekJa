import numpy as np
import asyncio
import time


def Car (wheel_angle, speed):
    wheel_angle += np.uniform (-10, 10) * 0,5
    speed       += np.uniform (-10, 10)
    
    if (wheel_angle < 10):
        wheel_angle += np.absolute (wheel_angle - 10)
    if (wheel_angle > 170):
        wheel_angle -= np.absolute (wheel_angle - 170)
    if (speed < 0):
        speed += np.absolute (speed)
    if (speed > 120):
        speed -= np.absolute (speed - 120)
    
    return wheel_angle, speed
    
async def user_funcion ():
    await asyncio.sleep(3)
    command = input ("What to do? ")
    if command != 'stop':
        command = user_funcion()
    
    return command

time_v   = 0
angle    = 90.0
velocity = 0.0
our_car  = [angle, velocity]

print ("Car stars working.")
print ("If you want to stop print: 'stop'")

user_command = user_funcion()

while 1:
    rate (100)
    
    if user_command == 'stop':
        print ("Car stopped.")
        break
    
    our_car = Car (angle, velocity)
    print ("Car agle: ", angle, " car speed: ", velocity)
    time_v += 1