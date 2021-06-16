from tkinter import Tk, Label, Button, Entry, Scale, HORIZONTAL, DoubleVar
import qrcode
from PIL import Image, ImageTk

def generateQRcode():
    # Link for website
    input_data = "https://www.easii-ic.com/fr/index.php"
    #Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=5,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    return img

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.geometry("600x400")
        self.attr1 = ""
        master.title("A simple GUI")

        self.label1 = Label(master, text="Enter a value in this input :", bg="#10D3D5")
        self.label1.place(x=180,y=5)
        
        #Input 
        self.varEntry = DoubleVar()
        self.entry1 = Entry(master, textvariable = self.varEntry)
        self.entry1.place(x=180,y=30)
        self.entry1.bind('<Return>', self.entryHandler)

        self.label2 = Label(master, text="This is a string with color", fg="#3300CC")
        self.label2.place(x=180,y=60)
        self.varSlider = DoubleVar() 
        self.slider =  Scale(master, from_=0.00, to=1.0,orient=HORIZONTAL, length=400, variable = self.varSlider,tickinterval=0.1, resolution=0.01, command="")
        self.slider.place(x=80,y=80)

        #qrCode
        self.QRcode = generateQRcode()
        self.img = ImageTk.PhotoImage(image = self.QRcode)
        self.labelQR = Label(master, image=self.img)
        self.labelQR.place(x=20,y=140)

        #Image
        self.img2 = ImageTk.PhotoImage(file = "easii-ic.png")
        self.labelEntr = Label(master, image=self.img2)
        self.labelEntr.place(x=300,y=140)

        #button
        self.greet_button = Button(master, text="Accept", command=self.accept, bg= "#1ED454")
        self.greet_button.place(x=20,y=350)
        self.close_button = Button(master, text="Fail", command=self.quit1, bg= "#E00A1D")
        self.close_button.place(x=550,y=350)
        

    def accept(self):
        self.attr1 = True
        self.master.quit()
    def quit1(self):
        self.attr1 = False
        self.master.quit()

    def entryHandler(self, event):
        self.master.quit()
        
def test():
    root = Tk()
    my_gui = MyFirstGUI(root)
    root.mainloop()
    li = []
    li.append(my_gui.varEntry.get())
    li.append(my_gui.attr1)
    li.append(my_gui.varSlider.get())
    return(li)
test()