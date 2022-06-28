import socket
import base64
import io
import os
import time
import glob
import requests
import telepot #telegram bot
from telepot.loop import MessageLoop
from datetime import datetime
from io import BytesIO
from PIL import Image, ImageFile
from shutil import copyfile



host = '' #this is the server
port = your port # port that is used for this connection
size = 0

token = "token of your selfmade bot" #token from bot
chatid = your chatid #chatid of my telegram

# Telepot Settings
bot = telepot.Bot(token)
bot.getMe()
bot.getUpdates()


def setupServer(): #this function creates a socket using the internet
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#makes sure we dont get "address already used" error
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection(): #this function set up the connection to the client
    s.listen(3) # Allows one connection at a time.
    conn, address = s.accept() #accept the client
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def GETSIZE(conn): # this function return the size of the data that we will receive
    data = conn.recv(1024) # receive the data
    size = data.decode('utf-8') #decode
    conn.sendall(str.encode('ok')) #send 'ok' because we are ready to receive the big data
    print(size)
    size = int(size)
    return size
    
def imageTransfer(conn, size, cam): #this function is used to receive and save images
    now = datetime.now()
    currenttime = now.strftime("%Y%m%d%H%M%S")
    picturename = currenttime + "Picture.jpg" # name is build from Year,Month,Day,Hour,Minute,Second
    print(picturename)
    ImageFile.LOAD_TRUNCATED_IMAGES = True # need to prevent from "truncated" error
    imagedata = conn.recv(2048) #receive imagedata
    data = imagedata
    if imagedata: 
        while imagedata: # while we receive data do this
            imagedata = conn.recv(2048)
            #print(len(imagedata))
            data += imagedata # add received data to data store
            if len(data) == size:
                break
    image = Image.open(io.BytesIO(data)) # put data into image
    image.save(picturename) #save Image with given picturename
    image.save('CAM'+str(cam)+'.jpg')
    os.system('mv /home/pi/'+picturename+' /home/pi/CAM'+str(cam)+'/Images/')#move picture to provided directory
    os.system('sudo mv /home/pi/CAM'+str(cam)+'.jpg /home/pi/CAM'+str(cam)+'/Images/')#move picture to provided directory
    print("Image saved")
    folder = '/home/pi/CAM'+str(cam)+'/Images/'
    dirlist = os.listdir(folder)
    numberofimages = len(dirlist)
    if numberofimages == 10:
        print(numberofimages)
        dirName = '/home/pi/CAM'+str(cam)+'/Images' # + camera + '/photos'
        listOfFiles = sorted(filter (lambda x: os.path.isfile(os.path.join(dirName, x)), os.listdir(dirName)))
        os.remove('/home/pi/CAM'+str(cam)+'/Images/'+listOfFiles[0])


def videoTransfer(conn, size, cam): #this function is used to receive and save videos
    global noimage    
    now = datetime.now()
    currenttime = now.strftime("%Y%m%d%H%M%S")
    videoname = currenttime + "Video.mp4" # name is build from Year,Month,Day,Hour,Minute,Second
    print(videoname)
    videodata = conn.recv(4096)
    data = videodata   
    if videodata:
        while len(data)<size: # as long as data is not the expected size do this
            videodata = conn.recv(4096)
            print("bytes benoetigt: %d" %int(size)+"\t empfangen bytes: %d" %len(data), end="\r") # print how much we received
            data += videodata #add received data to datastore
            if len(data) == size:
                print("done")
                break
    video = open('video.h264','wb')#save video in h264 format 
    video.write(data)
    video.close() 
    os.system('MP4Box -fps 30 -add video.h264 '+videoname) # convert h264 in mp4 and save with correct name
    print("Video saved")
    os.system('mv /home/pi/'+videoname+' /home/pi/CAM'+str(cam)+'/Videos/')#move picture to provided directory
    noimage = False

def getTemp(cam):
    global connection
    conn = connection[cam-1]
    conn.sendall(str.encode('Cam#'+str(cam)+'#temp'))
    measure = conn.recv(4096)
    measure = measure.decode('utf-8')
    measure = measure.split('#', 2)
    temperature = measure[0]
    humidity = measure[1]
    temp = open('/home/pi/CAM'+str(cam)+'/Measurements/tempcam'+str(cam)+'.txt','w')
    temp.write(temperature)
    hum = open('/home/pi/CAM'+str(cam)+'/Measurements/humcam'+str(cam)+'.txt','w')
    hum.write(humidity)

    print(temperature)

def getVideo(cam, length): #this function is called to ask clients for a "length"long video
    global connection
    global noimage
    noimage = True
    conn = connection[cam-1]
    conn.sendall(str.encode('Cam#'+str(cam)+'#'+str(length))) # send message to all clients 
    size = GETSIZE(conn) # first call GETSIZE
    if size > 0: # when we received a size call videoTransfer
        videoTransfer(conn, size, cam)
        size = 0

def getImage(cam): #this function is called to ask clients for a Image
    global connection
    conn = connection[cam-1]
    conn.sendall(str.encode('Cam#'+str(cam)+'#pic')) # send message to all clients
    size = GETSIZE(conn) # first call GETSIZE
    if size > 0: # when we received a size call imageTransfer
        imageTransfer(conn, size, cam) 
        size = 0

def handle(msg):
    global fileBuffer
    global newPhoto
    global cam

    message=msg['text']
    
    if fileBuffer and message.lower() != "ja":
        fileBuffer = False
        bot.sendMessage(chatid, "Das Bild wurde nicht gespeichert.")

    if message.lower() == "/start" :
        bot.sendMessage(chatid, 'Die Sicherheitsueberwachung wurde gestartet. \nWenn ein aktuelles Bild einer Kamera geschickt werden soll, antworten Sie mit \"/Kamera*zahl*\". \nSoll eine Aufnahme gestartet werden, antworten Sie mit \"/aufnahme*kamera*,*sekunden* (max. 20sek)\".')

    if message[0:9].lower() == "/aufnahme":

        if message[9] == '1':
            cam = 1
            startVideo(cam, message)
        elif message[9] == '2':
            cam = 2
            startVideo(cam, message)
        elif message[9] == '3':
            cam = 3
            #startVideo(cam, message)
        elif message[9] == '4':
            cam = 4
            #startVideo(cam, message)
        else:
            bot.sendMessage(chatid, 'Die Kameraeingabe ist ungueltig.')

    if message[0:7].lower() == "/kamera":
        if len(message) == 8 and int(message[7]) > 0 and int(message[7]) < 5:
            if int(message[7]) == 1:
                cam = 1
                getImage(cam)

                time.sleep(1)

                newPhoto = getNewFile()
                sendNewestPhoto(newPhoto, cam) 
                fileBuffer = True

            elif int(message[7]) == 2:
                cam = 2
                getImage(cam)

                time.sleep(1)

                newPhoto = getNewFile()
                sendNewestPhoto(newPhoto, cam) 
                fileBuffer = True

            elif int(message[7]) == 3:
                cam = 3
                getImage(cam)

                time.sleep(1)

                newPhoto = getNewFile()
                sendNewestPhoto(newPhoto, cam) # Kamera Nummer noch angeben!
                fileBuffer = True

            elif int(message[7]) == 4:
                cam = 4
                getImage(cam)

                time.sleep(1)

                newPhoto = getNewFile()
                sendNewestPhoto(newPhoto, cam) # Kamera Nummer noch angeben!
                fileBuffer = True

        else:
            bot.sendMessage(chatid, "Die angegebene Kamera existiert nicht.")

        if fileBuffer:
            bot.sendMessage(chatid, "Soll das aktuelle Bild gespeichert werden?")

    if fileBuffer and message.lower() == "ja":
        copyfile('/home/pi/CAM' + str(cam) + '/Images/' + newPhoto, '/home/pi/CAM' + str(cam) + '/Images/TelegramImages/' + newPhoto)
        fileBuffer = False
        
        bot.sendMessage(chatid, "Das Bild wurde gespeichert.")
    

def getNewFile(): # Camera + Video / Photo?
    dirName = '/home/pi/CAM' + str(cam) + '/Images' 
    listOfFiles = sorted(filter (lambda x: os.path.isfile(os.path.join(dirName, x)), os.listdir(dirName)))
    listOfFiles.reverse()
    return listOfFiles[1]
        
def sendNewestPhoto(fileName, cam): # Camera und Video / Photo ??
    document = open('/home/pi/CAM' + str(cam) + '/Images/' + fileName, 'rb') 
    bot.sendPhoto(chatid, document)

def getNewFileVideo():
    dirName = '/home/pi/CAM' + str(cam) + '/Videos'
    listOfFiles = sorted(filter (lambda x: os.path.isfile(os.path.join(dirName, x)), os.listdir(dirName)))
    listOfFiles.reverse()
    return listOfFiles[0]

def sendNewestVideo(fileName, cam):
    document = open('/home/pi/CAM' + str(cam) + '/Videos/' + fileName, 'rb')
    bot.sendVideo(chatid, document)

def startVideo(cam, message):
    # if one digit number behind command is added
        if len(message) == 12 and message[-1].isdigit():
            bot.sendMessage(chatid, 'Die Aufnahme wurde fuer ' + message[-1] + ' Sekunden gestartet. Bitte warten...')
            getVideo(cam, int(message[-1]))
            #time.sleep(int(message[-1])+2)
            time.sleep(1)
            newVideo = getNewFileVideo()
            sendNewestVideo(newVideo, cam)
        # if two digit number behind command is added
        elif len(message) == 13 and message[-2:].isdigit() and int(message[-2:]) <= 20: 
            bot.sendMessage(chatid, 'Die Aufnahme wurde fuer ' + message[-2:] + ' Sekunden gestartet. Bitte warten...')
            getVideo(cam, int(message[-2:]))
            #time.sleep(int(message[-2:])+2)
            time.sleep(1)
            newVideo = getNewFileVideo()
            sendNewestVideo(newVideo, cam)
        elif len(message) == 13 and message[-2:].isdigit() and int(message[-2:]) > 20: 
            bot.sendMessage(chatid, 'Die maximale Aufnahmezeit betraegt 20 Sekunden.')
        else:
            bot.sendMessage(chatid, 'Es wurde keine gueltige Zahl eingegeben.')

s = setupServer()
connected = False
video = False
global noimage
noimage = False

# Message loop to receive all messages
MessageLoop(bot, handle).run_as_thread()
fileBuffer = False
newPhoto = ''
cam = 0
bot.sendMessage(chatid, 'Willkommen beim Security Bot. \n Um die Sicherheitsueberwachung zu starten, geben Sie bitte \"/start\" ein.')

alreadyconnected = False
connection = []
lastTime = 0
numberofcams = 0
while True:
    if numberofcams<2:
        try:
            conn = setupConnection()
            if not conn in connection:
                connection.append(conn)
                print("new connection")
                numberofcams += 1
        
        except:
            for connections in connection:
                connections.close()
    else:
        period = datetime.now()
        if period.second % 20 == 0 and (abs(period.second - lastTime)) >= 1 and not noimage:
            print(period)
            lastTime = period.second
            for i in range(len(connection)):
                getImage(i+1)
                getTemp(i+1)
