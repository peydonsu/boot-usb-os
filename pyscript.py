import os as Windows
import cv2
from tkinter import messagebox as x
import playsound3 as playsound

def dll():
    img = cv2.imread("image.png")
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def messageInfo(title, str):
    x.showinfo(title, str)
    playsound.playsound("Alarm01.wav")
    
def messageWarning(title, str):
    x.showwarning(title, str)