from gpiozero import MotionSensor
from gpiozero import LED
import time

yellow_led = LED(17)
pir = MotionSensor(4)
count = 0


pir.wait_for_motion()
count = count + 1
print("Motion detected")
pir.wait_no_motion()
yellow_led.off()
print("No Motion")
