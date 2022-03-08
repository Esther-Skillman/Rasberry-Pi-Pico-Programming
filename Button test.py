from machine import Pin
import utime

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        print("Button pressed!")
        utime.sleep(0.5)