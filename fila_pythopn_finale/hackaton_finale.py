import PIL
import os, sys
import tkinter  as tk
from PIL import Image, ImageTk
import cv2
import time
import RPi.GPIO as GPIO

window = tk.Tk()
window.title("Join")
window.geometry('{0}x{1}+0+0' .format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(background='grey')

# open video source (by default this will try to open the computer webcam)
global avanti, indietro, filt_num, label_text, path, pathold, delay, img
filt_num = 4
avanti = 1
#self.vid = MyVideoCapture(self.video_source)
indietro = 2              
# Create a canvas that can fit the above video source size
path = "1.png"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

#The Pack geometry manager packs widgets in rows or columns.

#myimmagine = Image.open("/home/pi/Desktop/hackaton/page_1.jpg")
#image1 = ImageTk.PhotoImage(file = "/home/pi/Desktop/hackaton/page_1.jpg" )
#self.canvas.create_image(1, 1, image = image1)
#print (self.window.winfo_screenwidth(), self.window.winfo_screenheight())
##print(image1)



# Button that lets the user take a snapshot
# self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
# self.btn_snapshot.grid(row=1, column=2)

# Snapshot label
#snap_lab = tkinter.Label(window,textvariable=label_text, width=50)
#snap_lab.grid(row=1, column=2)

# Button setup    
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# After it is called once, the update method will be automatically called every delay milliseconds
delay = 5
pathold = "1.png"

def update():
    # RESIZE
    global avanti, indietro, filt_num, label_text, path, pathold, delay, img
    inputValue = GPIO.input(18)
    if (inputValue == False):
        # time.sleep(1)
        print("18")
        time.sleep(1)
        path = "1.png"

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
        
    inputValue = GPIO.input(23)
    if (inputValue == False):
        # time.sleep(1)
        print("23")
        time.sleep(1)
        path = "2.png"

        #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    if (path  != pathold):
        img = ImageTk.PhotoImage(Image.open(path))
        panel.config(image = img)

        #window.update_idletasks()
        pathold = path
        
    window.after(delay, update)
        
update()
window.mainloop()
                


                         









