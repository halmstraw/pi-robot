import curses
import Adafruit_PCA9685

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

key = ''
while key != ord('q'):
    key = scr.getch()

    if key == curses.KEY_DOWN:
      yaxis += degIncrease

      if yaxis > maxDegree:
        yaxis = maxDegree
    
      setDegree(1, yaxis)

    elif key == curses.KEY_UP:
      yaxis -= degIncrease

      if yaxis < 0:
        yaxis = 0
          
      setDegree(1, yaxis)

    if key == curses.KEY_LEFT:
      xaxis += degIncrease

      if xaxis > maxDegree:
        xaxis = maxDegree
    
      setDegree(0, xaxis)

    elif key == curses.KEY_RIGHT:
      xaxis -= degIncrease

      if xaxis < 0:
        xaxis = 0
          
      setDegree(0, xaxis)

curses.endwin()