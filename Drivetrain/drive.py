
# a subdirectory for controlling subsystems



# controls the servo to turn the fron tires
def turn():
    pass

# sets the motor voltage to positive 1/whatever voltage is a good speed
def forward(vari):
    # set the motor speed to 1
    if vari == 1:
        print("Driving forward...")
    if vari == 0:
        print("Stopping...")

# sets the motor voltage to negative 1/whatever voltage is a good speed
def reverse():
    # set motor speed to -1
    pass
