from PIL import Image
import numpy as np

import Drivetrain.turn as turn
import getImage
import Globals


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
    # get current frame from camera
    frame = getImage.get_frame()

    # get location in lane based on center line
    lane_pos = get_lane_pos(frame)

    # steer based on lane location
    if lane_pos > Globals.AUTO_CALIBRATION and lane_pos < Globals.AUTO_CALIBRATION + Globals.CENTER_WIDTH:
        # reset servo
        turn.turn_reset()

    else:
        if lane_pos < Globals.AUTO_CALIBRATION:
            # steer left
            turn.turn_angle(-Globals.ADJUST_SENSITIVITY)

        if lane_pos > Globals.AUTO_CALIBRATION:
            # steer right
            turn.turn_angle(Globals.ADJUST_SENSITIVITY)

