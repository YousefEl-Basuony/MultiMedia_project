from tkinter import *
import webbrowser

def open_link():
    link = mytext.get()
    webbrowser.open(link)

def open_github():
    webbrowser.open("https://github.com/YousefEl-Basuony")

def open_Portfolio():
    webbrowser.open("https://yousefel-basuony.github.io/Portfolio_YousefElbasuony/")

def exit_app():
    exit()

root = Tk()
root.title("My GUI App")
root.geometry("500x400")
root.configure(bg="#1e1e2f")

title_label = Label(
    root,
    text="Mini Web Browser",
    font="Helvatica 16 bold",
    fg="white",
    bg="#1e1e2f"
)
title_label.pack(pady=10)

info_label = Label(
    root,
    text="Go To Link اكتب أي لينك تحت واضغط  ",
    font="Helvatica 10 bold",
    fg="white",
    bg="#1e1e2f"
)
info_label.pack(pady=5)

mytext = Entry(
    root,
    width=40,
    font="Helvatica 12",
    fg="#222",
    bg="#e8e8e8",
    borderwidth=3,
    relief="groove"
)
mytext.pack(pady=10, ipady=5, fill=X, padx=30)

go_button = Button(
    root,
    text="Go To Link",
    fg="white",
    bg="#4a4ac8",
    activebackground="#6a6af0",
    activeforeground="white",
    font="Helvatica 12 bold",
    padx=20,
    pady=5,
    command=open_link
)
go_button.pack(pady=10)

github_button = Button(
    root,
    text="GitHub",
    fg="white",
    bg="#24292e",
    activebackground="#3b3f45",
    activeforeground="white",
    font="Helvatica 10 bold",
    padx=20,
    pady=5,
    command=open_github
)
github_button.pack(side=LEFT, padx=30, pady=20, anchor="w")

Portfolio_button = Button(
    root,
    text="Portfolio",
    fg="white",
    bg="red",
    activebackground="#6075d0",
    activeforeground="white",
    font="Helvatica 10 bold",
    padx=20,
    pady=5,
    command=open_Portfolio
)
Portfolio_button.pack(side=LEFT, padx=10, pady=20, anchor="w")

exit_button = Button(
    root,
    text="Exit",
    fg="white",
    bg="gray",
    activebackground="#999",
    activeforeground="white",
    font="Helvatica 10 bold",
    padx=20,
    pady=5,
    command=exit_app
)
exit_button.pack(side=RIGHT, padx=30, pady=20, anchor="e")

root.mainloop()
