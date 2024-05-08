import cv2

# What port is the camera on?
USB_CAMERA = 0


cam = cv2.VideoCapture(USB_CAMERA)

# Set the resolution to 640x480
cam.set(3, 640)
cam.set(4, 480)

cv2.namedWindow("USB Camera Feed")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    # Flip the frame horizontally
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
