from machine import Pin, Timer
import utime
#timer = Timer()
trigger = Pin(3, Pin.OUT) #GPIO Pins- General Purpose INput/OUTput 
echo = Pin(2, Pin.IN)
led = Pin(15,Pin.OUT) #output to pin, cathode connected at GND pin (38)

def ultra(): #code necessary to take a reading
   trigger.low() #ensures trigger is not active
   utime.sleep_us(2) #2 microseconds
   trigger.high()
   utime.sleep_us(5)
   trigger.low() #5 microsecond pulse sent from the sensor
   while echo.value() == 0: #no echo pulse is received
       signaloff = utime.ticks_us() #timestamp
   while echo.value() == 1: #echo pulse is received
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2 #0.0343 - speed of sound (cm/s), /2 - from sensor to object
   #return distance
   if distance > 100:
       print("Distance:",distance / 100,"m")
   else:
       print("Distance:", distance, "cm")
   if distance < 5:
       led.value(1)
   else:
       led.value(0)
   #return distance
while True:
    ultra()
    utime.sleep(1)

   