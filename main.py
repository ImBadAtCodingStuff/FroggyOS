import Drivetrain.turn as turn
import Drivetrain.drive as Drivetrain
import cam as camera
from time import sleep

# Example
#Drivetrain.forward(1)
#sleep(2)
#Drivetrain.forward(0)

# controls
import pygame as myInput


myInput.joystick.init()
print(myInput.joystick.get_count())
Joysticks = [myInput.joystick.Joystick(x) for x in range(myInput.joystick.get_count())]

myInput.init()



while True:
    for event in myInput.event.get():
        
        #print(event)
        
        #print(str(myInput.joystick.Joystick(0).get_hat()))
        
        controller1 = myInput.joystick.Joystick(0)
        
        if event.type == myInput.JOYHATMOTION:
  
            if controller1.get_hat(0) == (-1, 0):
                #print("button LEFT_DPAD pressed...")
                turn.turn_angle(-1)
            if controller1.get_hat(0) == (1, 0):
                #print("button RIGHT_DPAD pressed...")
                turn.turn_angle(1)
            if controller1.get_hat(0) == (0, -1):
                #print("button DOWN_DPAD pressed...")
                turn.turn_angle(0)
            if controller1.get_hat(0) == (0, 1):
                #print("button UP_DPAD pressed...")
                pass
             
            
        # get Joystick pos
        if event.type == myInput.JOYAXISMOTION:  # Joystick
            #print(myInput.joystick.Joystick(0).get_axis(0))
            
            if controller1.get_axis(0) >= 0.5:
                #print ("right has been pressed") 
                pass   
            if controller1.get_axis(0) <= -1:
                #print ("left has been pressed")  
                pass    
            if controller1.get_axis(1) >= 0.5:
                #print ("Down has been pressed")  
                pass
            if controller1.get_axis(1) <= -1:
                #print ("Up has been pressed") 
                pass
                
                #print("Joystick Moved")
        
        # getting simple button presses
        if event.type == myInput.JOYBUTTONDOWN:
            #print(event)
            
            # get ABXY buttons
            if controller1.get_button(0):
                #print("button A pressed...")
                Drivetrain.forward(1)
            if controller1.get_button(1):
                #print("button B pressed...")
                pass
            if controller1.get_button(4):
                #print("button Y pressed...") 
                camera.take_image()     
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




