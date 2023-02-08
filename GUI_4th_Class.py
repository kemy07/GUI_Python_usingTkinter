import tkinter
window = tkinter.Tk()
window.title ("Button Handling")
window.geometry('400x400')
label = tkinter.Label(window, text = "Before Clicking")
def changeText():
    label.configure(text = "After Clicking")
    label.configure(foreground = "purple")
def main():

    button = tkinter.Button (window, text ="Display", command =lambda:changeText())
    label.grid(column = 1 , row = 0)
    button.grid(column = 4 , row = 4)
    window.mainloop()


if __name__ == '__main__':
    main()

