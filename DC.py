import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pwmPin = 24
GPIO.setup(pwmPin, GPIO.OUT)
pwm = GPIO.PWM(pwmPin, 50) # PWM object at 50 Hz (20 ms period)
pwm.start(100)
try: 
  i=0
  
  for dc in range(0,100):
    pwm.ChangeDutyCycle(100-dc)
    print(100-dc)
    time.sleep(0.005)
   
except KeyboardInterrupt:
  GPIO.cleanup()