import tkinter
def main():
    window = tkinter.Tk()
    window.title ("GUI")
    window.geometry('400x200')
    label = tkinter.Label(window, text = "Hello World")
    label.pack ()
    window.mainloop()


if __name__ == '__main__':
    main()

