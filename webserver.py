from os import system

for i in range(4): # move newest picture to webserver
    system("cp /home/pi/CAM"+str(i+1)+"/Images/CAM"+str(i+1)+".jpg /var/www/html/")
    system("sudo chown www-data:www-data /var/www/html/CAM"+str(i+1)+".jpg")
