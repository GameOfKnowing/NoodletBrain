# DIY "Soba" Baby Noodlefeet Code
# by Daniel Lytle (daniellytle.com)
# MIT License
# Designed for use on the Adafruit Trinket M0 board
# in a "Noodle Spawnling" robot designed by Sarah 
# Petkus (zoness.com)

import board
from digitalio import DigitalInOut, Direction, Pull
import pulseio
import simpleio
from adafruit_dotstar import DotStar
import time
import random
 
dotstar = DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness = 0.3)
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT
rightEye = DigitalInOut(board.D0)
leftEye = DigitalInOut(board.D3)
sensor = DigitalInOut(board.D4)
piezo = pulseio.PWMOut(board.D2, duty_cycle=0, frequency = 250, variable_frequency=True)
rightEye.direction = Direction.OUTPUT
leftEye.direction = Direction.OUTPUT
sensor.direction = Direction.INPUT
sensor.pull = Pull.UP

loopCount = 0

rightEye.value = True
leftEye.value = True

dotstar[0] = (0, 0, 255)

def moved():
    dotstar[0] = (255, 255, 0)
    squeak(3)
    time.sleep(2)
    
def eyeBehavior(bNumber):
    if (bNumber == 0):
        rightEye.value = False
        leftEye.value = False
        time.sleep(0.15)
        rightEye.value = True
        leftEye.value = True
    elif (bNumber == 1):
        rightEye.value = False
        time.sleep(0.15)
        rightEye.value = True
    elif (bNumber == 2):
        leftEye.value = False
        time.sleep(0.15)
        leftEye.value = True
    elif (bNumber == 3):
        rightEye.value = False
        time.sleep(0.10)
        leftEye.value = False
        time.sleep(0.05)
        rightEye.value = True
        time.sleep(0.10)
        leftEye.value = True
    elif (bNumber == 4):
        leftEye.value = False
        time.sleep(0.10)
        rightEye.value = False
        time.sleep(0.05)
        leftEye.value = True
        time.sleep(0.10)
        rightEye.value = True

def squeak(sNumber): # sNumber is an int between 0 and 3 inclusive
    if (sNumber == 0):
        for f in (880, 988, 1046):
            piezo.frequency = f         #plays a tone at frequncy f for given time
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.08)            #let note play for 1/4 second        
            piezo.duty_cycle = 0        #set duty cycle to 0%
    elif (sNumber == 1):
        fadeFreq = 3750
        while (fadeFreq > 3250):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq -= 2
        piezo.duty_cycle = 0
        time.sleep(0.05)
        fadeFreq = 4750
        while (fadeFreq > 4250):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq -= 2
        piezo.duty_cycle = 0
        time.sleep(0.05)
        fadeFreq = 3750
        while (fadeFreq > 3250):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq -= 2
        piezo.duty_cycle = 0
        time.sleep(0.05)
        fadeFreq = 4750
        while (fadeFreq > 4250):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq -= 2
        piezo.duty_cycle = 0
    elif (sNumber == 2):
        fadeFreq = 1250
        while (fadeFreq < 2000):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq += 3
        piezo.duty_cycle = 0
        time.sleep(0.1)
        fadeFreq = 250
        while (fadeFreq < 1000):
            piezo.frequency = fadeFreq         #plays a tone at frequncy f for given time
            piezo.duty_cycle = 65536//2    #set duty cycle to 50%
            time.sleep(0.001)            #let note play for 1/4 second
            fadeFreq += 1
        piezo.duty_cycle = 0
    elif (sNumber == 3): #earmarked for vibration event
        fadeFreq = 50
        while (fadeFreq < 115):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2
            if (rightEye.value):
                rightEye.value = False
            else:
                rightEye.value = True
            time.sleep(0.065)
            if (leftEye.value):
                leftEye.value = False
            else:
                leftEye.value = True
            fadeFreq += 2
        while (fadeFreq > 50):
            piezo.frequency = fadeFreq
            piezo.duty_cycle = 65536//2
            if (rightEye.value):
                rightEye.value = False
            else:
                rightEye.value = True
            time.sleep(0.065)
            if (leftEye.value):
                leftEye.value = False
            else:
                leftEye.value = True
            fadeFreq -= 2
        piezo.duty_cycle = 0

while True:
    loopCount += 1
    
    if loopCount >= 1000:
        loopCount = 0
        randNum = random.randint(0, 1000)
        if (randNum > 975):
            bRandNum = random.randint(0, 4)
            if (randNum % 10 == 6 | randNum % 10 == 7):
                sRandNum = random.randint(0, 2)
                squeak(sRandNum)
                eyeBehavior(bRandNum)
            else:
                eyeBehavior(bRandNum)
    
    if (sensor.value == False):
        moved()
        dotstar[0] = (0, 0, 255)
    

False
