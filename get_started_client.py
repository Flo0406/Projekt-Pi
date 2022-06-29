#----------------------------------------------------------------------------------------------#
#Version    : 1.0
#Date       : 29.06.2022
#Description: Use this script to install and create the required packages and paths 
#             for the Client Raspberry Pi
#----------------------------------------------------------------------------------------------#

from os import system
from time import sleep

# ------------------------------- raspi-config settings -------------------------------#

system("sudo raspi-config nonint do_change_timezone Europe/Berlin")  # time zone
system("sudo passwd pi")  # change password

# -------------------------------  update & upgrade -------------------------------#

system("sudo apt-get update -y")
system("sudo apt-get upgrade -y")

# -------------------------------  install neccessary packages -------------------------------#

list_apt_install = (
    "python3-pip",  # version:  # 18.1 python 3.7
    "git",
)
list_pip_install = (
    "picamera",
    "Adafruit_DHT",
)
# list to string
list_apt_install = " ".join(list_apt_install)
list_pip_install = " ".join(list_pip_install)

# install all packages
system("sudo apt-get install %s -y" % list_apt_install)
system("sudo pip3 install %s" % list_pip_install)

# -------------------------------  download files  -------------------------------#

system("git clone --branch Client https://github.com/Flo0406/Projekt-Pi")
system("sudo mv /home/pi/Projekt-Pi/Cameraclient.py /home/pi")

# -------------------------------  final reboot -------------------------------#

duration_now = 5

while duration_now >= 0:

    min, sec = divmod(duration_now, 1000)

    print("Everything is done. Reboot in %d" % sec, end="\r")
    sleep(1)
    duration_now -= 1

print("\nReboot now")
system("sudo reboot")
