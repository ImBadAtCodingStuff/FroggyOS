import tkinter as tk
import socket

Froggy_MAC = ""



def select_button(button):
    con_button.config(bg='SystemButtonFace')
    auto_button.config(bg='SystemButtonFace')
    button.config(bg='yellow')

def con_function():
    print("Controller")

def auto_function():
    print("Autonomous")

def connect():
    menu_button.destroy()
    print(f"\n\nserching for MAC:{Froggy_MAC}\n\n")
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    try:
        server.bind((Froggy_MAC, 4))
        server.listen(1)
        # allow connection to server
        client, addr = server.accept()
    except:
        print("unable to find that MAC address\n\n")
        

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
