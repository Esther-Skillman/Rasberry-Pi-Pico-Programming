from machine import Pin
import utime

led_red = machine.Pin(15, machine.Pin.OUT)
led_amber = machine.Pin(12, machine.Pin.OUT)
led_green = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led_red.value(1)
        utime.sleep(5)
        led_amber.value(1)
        utime.sleep(2)
        led_red.value(0)
        led_amber.value(0)
        led_green.value(1)
        utime.sleep(5)
        led_green.value(0)
        led_amber.value(1)
        utime.sleep(5)
        led_amber.value(0)

