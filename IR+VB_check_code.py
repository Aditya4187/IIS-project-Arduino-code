from machine import Pin
from machine import ADC
from time import sleep

led = Pin(4,Pin.OUT)
sensor = ADC(0)
solenoid = Pin(5,Pin.OUT)
threshold = 50
ir_sensor_pin = Pin(2, Pin.IN)  # set up the IR sensor pin

def loop():
    value = sensor.read()
    ir_value = ir_sensor_pin.value()  # read the IR sensor value
    if value >= threshold or ir_value == 1:  # only trigger if both sensor values are met
        led.value(0)
        solenoid.value(1)
        sleep(1)
    else:
        led.value(1)
        solenoid.value(0)
        sleep(1)

while True:
    loop()

        
