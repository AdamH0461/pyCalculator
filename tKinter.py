import tkinter
#creates window
window = tkinter.Tk()
#sets window title
window.title("title")
#window size
window.geometry("300x300")
#creates label, entry box, and button
label = tkinter.Label(window, text="Label")
entry = tkinter.Entry(window)
button = tkinter.Button(window, text="this is button")
#packs them onto screen
entry.pack()
button.pack()
label.pack()
#draws screen
window.mainloop()