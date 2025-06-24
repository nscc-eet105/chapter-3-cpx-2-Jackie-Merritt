#Chp3-CPX2
from adafruit_circuitplayground import cp
import time
BLACK = (0, 0, 0)
while True:
    for num in range(0, 10):
        cp.pixels[num] = (0, 100, 100) #
        time.sleep(.2)
        cp.pixels[num] = BLACK
        time.sleep(.2)

    for num in range(9, -1, -1):
        cp.pixels[num] = (150, 0, 150) #
        time.sleep(.2)
        cp.pixels[num] = BLACK
        time.sleep(.2)
