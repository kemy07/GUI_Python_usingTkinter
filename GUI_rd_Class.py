import tkinter
from tkinter import messagebox
def display():
    messagebox.showinfo("Message","Welcome to our App")
def main():
    window = tkinter.Tk()
    window.title ("Button Handling")
    window.geometry('400x400')
    button = tkinter.Button (window , text ="Display" , command =lambda:display() )
    button.grid(column = 4 , row = 4)
    window.mainloop()


if __name__ == '__main__':
    main()

