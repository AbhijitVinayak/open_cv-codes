# Untitled - By: akshatha_kamath - Thu Jan 17 2019

import sensor, image, time

sensor.reset()
sensor.set_pixformat(sensor.RGB565) #To use RGB
#sensor.set_pixformat(sensor.GRAYSCALE) #to use grayscale
sensor.set_framesize(sensor.QVGA)
sensor.set_whitebal(False)
sensor.skip_frames(time = 2000)

clock = time.clock()

while(True):
    clock.tick()
    img = sensor.snapshot()
    print(clock.fps())
