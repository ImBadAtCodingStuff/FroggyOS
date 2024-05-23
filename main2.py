import logging
import os
import socket
import pygame as myInput
from time import sleep
import autonomous
import Global_var
import multiprocessing

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a class to organize the code
class RobotController:
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.autoTickThread = None
        self.controllerThread = None
        self.existing_auto = 0
        self.existing_controller = 0
        self.init_joystick()
        self.init_server()

    def init_joystick(self):
        try:
            myInput.joystick.init()
            logging.info("Found %d controllers...", myInput.joystick.get_count())
            self.Joysticks = [myInput.joystick.Joystick(x) for x in range(myInput.joystick.get_count())]
            myInput.init()
        except Exception as e:
            logging.error("Joystick initialization failed: %s", e)
            sleep(2)
            self.init_joystick()

    def init_server(self):
        try:
            self.serversocket.bind(('10.42.0.1', 701))
            self.serversocket.listen(1)
            logging.info("Server initialized and listening")
        except Exception as e:
            logging.error("Server initialization failed: %s", e)
            self.serversocket.close()
            exit(1)

    def controller(self):
        # Controller logic here...
        pass

    def autonomous_mode(self):
        # Autonomous mode logic here...
        pass

    def run(self):
        try:
            while True:
                connection, address = self.serversocket.accept()
                buf = connection.recv(64)
                if len(buf) > 0:
                    decoded = buf.decode('utf-8')
                    logging.info("Received data from %s", address[0])
                    # Mode switching logic here...
                else:
                    logging.info("No data received.")
        except KeyboardInterrupt:
            logging.info("Shutting down gracefully...")
            self.shutdown()
        except Exception as e:
            logging.error("An error occurred: %s", e)
            self.shutdown()

    def shutdown(self):
        if self.autoTickThread:
            self.autoTickThread.terminate()
        if self.controllerThread:
            self.controllerThread.terminate()
        self.serversocket.close()
        logging.info("Shutdown complete.")

# Main execution
if __name__ == "__main__":
    robot_controller = RobotController()
    robot_controller.run()
