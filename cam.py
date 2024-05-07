from cv2 import *

#cam_port = 0
#cam = VideoCapture(cam_port)

def take_image():
    
    cam_port = 0
    cam = VideoCapture(cam_port)

    result, image = cam.read()

    if result:
        imwrite("thisisimage.png", image)
        
    else:
        print("No image detected. Please try again!")