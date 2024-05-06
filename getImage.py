def get_frame():
    import cv2
    import Globals


    cam = cv2.VideoCapture(Globals.USB_CAMERA)

    # Set the resolution to 640x480
    cam.set(3, Globals.CAM_RES_X)
    cam.set(4, Globals.CAM_RES_Y)

    #cv2.namedWindow("USB Camera Feed")




    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    # Flip the frame horizontally
    frame = cv2.flip(frame, 0)

    return frame