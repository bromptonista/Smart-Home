# Original from https://gist.github.com/mmoyer2655
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import ftplib
import os

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        os.system ("fswebcam --delay 1.5 -r 1920x1080 -S 20  --scale 960x540  --rotate 270 inourfri$
        sftp = ftplib.FTP('HOST','USER','PASSWORD') # Connect
        fp = open('inourfridge.jpg') # file to send
        sftp.storbinary('STOR inourfridge.jpg', fp) # Send the file
        fp.close() # Close file and FTP
        sftp.quit()
        time.sleep(30)
