# pi-robot

##Getting wiimote working
http://www.theraspberrypiguy.com/raspberry-pi-how-to-use-a-wiimote/

##wiring diagram for TB6612FNG motor driver board
http://chojayr.blogspot.co.uk/

##Control 2 motor robot script
https://github.com/chojayr/Pi-dro

##Servo Driver board wiring
http://www.lediouris.net/RaspberryPI/servo/readme.html

##Servo python scripts from adafruit
https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview

##vnc setup
On pi install

$ sudo apt-get update

$ sudo apt-get install tightvncserver

start
$ vncserver :1

On laptop

##ssh to pi
Connect with Putty, just enter hostname, use username "pi" and password "raspberry"

## VLC Camera setup
Works but stream not stable, can't view in browser
###Installation
sudo apt-get install vlc

###Stream with command
raspivid -o - -t 0 -n -w 1920 -h 1080 -fps 12 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
raspivid -o - -t 0 -n -w 1280 -h 720 -fps 30 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554/}' :demux=h264
 	
##MPEG Streamer Camera Setup

http://blog.cudmore.io/post/2015/03/15/Installing-mjpg-streamer-on-a-raspberry-pi/
### commands
'sudo apt-get install libjpeg8-dev imagemagick libv4l-dev'
'ln -s /usr/include/linux/videodev2.h /usr/include/linux/videodev.h'
'wget http://sourceforge.net/code-snapshots/svn/m/mj/mjpg-streamer/code/mjpg-streamer-code-182.zip'
'unzip mjpg-streamer-code-182.zip'

build with 'make'
'cd mjpg-streamer-code-182/mjpg-streamer'
'make mjpg_streamer input_file.so output_http.so'

install by copying files
'sudo cp mjpg_streamer /usr/local/bin  '
'sudo cp output_http.so input_file.so /usr/local/lib/  '
'sudo cp -R www /usr/local/www'

start the camera module
'mkdir /tmp/stream  
    raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 &'
    
start mjpg-streamer for raspberry pi camera module. This streams using ‘input_file.so’
'LD_LIBRARY_PATH=/usr/local/lib  
    mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"'
