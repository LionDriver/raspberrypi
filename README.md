# raspberrypi
Commonly used raspberry pi scripts I've created

#ipdisplay.py
Display your current IP address full screen upon boot, be sure to update the screen geometry to fit your screen (defaults to 800x480 for a common 5" display)


## Requirments:
Raspberry pi running raspbian with latest updates (only has been tested on rpi 3 b)
TKinter python library


## Install:
clone to where you want it, if you want it to always display on GUI, do the following
Add the following to /etc/xdg/autostart/startup.desktop (create file if it doesn't exist)
[Desktop Entry]
Type=Application
Name=ip display
Exec=/home/pi/workspace/tools/ipdisplay.py &    (edit this line to match where you installed ipdisplay.py)
Terminal=false
Hidden=false
X-GNOME-Autostart-enabled=true
Comment=Display IP on start up


Also you may need to add in the following to your .profile or .bashrc file in your home directory depending on how you want to handle it:
export DISPLAY=:0



