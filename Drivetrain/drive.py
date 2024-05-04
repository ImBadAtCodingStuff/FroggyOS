# a subdirectory for controlling subsystems

from gpiozero import Motor
from time import sleep

in1 = 22  # Input 1
in2 = 23  # Input 2
en = 27   # Enable (PWM)

# Create a motor object
motor = Motor(forward=in1, backward=in2, enable=en)
#reverse_motor = Motor(forward=in2, backward=in1, enable=en)


# controls the servo to turn the fron tires
def turn():
    pass

# sets the motor voltage to positive 1/whatever voltage is a good speed
def forward(speed, m=motor):
    
    if (speed<.1):
        m.forward(speed+.1)
    else:
        m.forward(speed)

# sets the motor voltage to negative 1/whatever voltage is a good speed
def reverse(speed, m=motor):
    
    # Note to future Evan White 
    #                                   Look up GPIO OutputDevice that should do the trick here
    
    print(speed)
    if (speed<.1):
        print("adding")
        m.backward(speed+.1)
    else:
        print("not adding")
        m.backward(speed)
    
def stop_motor(m=motor):
    m.stop()
