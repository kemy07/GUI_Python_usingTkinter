import tkinter
window = tkinter.Tk()
window.title ("GUI Entry")
window.geometry('400x200')
label2 = tkinter.Label(window, text="The name Will ne here")
entry = tkinter.Entry(window , bd = 3)
def change():
    name = entry.get()
    label2.configure(text = name)
def main():

    label = tkinter.Label(window, text = "Please Enter Your name")
    button = tkinter.Button (window, text ="Display", command =lambda:change())
    label.grid(column=0, row=0)
    entry.grid(column=0, row=1)
    button.grid(column=0, row=2)
    label2.grid(column=0, row=3)
    window.mainloop()


if __name__ == '__main__':
    main()

