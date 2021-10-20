import RPi.GPIO as GPIO
p= 5
dc=50
GPIO.setmode(GPIO.BCM)
GPIO.setup(p, GPIO.OUT)
T = 0.02                   # define the servo signal period
pwm = GPIO.PWM(p, 1/T)   # PWM instance @ 50 Hz, 1/(20 ms)
pwm.start(dc)              # Start PWM
pwm.ChangeDutyCycle(dc)    # Change duty cycle as desired
pwm.stop()                 # Stop PWM