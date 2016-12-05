# pi-robot

Great wiring view for the pi
https://pinout.xyz/

##Getting wiimote working
http://www.theraspberrypiguy.com/raspberry-pi-how-to-use-a-wiimote/

##wiring diagram for TB6612FNG motor driver board
http://chojayr.blogspot.co.uk/

##Control 2 motor robot script
https://github.com/chojayr/Pi-dro

##Servo Driver board wiring
http://www.lediouris.net/RaspberryPI/servo/readme.html
The chip needs 3v, the motor uses 5v, can power the motors from the pi as we don't use them much

##Servo python scripts from adafruit
https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview

##DC Motor scripts from adafruit
https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors
https://learn.adafruit.com/micropython-hardware-pca9685-dc-motor-and-stepper-driver/software

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
export LD_LIBRARY_PATH=/usr/local/lib  
mjpg_streamer -i "input_file.so -f /tmp/stream -n pic.jpg" -o "output_http.so -w /usr/local/www"

##Motion WebCamera Server setup
https://www.raspberrypi.org/forums/viewtopic.php?f=43&t=44966&start=350

Following this instructions made motion working on a latest released jessie on rpi2:

sudo apt-get install -y libjpeg-dev libavformat56 libavformat-dev libavcodec56 libavcodec-dev libavutil54 libavutil-dev libc6-dev zlib1g-dev libmysqlclient18 libmysqlclient-dev libpq5 libpq-dev

wget https://www.dropbox.com/s/6ruqgv1h65zufr6/motion-mmal-lowflyerUK-20151114.tar.gz

tar -zxvf motion-mmal-lowflyerUK-20151114.tar.gz
./motion -c motion-mmalcam-both.conf


