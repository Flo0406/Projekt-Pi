#------------------------------------------------------------------------------------------#
# Version: 1.0
# Date: 29.06.22
# Description: move pictures to html folder and change group and user to enable access for
#              the webserver
#------------------------------------------------------------------------------------------#

from os import system

for i in range(4): # move newest picture to webserver and change group and user for access
    system("cp /home/pi/CAM"+str(i+1)+"/Images/CAM"+str(i+1)+".jpg /var/www/html/")
    system("sudo chown www-data:www-data /var/www/html/CAM"+str(i+1)+".jpg")
