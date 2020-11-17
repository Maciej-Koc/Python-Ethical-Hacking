#!/usr/bin/env python

#MAC Address Changer
#Increases anonymity,impersonate other devices, bypass filters

#subprocess contains functions that allow us to execture system commands
#commands depend on the OS which executes the script
import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00::11:22:33:44:66" ,shell=True)
subprocess.call("ifconfig wlan0 up" ,shell=True)