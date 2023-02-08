import tkinter
window = tkinter.Tk()
window.title ("Items Examples")
window.geometry('400x200')
entry = tkinter.Entry(window , bd = 3)
entry2 = tkinter.Entry(window , bd = 3)
entry3 = tkinter.Entry(window , bd = 3)
def Cal():
    price = int (entry.get())
    count = int (entry2.get())
    total = price * count
    entry3.delete(0 , tkinter.END)
    entry3.insert(0 , str(total))
def main():

    label = tkinter.Label(window, text = "Item Price")
    label2 = tkinter.Label(window, text = "Item Count")
    button = tkinter.Button (window, text ="Calc", command =lambda:Cal())
    label.grid(column=0, row=0)
    entry.grid(column=0, row=1)
    label2.grid(column=0, row=2)
    entry2.grid(column=0, row=3)
    button.grid(column=0, row=4)
    entry3.grid(column=0, row=5)
    window.mainloop()


if __name__ == '__main__':
    main()

