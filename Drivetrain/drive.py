
# a subdirectory for controlling subsystems



# controls the servo to turn the fron tires
def turn():
    pass

# sets the motor voltage to positive 1/whatever voltage is a good speed
def forward(speed):
    # set the motor speed to 1
    print("Driving forward at speed: " + str(speed * .5 + .5))
    if speed == 0:
        print("Stopping...")

# sets the motor voltage to negative 1/whatever voltage is a good speed
def reverse():
    # set motor speed to -1
    pass
