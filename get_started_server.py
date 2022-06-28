from os import mkdir, system
from time import sleep
# -------------------------------  settings -------------------------------#

system("sudo raspi-config nonint do_change_timezone Europe/Berlin") # time zone
system("sudo passwd pi") # change password

# -------------------------------  update & upgrade -------------------------------#

system("sudo apt-get update ")
system("sudo apt-get upgrade")

# -------------------------------  install neccessary packages -------------------------------#

list_apt_install = (        # version:
    "apache2",              # 2.4.38 (Raspbian)
    "php",                  # 7.3.31-1~deb10u1
    "libapache2-mod-php",
    "gpac",                 # GPAC version 0.5.2-DEV-revVersion: 0.5.2-426-gc5ad4e4+dfsg5-5
    "python3-pip",          # 18.1 python 3.7
    "libopenjp2-7",         
    "libtiff5",             
    "libatlas-base-dev",    
)
list_pip_install = (
    "pillow",
    "telepot",
)
# list to string
list_apt_install = " ".join(list_apt_install)
list_pip_install = " ".join(list_pip_install)
# install all packages
system("sudo apt-get install %s -y" % list_apt_install)
system("sudo pip3 install %s" % list_pip_install)

# -------------------------------  create folder structure -------------------------------#

input_correct = False

while input_correct is False:

    inp = int(input("How many camera slots are required ? [1 - 4] "))

    if 0 < inp < 5:
        input_correct = True
    else:
        print("Wrong input. Try again!")

# directory and subdirectory
folder_name_camera = r"/home/pi/CAM"
folder_name_video = r"/Video"
folder_name_image = r"/Images"
folder_name_image_telegram = r"/TelegramImages"
folder_name_measurements = r"/Measurements"
folder_name_measurements_humidity = r"/Humidity"
folder_name_measurements_temperature = r"/Temperature"

# create for every camera client a folderstructure
for i in range(1, inp + 1, 1):

    folder_name = folder_name_camera + str(i)
    mkdir(folder_name)
    folder_name += folder_name_image
    mkdir(folder_name)
    folder_name += folder_name_image_telegram
    mkdir(folder_name)
    folder_name = folder_name_camera + str(i) + folder_name_video
    mkdir(folder_name)
    folder_name = folder_name_camera + str(i) + folder_name_measurements
    mkdir(folder_name)
    folder_name = (
        folder_name_camera
        + str(i)
        + folder_name_measurements
        + folder_name_measurements_humidity
    )
    mkdir(folder_name)
    folder_name = (
        folder_name_camera
        + str(i)
        + folder_name_measurements
        + folder_name_measurements_temperature
    )
    mkdir(folder_name)

# -------------------------------  download files  -------------------------------#
system("git clone --branch Server https://github.com/Flo0406/Projekt-Pi")

system("sudo mv /home/pi/Projekt-Pi/server.php /var/www/html/")
system("sudo mv /home/pi/Projekt-Pi/stylesheet.css /var/www/html/")
system("sudo mv /home/pi/Projekt-Pi/Cameraserver.py /home/pi")
system("sudo mv /home/pi/Projekt-Pi/webserver.py /home/pi") 
# -------------------------------  change rights -------------------------------#
system("sudo chown www-data:www-data server.php stylesheet.css")
# -------------------------------  cronjob  -------------------------------#

# -------------------------------  final reboot -------------------------------#

duration_now = 5

while duration_now >= 0 :

    min, sec = divmod(duration_now, 1000)
 
    print("Everything is finished. Reboot in %d" %sec,end="\r")
    sleep(1)
    duration_now -= 1

print("\nReboot now")
system("sudo reboot")
