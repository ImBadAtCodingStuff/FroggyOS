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
                print("button LEFT_DPAD pressed...")
            if controller1.get_hat(0) == (1, 0):
                print("button RIGHT_DPAD pressed...")
            if controller1.get_hat(0) == (0, -1):
                print("button DOWN_DPAD pressed...")
            if controller1.get_hat(0) == (0, 1):
                print("button UP_DPAD pressed...")
             
            
        # get Joystick pos
        if event.type == myInput.JOYAXISMOTION:  # Joystick
            #print(myInput.joystick.Joystick(0).get_axis(0))
            
            if controller1.get_axis(0) >= 0.5:
                print ("right has been pressed")    
            if controller1.get_axis(0) <= -1:
                print ("left has been pressed")      
            if controller1.get_axis(1) >= 0.5:
                print ("Down has been pressed")  
            if controller1.get_axis(1) <= -1:
                print ("Up has been pressed") 
                
                #print("Joystick Moved")
        
        # getting simple button presses
        if event.type == myInput.JOYBUTTONDOWN:
            #print(event)
            
            # get ABXY buttons
            if controller1.get_button(0):
                print("button A pressed...")
            if controller1.get_button(1):
                print("button B pressed...")
            if controller1.get_button(4):
                print("button Y pressed...")            
            if controller1.get_button(3):
                print("button X pressed...")
                
            # get pause, select and XBOX_LOGO buttons
            if controller1.get_button(12):
                print("button XBOX_LOGO pressed...")
            if controller1.get_button(11):
                print("button PAUSE pressed...")
            if controller1.get_button(10):
                print("button SELECT pressed...")
                
            # get stick press in buttons
            if controller1.get_button(13):
                print("button LEFT_STICK_IN pressed...")
            if controller1.get_button(14):
                print("button RIGHT_STICK_IN pressed...")
            
                
                
            # Handle joystick hotswapping
#        if event.type == JOYDEVICEREMOVED:
#           Joysticks = [myInput.joystick.Joystick(x) for x in range(myInput.joystick.get_count())]
#        if event.type == JOYDEVICEADDED:
#           Joysticks = [myInput.joystick.Joystick(x) for x in range(myInput.joystick.get_count())]
#           for Joystick in Joysticks:
#                print(Joystick.get_name())
            
            