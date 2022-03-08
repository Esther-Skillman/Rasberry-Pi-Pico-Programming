from machine import Pin
import utime

led = machine.Pin(15, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.value(1)
        utime.sleep(2)
    led.value(0)
