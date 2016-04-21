import RPi.GPIO as GPIO
import time
import picamera
import datetime
#import pyimgur

#CLIENT_ID = ""
#CLIENT_SECRET = ""
#im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

#print(im.authorization_url("pin"))
#pin = raw_input("What is the pin?")
#pin = ""
#print(im.exchange_pin(pin))
#album = im.get_album("")

camera = picamera.PiCamera()
#camera.vflip = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print("Press the button to begin the countdown...")
camera.start_preview()
camera.preview.fullscreen = False
camera.preview.window = (0,0,1920,1000)

def TryUploadToImgur(fileName):
	try:
	        PATH = "/home/pi/Python_Projects/" + fileName
        	im.upload_image(PATH, album=album)
	except:
		print("Imgur is being dumb")
	return;

def PauseBetweenCaptures():
	print("3...")
	time.sleep(1)
	print("2...")
	time.sleep(1)
	print("1...")
	time.sleep(1)
	return;

while True:
	input_state = GPIO.input(18)
	if input_state == False:
		#input = raw_input("Press Enter")
		current_time = datetime.datetime.now().time()
		print("First picture in...")
		PauseBetweenCaptures()
		time.sleep(1)
		firstName = current_time.isoformat() + '-1.jpg'
		camera.capture(firstName)
		#TryUploadToImgur(firstName)
		print("Second picture in...")
        	PauseBetweenCaptures()
		secondName = current_time.isoformat() + '-2.jpg'
		camera.capture(secondName)
		#TryUploadToImgur(secondName)
		print("Last picture in...")
        	PauseBetweenCaptures()
		thirdName = current_time.isoformat() + '-3.jpg'
		camera.capture(thirdName)
		#TryUploadToImgur(thirdName)
		print("Done!  Press the button to take more pictures")
		#im.refresh_access_token()

camera.stop_preview()
