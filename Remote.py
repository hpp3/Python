# A GUI to control a specific type of Sharp TV from a connected computer

from Tkinter import *
import serial
from time import *
try:
    ser.close()
except:
    pass
ser = serial.Serial(0, 9600, timeout=1)
class App:

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()
        
        self.button = Button(self.frame, text="QUIT", fg="red", command=self.quiting)
        self.button.pack(side=LEFT) 
        
        v = IntVar()
        self.radio = Radiobutton(master, text="Power On", fg = "red", variable=v, value=1, indicatoron=0, command=self.poweron)
        self.radio.pack(side = LEFT)
        self.radio = Radiobutton(master, text="Power Off", fg="red", variable=v, value=2, indicatoron=0, command=self.poweroff)
        self.radio.pack(side = LEFT)

        self.volume = Scale(self.frame, from_=0, to=60, orient = HORIZONTAL)
        self.volume.pack(side = LEFT)

        self.button = Button(self.frame, text="Set Volume",  command=self.volume_set)
        self.button.pack(padx=5, pady = 5)
        
        self.menubar=Menu(root)
        
        self.inputmenu = Menu(self.menubar, tearoff=0)
        self.inputmenu.add_command(label="TV", command=self.input0)
        self.inputmenu.add_command(label="DVD", command=self.input1)
        self.inputmenu.add_command(label="Satellite", command=self.input2)
        self.inputmenu.add_command(label="DTV", command=self.input3)
        self.inputmenu.add_command(label="INPUT 4", command=self.input4)
        self.inputmenu.add_command(label="INPUT 5", command=self.input5)
        self.inputmenu.add_command(label="INPUT 6", command=self.input6)
        self.inputmenu.add_command(label="PC", command=self.input7)
        self.menubar.add_cascade(label="Input mode", menu=self.inputmenu)
        
        
        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.viewmenu.add_command(label="Side Bar [AV]", command=self.view1)
        self.viewmenu.add_command(label="S.Stretch [AV]", command=self.view2)
        self.viewmenu.add_command(label="Zoom [AV]", command=self.view3)
        self.viewmenu.add_command(label="Stretch [AV]", command=self.view4)
        self.viewmenu.add_separator()
        self.viewmenu.add_command(label="Normal [PC]", command=self.view5)
        self.viewmenu.add_command(label="Zoom [PC]", command=self.view6)
        self.viewmenu.add_command(label="Stretch [PC]", command=self.view7)
        self.viewmenu.add_command(label="Dot by Dot [PC]", command=self.view8)
        self.menubar.add_cascade(label="View mode", menu=self.viewmenu)
        
        self.menubar.add_command(label="Command...", command=self.dialog)
        
        root.config(menu=self.menubar)
        



    
    def quiting(self):
        ser.close()
        self.frame.quit()

    def volume_set(self):
        x = str(self.volume.get())
        ser_write("VOLM"+x)

    def poweron(self):
        ser_write("POWR1")

    def poweroff(self):
        ser_write("RSPW1")
        sleep(1)
        ser_write("POWR0")

    def input0(self):
        ser_write("ITVD0") 
    def input1(self):
        ser_write("IAVD1") 
    def input2(self):
        ser_write("IAVD2") 
    def input3(self):
        ser_write("IAVD3") 
    def input4(self):
        ser_write("IAVD4") 
    def input5(self):
        ser_write("IAVD5") 
    def input6(self):
        ser_write("IAVD6") 
    def input7(self):
        ser_write("IAVD7") 

    def view1(self):
        ser_write("WIDE1") 
    def view2(self):
        ser_write("WIDE2") 
    def view3(self):
        ser_write("WIDE3") 
    def view4(self):
        ser_write("WIDE4") 
    def view5(self):
        ser_write("WIDE5") 
    def view6(self):
        ser_write("WIDE6") 
    def view7(self):
        ser_write("WIDE7") 
    def view8(self):
        ser_write("WIDE8")
    
    def dialog(self):
        new_ = MyDialog()
        
class MyDialog:

    def __init__(self):

        top = self.top = Toplevel()



        Label(top, text="Command:").pack()

        self.e = Entry(top)
        self.e.pack(padx=5)


        self.buttonbox()
    def buttonbox(self):

        w = Button(self.top, text="OK", width=10, command=self.ok, )
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(self.top, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.top.bind("<Return>", self.ok)
        self.top.bind("<Escape>", self.cancel)




    def ok(self, event = None):

        x = self.e.get()
        ser_write(x)

        self.top.destroy()
    
    def cancel(self, event=None):
        self.top.destroy()

def ser_write(string_):
    i = 8 - len(string_) 
    string_ = string_.upper()
    #print(string_+"~"*i+";"),
    ser.write(string_+" "*i+"\r")
    #print ser.readline()
    
root = Tk()

app = App(root)

root.mainloop()
