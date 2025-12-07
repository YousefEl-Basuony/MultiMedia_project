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

title_label = Label(root, text="Mini Web Browser", font="Helvetica 16 bold", fg="white", bg="#1e1e2f")
title_label.pack(pady=10)

info_label = Label(root, text="Go To Link اكتب أي لينك تحت واضغط", font="Helvetica 10 bold", fg="white", bg="#1e1e2f")
info_label.pack(pady=5)

mytext = Entry(root, width=40, font="Helvetica 12", fg="#222", bg="#e8e8e8", borderwidth=3, relief="groove")
mytext.pack(pady=10, ipady=5, fill=X, padx=30)

go_button = Button(root, text="Go To Link", fg="white", bg="#4a4ac8", activebackground="#6a6af0", activeforeground="white", font="Helvetica 12 bold", padx=20, pady=5, command=open_link)
go_button.pack(pady=10)

buttons_frame = Frame(root, bg="#1e1e2f")
buttons_frame.pack(pady=10)

github_button = Button(buttons_frame, text="GitHub", fg="white", bg="#24292e", activebackground="#3b3f45", activeforeground="white", font="Helvetica 10 bold", padx=20, pady=5, command=open_github)
github_button.grid(row=0, column=0, padx=10)

Portfolio_button = Button(buttons_frame, text="Portfolio", fg="white", bg="red", activebackground="#6075d0", activeforeground="white", font="Helvetica 10 bold", padx=20, pady=5, command=open_Portfolio)
Portfolio_button.grid(row=0, column=1, padx=10)

exit_button = Button(root, text="Exit", fg="white", bg="gray", activebackground="#999", activeforeground="white", font="Helvetica 10 bold", padx=20, pady=5, command=exit_app)
exit_button.pack(pady=5)

footer_label = Label(root, text="Designed by Yousef Elbasuony", font="Helvetica 11 bold", fg="#3b6bd6", bg="#1e1e2f")
footer_label.pack(pady=(8,14))

root.mainloop()
