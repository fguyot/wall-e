# Configuration and setup


## Additionnal step, : 

- Configure SSH 
- Need to update specific package of openCV for raspberry : pip3 install opencv-python==3.4.6.27
- Get the visual feedback from the camera using VNC require to change settings : on pi -> VNC options -> troubleshooting -> Enable direct capture mode

## Sources : 
Initial walle project : https://github.com/chillibasket/walle-replica/blob/master/wall-e/wall-e.ino
Configuration of OPENCV : https://www.framboise314.fr/i-a-realisez-un-systeme-de-reconnaissance-dobjets-avec-raspberry-pi/ 
Face recognition : https://www.pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/

## Notes 
 WARNING: The scripts face_detection and face_recognition are installed in '/home/pi/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
