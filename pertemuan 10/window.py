from tkinter import *

def display_greeting():
    greeting_label.config(text="Halo, Selamat datang")

window = Tk()
window.title("Program sambutan")

greeting_label = Label(window, text="")
greeting_label.pack(pady=20)

greet_button = Button(window, text="Tampilan Sambutan", command=display_greeting)
greet_button.pack()

window.mainloop()