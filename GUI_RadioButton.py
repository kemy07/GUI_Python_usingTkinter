# advanced Method
from  tkinter import *
window = Tk()
window.title("GUI Radio Button")
window.geometry('400x200')
label = Label(window, text="Color")
var = IntVar()
def change():
    val = var.get()
    if (val == 1):
        label.configure(foreground="Red")
    if (val == 2):
        label.configure(foreground="Green")
    if (val == 3):
        label.configure(foreground="Blue")

def main():

    radio1 = Radiobutton(window , text = "Red" , variable = var , value = 1 , command = lambda : change() )
    radio2 = Radiobutton(window , text = "Green" , variable = var , value = 2 , command = lambda : change() )
    radio3 = Radiobutton(window , text = "Blue" , variable = var , value = 3 , command = lambda : change() )
    radio1.grid(column=0, row=0)
    radio2.grid(column=0, row=1)
    radio3.grid(column=0, row=2)
    label.grid(column=0, row=3)
    window.mainloop()


if __name__ == '__main__':
    main()

