from cv2 import *

cam_port = 0
cam = VideoCapture(cam_port)

result, image = cam.read()

if result:
    imshow("image is here", image)
    imwrite("thisisimage.png", image)
    
else:
    print("No image detected. Please try again!")