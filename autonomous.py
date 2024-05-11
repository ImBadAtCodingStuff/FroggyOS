from PIL import Image
import numpy as np

import Drivetrain.turn as turn
import getImage
import Globals
import cv2



##################################### camera config
# What port is the camera on?
USB_CAMERA = 0


cam = cv2.VideoCapture(USB_CAMERA)

# Set the resolution to 640x480
cam.set(3, 640)
cam.set(4, 480)

cv2.namedWindow("USB Camera Feed")

img_counter = 0
####################################


# keep car centered in the lines

# only track center left line


def get_lane_pos(frame):

    # Convert the image to RGB if it's not
    frame = frame.convert('RGB')

    # Convert the image to a NumPy array
    frame_array = np.array(frame)

    # Define the range for yellow color
    # These values can be adjusted depending on the shade of yellow
    yellow_min = np.array([200, 200, 0], np.uint8)
    yellow_max = np.array([255, 255, 150], np.uint8)

    # Find yellow pixels
    yellow_pixels = np.where(
        (frame_array[:, :, 0] >= yellow_min[0]) & (frame_array[:, :, 0] <= yellow_max[0]) &
        (frame_array[:, :, 1] >= yellow_min[1]) & (frame_array[:, :, 1] <= yellow_max[1]) &
        (frame_array[:, :, 2] >= yellow_min[2]) & (frame_array[:, :, 2] <= yellow_max[2])
    )

    # Calculate the average position of yellow pixels
    average_position = np.mean(yellow_pixels, axis=1)

    # change average pixel color to red
    # for pixel in image_data:


    print(f'Average position of yellow pixels: {average_position}')
    return average_position[0]

def autoTick():
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        print("break condition...")
    # Flip the frame horizontally
    frame = cv2.flip(frame, 0)
    frame = cv2.flip(frame, 1)
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        print("break condition")
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
