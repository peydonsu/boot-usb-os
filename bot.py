import playsound3 as playsound
from tkinter import messagebox as x

def media_tools():
    playsound.playsound("Windows Background.wav")
    print("loading...")

    playsound.playsound("Windows Foreground.wav")
    print("fail")
    
def usb_menu():
    playsound.playsound("Ring09.wav")
    print("opening.")
    print("opening..")
    print("opening...")
    x.showinfo("USB Drive", "Hello")
    x.showinfo("USB Drive", "Welcome to my file manager")