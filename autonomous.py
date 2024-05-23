from PIL import Image
import numpy as np

import Drivetrain.turn as turn
import Global_var
import cv2

from time import sleep






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

#ticks = 0

def autoTick():
    USB_CAMERA = 0
    cam = cv2.VideoCapture(USB_CAMERA)
    # Set the resolution to 640x480
    cam.set(3, 640)
    cam.set(4, 480)

    #    cv2.namedWindow("USB Camera Feed")
    img_counter = 0
    while True:
            
        if Global_var.continue_auto == 'false':
            print("cancel auto")
            cam.release()
            cv2.destroyAllWindows()
            #ticks = 0
            sleep(10)
        else:
            #ticks+=1
        
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                print("break condition...")
            # Flip the frame horizontally
            frame = cv2.flip(frame, 0)
            frame = cv2.flip(frame, 1)
            cv2.imshow("USB CAMERA", frame)
            #print(ticks)

