from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1) # autofocus

print("start streaming")

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    image = frame.array # get the new frame array in order to display it 

    cv2.imshow("Frame", image) # add the new image on the display window

    rawCapture.truncate(0)

    if (cv2.waitKey(1) & 0xFF) == ord("q"):     # if key press 'q' is detect (on the running stream window)
        break

