import Drivetrain.turn as turn
import Drivetrain.drive as drivetrain
#import cam as cameraa
from time import sleep
import autonomous

# Example
#Drivetrain.forward(1)
#sleep(2)
#Drivetrain.forward(0)

# controls
import pygame as myInput
import os
import threading
import socket


# current mode (this will change throughout live operation)
current_mode = ''



# fresh start
os.system("clear")

# wait for delay in controller connection
sleep(2)

#################################################### init joystick config
myInput.joystick.init()
print("Found "+str(myInput.joystick.get_count())+" controllers...")
Joysticks = [myInput.joystick.Joystick(x) for x in range(myInput.joystick.get_count())]

myInput.init()
#####################################################

def Listen_to_socket():
    global current_mode
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('10.42.0.1', 701))
    serversocket.listen(1) # become a server socket, maximum 1 connections

    while True:
        #print("hello world")
        connection, address = serversocket.accept()
        buf = connection.recv(64)
        if len(buf) > 0:
            decoded = buf.decode('utf-8')
            print (decoded)
            print(address[0])
            
            # check the incomming packet
            if decoded == '':
                print('nothing in packet')

            if decoded == 'mode = controller':
                current_mode = 'mode = controller'

            if decoded == 'mode = autonomous':
                current_mode = 'mode = autonomous'
        else:
            print("nothing in buffer...")

def AUTONOMOUS():
    print("autonomous was selected just now")
    autonomous.autoTick()

def CONTROLLER():
    '''
    for event in myInput.event.get():
        
        #print(event)
        
        #print(str(myInput.joystick.Joystick(0).get_hat()))
        
        controller1 = myInput.joystick.Joystick(0)
        
        if event.type == myInput.JOYHATMOTION:

            if controller1.get_hat(0) == (-1, 0):
                #print("button LEFT_DPAD pressed...")
                #turn.turn_angle(-1)
                pass
            if controller1.get_hat(0) == (1, 0):
                #print("button RIGHT_DPAD pressed...")
                #turn.turn_angle(1)
                pass
            if controller1.get_hat(0) == (0, -1):
                #print("button DOWN_DPAD pressed...")
                #turn.turn_angle(0)
                pass
            if controller1.get_hat(0) == (0, 1):
                #print("button UP_DPAD pressed...")
                pass
            
            
        # get Joystick pos
        if event.type == myInput.JOYAXISMOTION:  # Joystick
            #print(myInput.joystick.Joystick(0).get_axis(0))
            
            CJAMS_hor = controller1.get_axis(0)
            CJAMS_ver = controller1.get_axis(1)
            #print(CJAMS_hor)
            turn.turn_angle(-CJAMS_hor+.10)
            # Reset state
            if CJAMS_hor <= 0.4 and CJAMS_hor >= -0.4 and CJAMS_ver <= 0.4 and CJAMS_ver >= -0.4:
                turn.turn_reset()
                
            # Getting trigger inputs   
            if event.type == myInput.JOYAXISMOTION:
                
                RIGHT_TRIGGER = controller1.get_axis(4)
                LEFT_TRIGGER = controller1.get_axis(5)
                
                forward_drive = RIGHT_TRIGGER*.5+.5
                reverse_drive = LEFT_TRIGGER*.5+.5
                
                if (forward_drive>0):
                    #print("forward")
                    # default to forward
                
                    #print(drive_speed)
                    if forward_drive>0:
                        drivetrain.forward(forward_drive)
                    else:
                        pass
                
                elif (reverse_drive>0):
                    print("reverse") 
                    # default to reverse
                    if reverse_drive>0:
                        drivetrain.reverse(reverse_drive)
                        
                    else:
                        pass
                        #.578
                else:
                        print("nothing pressed")
                        drivetrain.stop_motor()
                
                #print("yipeee")
                
        
        # getting simple button presses
        if event.type == myInput.JOYBUTTONDOWN:
            #print(event)
            
            # get ABXY buttons
            if controller1.get_button(0):
                #print("button A pressed...")
                #Drivetrain.forward(1)
                pass
            if controller1.get_button(1):
                #print("button B pressed...")
                pass
            if controller1.get_button(4):
                #print("button Y pressed...") 
                #image_capture()     
                pass
            if controller1.get_button(3):
                #print("button X pressed...")
                pass
                
            # get pause, select and XBOX_LOGO buttons
            if controller1.get_button(12):
                #print("button XBOX_LOGO pressed...")
                pass
            if controller1.get_button(11):
                #print("button PAUSE pressed...")
                pass
            if controller1.get_button(10):
                #print("button SELECT pressed...")
                pass
                
            # get stick press in buttons
            if controller1.get_button(13):
                #print("button LEFT_STICK_IN pressed...")
                pass
            if controller1.get_button(14):
                #print("button RIGHT_STICK_IN pressed...")
                pass
                
        # getting simple button presses
        if event.type == myInput.JOYBUTTONUP:
            #print(event)
            
            # get ABXY buttons
            if event.button == 0:
                #print("button A unPressed...")
                Drivetrain.forward(0)
            if event.button == 0:
                #print("button B unPressed...")
                pass
            if event.button == 0:
                #print("button Y unPressed...") 
                pass           
            if event.button == 0:
                #print("button X unPressed...")
                pass
                
            # get pause, select and XBOX_LOGO buttons
            if event.button == 0:
                #print("button XBOX_LOGO unPressed...")
                pass
            if event.button == 0:
                #print("button PAUSE unPressed...")
                pass
            if event.button == 0:
                #print("button SELECT unPressed...")
                pass
                
            # get stick press in buttons
            if event.button == 0:
                #print("button LEFT_STICK_IN unPressed...")
                pass
            if event.button == 0:
                #print("button RIGHT_STICK_IN unPressed...")
                pass
        '''

# break out thread for checking current state
listen_thread = threading.Thread(target=Listen_to_socket)
listen_thread.start()


while True:
    #print("llllllllllllllllllll")
    if current_mode == '':
        pass
    if current_mode == 'mode = controller':
        CONTROLLER()
    if current_mode == 'mode = autonomous':
        AUTONOMOUS()

