import curses
import Adafruit_PCA9685
import time 
import socket 
import pygame
import RPi.GPIO as GPIO

#SETUP For Robot Tracks
GPIO.setmode(GPIO.BCM)
interval = 0.5
regularUpdate = True

# Set which GPIO pins the drive outputs are connected
PWMA = 17
AIN1 = 27
AIN2 = 4
PWMB = 23
BIN1 = 24
BIN2 = 25
STBY = 22
##
### Set all the drive pins as output pins
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

state = GPIO.input(PWMA)
global hadEvent
global moveUp
global moveDown
global moveLeft
global moveRight
global moveQuit

hadEvent = True
moveUp = False
moveDown = False
moveLeft = False
moveRight = False
moveQuit = False

pygame.init()
screen = pygame.display.set_mode([200,200])
pygame.display.set_caption("custompidro - Press [ESC] to quit")

#SETUP for Servo
# Initialise the PWM device using the default address
pwm = Adafruit_PCA9685.PCA9685()

servoMin = 150  # Min pulse length out of 4096
servoMax = 600  # Max pulse length out of 4096
maxDegree = 60 # Degrees your servo can rotate
degIncrease = 5 # Number of degrees to increase by each time

pwm.set_pwm_freq(60) # Set PWM frequency to 60Hz

def setDegree(channel, d):
    degreePulse = servoMin
    degreePulse += int((servoMax - servoMin) / maxDegree) * d
    pwm.set_pwm(channel, 0, degreePulse)  
# Set up curses for arrow input
scr = curses.initscr()
curses.cbreak()
scr.keypad(True)
scr.addstr(0, 0, "Servo Control")
scr.addstr(1, 0, "use cursor keys to look around")
scr.addstr(2, 0, "q to quit")
scr.refresh()

xaxis = 30
yaxis = 30

setDegree(0, xaxis)
setDegree(1, yaxis)

def forward():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.HIGH))
    (GPIO.output(BIN1, GPIO.HIGH))
    (GPIO.output(BIN2, GPIO.LOW))
    (GPIO.output(STBY, GPIO.HIGH))
    (GPIO.output(PWMA, GPIO.HIGH))
    (GPIO.output(PWMB, GPIO.HIGH))

def reverse():
    (GPIO.output(AIN1, GPIO.HIGH))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.HIGH))
    (GPIO.output(STBY, GPIO.HIGH))
    (GPIO.output(PWMA, GPIO.HIGH))
    (GPIO.output(PWMB, GPIO.HIGH))

def left():
    (GPIO.output(AIN1, GPIO.HIGH))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.HIGH))
    (GPIO.output(BIN2, GPIO.LOW))
    (GPIO.output(STBY, GPIO.HIGH))
    (GPIO.output(PWMA, GPIO.HIGH))
    (GPIO.output(PWMB, GPIO.HIGH))\

def right():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.HIGH))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.HIGH))
    (GPIO.output(STBY, GPIO.HIGH))
    (GPIO.output(PWMA, GPIO.HIGH))
    (GPIO.output(PWMB, GPIO.HIGH))

def off():
    (GPIO.output(AIN1, GPIO.LOW))
    (GPIO.output(AIN2, GPIO.LOW))
    (GPIO.output(BIN1, GPIO.LOW))
    (GPIO.output(BIN2, GPIO.LOW))
    (GPIO.output(STBY, GPIO.LOW))
    (GPIO.output(PWMA, GPIO.LOW))
    (GPIO.output(PWMB, GPIO.LOW))

key = ''
while key != ord('q'):
    key = scr.getch()

#Define Servo Control First
    if key == ord('s'):
      yaxis += degIncrease

      if yaxis > maxDegree:
        yaxis = maxDegree
    
      setDegree(1, yaxis)

    if key == ord('w'):
      yaxis -= degIncrease

      if yaxis < 0:
        yaxis = 0
          
      setDegree(1, yaxis)

    if key == ord('a'):
      xaxis += degIncrease

      if xaxis > maxDegree:
        xaxis = maxDegree
    
      setDegree(0, xaxis)

    if key == ord('d'):
      xaxis -= degIncrease

      if xaxis < 0:
        xaxis = 0
          
      setDegree(0, xaxis)

    #Now for motors
    if key == curses.KEY_UP:
      forward()
      time.sleep(interval)
      off()

    if key == curses.KEY_DOWN:
      reverse()
      time.sleep(interval)
      off()

    if key == curses.KEY_LEFT:
      left()
      time.sleep(interval)
      off()

    if key == curses.KEY_RIGHT:
      right()
      time.sleep(interval)
      off()

curses.endwin()

# Function to handle pygame events
def PygameHandler(events):
# Variables accessible outside this function
    global hadEvent
    global moveUp
    global moveDown
    global moveLeft
    global moveRight
    global moveQuit

    # Handle each event individually
    for event in events:
        if event.type == pygame.QUIT:
            # User exit
            hadEvent = True
            moveQuit = True
        elif event.type == pygame.KEYDOWN:
            # A key has been pressed, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_UP:
                moveUp = True
            elif event.key == pygame.K_DOWN:
                moveDown = True
            elif event.key == pygame.K_LEFT:
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_ESCAPE:
                moveQuit = True
        elif event.type == pygame.KEYUP:
            # A key has been released, see if it is one we want
            hadEvent = True
            if event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_DOWN:
                moveDown = False
            elif event.key == pygame.K_LEFT:
                moveLeft = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False
            elif event.key == pygame.K_ESCAPE:
                moveQuit = False

try:
    print 'Press [ESC] to quit'
    # Loop indefinitely
    while True:
        # Get the currently pressed keys on the keyboard
        PygameHandler(pygame.event.get())
        if hadEvent or regularUpdate:

            hadEvent = False
            #driveCommands = ['X', 'X', 'X', 'X']  
            if moveQuit:
                break
            elif moveUp:
                forward() 
            elif moveDown:
                reverse()
            elif moveLeft:
                left()
            elif moveRight:
                right()
            else:
                off()

        time.sleep(interval)
# Send the drive commands
except KeyboardInterrupt:
    print "(exit goodbye ciao)"
    GPIO.cleanup()