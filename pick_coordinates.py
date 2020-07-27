from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

#setting up a tkinter canvas with scrollbars
c = []
def pick(videofile) : 

    root = Tk()
    # top left top right -- buttom left  bottom right center 
    print ("\n \n ----------------------------------------------------------------------------------------------------------------------")
    print("Click on these positions on the image with this specific order : ")
    print("1- Top Left corner \n 2- Top right \n 3- Buttom Left \n 4- Buttom Right \n 5- Center")
    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)
   # frame.parent.geometry(500,500)
    getFirstFrame(videofile)
        #adding the image
    img= cv2.imread("first_frame.jpg")
    
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
   # File = filedialog.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    img = ImageTk.PhotoImage(im_pil)
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

        #function to be called when mouse is clicked
    def printcoords(event):
            #outputting x and y coords to console
        d = [event.x,event.y]
        print (d)
        c.append(d)
        
        if (len(c)>= 5 ):
            root.destroy()
        #mouseclick event
        
    canvas.bind("<Button 1>",printcoords)


    root.mainloop()
    return c
    
    
def getFirstFrame(videofile):
    vidcap = cv2.VideoCapture(videofile)
    success, image = vidcap.read()
    if success:
         cv2.imwrite("first_frame.jpg", image)  # save frame as JPEG file
    else :
        print("dasdasdasdasd")
        
        
        
