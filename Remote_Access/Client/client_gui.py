import tkinter as tk
import socket
from time import sleep

# froggy default gateway
Froggy_DFGW = "10.42.0.1"

# socket setup
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def select_button(button):
    con_button.config(bg='SystemButtonFace')
    auto_button.config(bg='SystemButtonFace')
    button.config(bg='yellow')

def con_function():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientsocket.connect(('10.42.0.1', 701))
    except:
        print("unable to find that default gateway address...\n\n")
        print("trying again in 5 seconds...\n\n")
        sleep(5)
        connect()
    print("Controller")
    string = "mode = controller"
    encoded = string.encode('utf-8')
    clientsocket.send(encoded)
    clientsocket.close()

def auto_function():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        clientsocket.connect(('10.42.0.1', 701))
    except:
        print("unable to find that default gateway address...\n\n")
        print("trying again in 5 seconds...\n\n")
        sleep(5)
        connect()
    print("Autonomous")
    string = "mode = autonomous"
    encoded = string.encode('utf-8')
    clientsocket.send(encoded)
    clientsocket.close()

def connect():
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    menu_button.destroy()
    print(f"\n\nserching for FROGGY_DFGW at: {Froggy_DFGW}\n\n")
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        clientsocket.connect(('10.42.0.1', 701))
    except:
        print("unable to find that default gateway address...\n\n")
        print("trying again in 5 seconds...\n\n")
        sleep(5)
        connect()
    clientsocket.close()
        

    # pack selection buttons onto window
    con_button.pack(side='left', padx=10)

    auto_button.pack(side='left', padx=10)



root = tk.Tk()
root.geometry('500x200')

frame = tk.Frame(root)
frame.pack()

# define config for controller selection
con_button = tk.Button(frame, text="Controller", command=lambda: [select_button(con_button), con_function()], width=15, height=5)

# define config for auto slection
auto_button = tk.Button(frame, text="Autonomous", command=lambda: [select_button(auto_button), auto_function()], width=15, height=5)


menu_button = tk.Button(frame, text="Connect", command=lambda: [select_button(menu_button), connect()], width=15, height=5)
menu_button.pack(side='left', padx=10)


root.mainloop()
