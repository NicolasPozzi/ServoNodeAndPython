import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)

ajoutAngle = 5
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
if sys.argv[1] == '2':
    #print("On est rentre dans le if !")
    nbrTour = int(sys.argv[2])

    pwm=GPIO.PWM(17,100)
    pwm.start(5)

    angle1 = 0
    duty1 = float(angle1)/10 + ajoutAngle

    angle2=180
    duty2= float(angle2)/10 + ajoutAngle

    i = 0

    while i < nbrTour:
         pwm.ChangeDutyCycle(duty1)
         time.sleep(0.8)
         pwm.ChangeDutyCycle(duty2)
         time.sleep(0.8)
         i = i+1
    GPIO.cleanup()

if sys.argv[1] == '1':
    #angle = float(input("Entrez l'angle souhaite :\n"))
    angle = int(sys.argv[2])
    #duree = int(input("Entrez la duree durant laquelle le Servo devra tenir sa position : ( en secondes )\n"))
    duree = 5
    pwm=GPIO.PWM(17,100)
    pwm.start(5)

    angleChoisi = angle/10 + ajoutAngle
    pwm.ChangeDutyCycle(angleChoisi)
    time.sleep(duree)
    GPIO.cleanup()