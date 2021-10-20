import RPi.GPIO as GPIO
import time

Pin1 = 17
Pin2 = 22
Pin3 = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(Pin1, GPIO.OUT)
GPIO.setup(Pin2, GPIO.OUT)
GPIO.setup(Pin3, GPIO.OUT)

pwm1 = GPIO.PWM(Pin1, 100)
pwm2 = GPIO.PWM(Pin2, 100)
pwm3 = GPIO.PWM(Pin3, 100) # PWM object on our pin at 100 Hz
pwm.start(0) # start with LED off

with open("value.txt", 'r') as f:
 if int(f.read()) == Pin1:
  with open("led_pwm.txt", 'r') as f:
   dutyCycle = float(f.read()) # read duty cycle value from file
   pwm1.ChangeDutyCycle(dutyCycle)
   time.sleep(15.1)

 if int(f.read()) == Pin2:
  with open("led_pwm.txt", 'r') as f:
   dutyCycle = float(f.read()) 
   pwm2.ChangeDutyCycle(dutyCycle)
   time.sleep(15.1)

 if int(f.read()) == Pin3:
    with open("led_pwm.txt", 'r') as f:
     dutyCycle = float(f.read()) # read duty cycle value from file
     pwm3.ChangeDutyCycle(dutyCycle)
     time.sleep(15.1)
  



