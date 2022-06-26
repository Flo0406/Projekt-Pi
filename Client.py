import socket
import time
import os
import base64
import Adafruit_DHT
from picamera import PiCamera
from datetime import datetime


host = ""  # ipaddress of the host here enter your own ip
port = ""  # same port as host

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


def Temperature():
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 2
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temp = str(round(temperature, 2))
    hum = str(round(humidity, 2))
    s.send(str.encode(temp + "#" + hum))


def Image():  # take an image, send size of the image, send image
    camera = PiCamera(  # take a picture
        resolution=(1920, 1080),  # resolution of image
        framerate=30,  # picture per second
    )
    camera.capture("CAM1.jpg", use_video_port=True)  # save image under CAM1.png
    camera.close()
    imagefile = open("CAM1.jpg", "rb")  # open and read image binary
    imagedata = imagefile.read()
    size = str.encode(str(len(imagedata)))  # calculate size of image
    print("Size of Image:" + str(size))
    s.send(size)  # send size to server
    reply = s.recv(1024)  # wait for reply of the server, so we can send the image
    message = reply.decode("utf-8")
    print(message)
    if message == "ok":  # when server send 'ok', send the image
        s.send(imagedata)
        imagefile.close()


def Video(duration):  # do a video, send size of video, send video
    duration = duration  # duration is given by server message
    duration_now = 0  # duration start with 0
    clearance = 1
    file_name_format = "{:s}.{:s}"  # file format
    folder_name_video = r"/home/pi/"  # save video in home/pi
    file_type_video = r"h264"
    file_name_video = folder_name_video + file_name_format.format(
        "Video", file_type_video
    )  # save as video.h264

    camera = PiCamera(
        resolution=(1280, 720),  # resolution of video
        framerate=30,  # picture per minute
    )

    camera.start_recording(file_name_video)

    while (
        duration_now < duration
    ):  # do this till actual duration ist the given duration
        sec, milsec = divmod(duration_now, 1000)
        timer = "{:2d}{:3d}".format(sec, milsec)

        print(timer, end="\r")
        time.sleep(clearance)
        duration_now += 1

    # Aufnahme stoppen und Kameramodul schliessen
    camera.stop_recording()
    camera.close()

    videofile = open("Video.h264", "rb")  # open and read Video.h264 binary
    videodata = videofile.read()
    size = str.encode(str(len(videodata)))  # calculate size of video
    print(size)
    s.send(size)  # send size to server
    reply = s.recv(1024)  # wait for replay
    message = reply.decode("utf-8")
    print(message)
    if message == "ok":  # when server send 'ok', we know we can send video
        s.send(videodata)  # send video
        videofile.close()


while True:
    reply = s.recv(1024)  # wait for message from server
    if reply:
        message = reply.decode("utf-8")  # decode message
        print(message)
        wish = message.split(
            "#", 3
        )  # split the message, which is separated with hastag
        print(wish)
        if wish[1] == "1":  # when second sign is '1' cameraclient 1 should do something
            if (
                wish[2] == "pic"
            ):  # when second sign is 'pic' call function to send image
                print("PIC")
                Image()
            elif wish[2] == "temp":
                Temperature()
            else:  # when third sign isnt 'pic' it is the duration
                Video(int(wish[2]))  # call videofunction and give duration

s.close()
