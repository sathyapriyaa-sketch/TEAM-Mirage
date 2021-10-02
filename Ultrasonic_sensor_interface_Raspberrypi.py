import RPi.GPIO as GPIO
import time
USsensor(astring):
   if(astring == "beep"):
       Beep()
       
TRIG=21
ECHO=20
TOI_spot = TOI()
if(TOI_spot < 100):
    R = 0
else
   R = 1    
if(R == 0):
  BPS = 110
  BPD = 70
  print("normal")
while(R == 1):
  BPS = 130
  BPD = 90
  print("at risk")
  USsensor("beep")
GPIO.setmode(GPIO.BCM)
while True:
    print("distance measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG,False)
    print("waiting for sensor to settle")
    time.sleep(0.2)
    GPIO.output(TRIG,True)
    time.sleep(0.00001)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start=time.time()
    while GPIO.input(ECHO)==1:
        pulse_end=time.time()
    pulse_duration=pulse_end-pulse_start
    distance=pulse_duration*17150
    distance=round(distance,2)
    print("distance:"),distance,"cm"
    time.sleep(2)    