import machine
import utime
led_onboard = machine.Pin(15, machine.Pin.OUT) #Pin 25 for onboard LED
while True:
    led_onboard.value(1)
    utime.sleep(5)
    led_onboard.value(0)
    utime.sleep(5)