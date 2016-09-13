#!/usr/bin/python
#Set this to run once the raspbian LXDE desktop loads
#Don't forget to: export DISPLAY=:0
#This can be set to run in .profile or .bashrc with a line like this:
#export DISPLAY=:0
#python $HOME/ipdisplay.py &


from Tkinter import *
import tkMessageBox as mbox
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl( 
    	s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    	)[20:24])

myip = get_ip_address('eth0')

root = Tk()
label = Label(root, fg="red", bg='black', text=myip, width=800, font=("Helvetica", 64))
label.pack()
label.focus_set()

button = Button(root, width=100, text="OK", command=quit)
button.pack()

root.geometry("800x480")
root.mainloop()
