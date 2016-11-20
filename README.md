# pi-robot

##Getting wiimote working
http://www.theraspberrypiguy.com/raspberry-pi-how-to-use-a-wiimote/

##wiring diagram for TB6612FNG motor driver board
http://chojayr.blogspot.co.uk/

##Control 2 motor robot script
https://github.com/chojayr/Pi-dro

##Servo Driver board wiring
http://www.lediouris.net/RaspberryPI/servo/readme.html

##vnc setup
On pi install

$ sudo apt-get update

$ sudo apt-get install tightvncserver

start
$ vncserver :1

On laptop

##ssh to pi
Connect with Putty, just enter hostname, use username "pi" and password "raspberry"

## Camera setup

###Installation
sudo apt-get install vlc

###Stream with command
raspivid -o - -t 0 -n -w 1920 -h 1080 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
raspivid -o - -t 0 -n -w 1280 -h 720 -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
 	
