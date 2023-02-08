import tkinter
def main():
    window = tkinter.Tk()
    window.title ("Second GUI")
    window.geometry('400x400')
    label = tkinter.Label(window, text = "Label1")
    label2 = tkinter.Label(window, text = "Label2")
    label3 = tkinter.Label(window, text = "Label3")
    button = tkinter.Button (window , text ="Click")
    # label.pack ()
    # label2.pack ()
    # label3.pack ()
    label.grid(column = 1 , row = 0)
    label2.grid(column = 2 , row = 0)
    label3.grid(column = 3 , row = 0)
    button.grid(column = 4 , row = 1)
    window.mainloop()


if __name__ == '__main__':
    main()

