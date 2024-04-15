from tkinter import *
import calendar


text = calendar.calendar(2024)

root = Tk()
root.geometry("950x950")
root.title("King")
label1 = Label(root, text="King", bg="dark gray", font=("times", 20, "bold"))
label1.grid(row=1, column=1)
root.config(background="white")
l1 = Label(root, text=text, font=("consolas", 14, "bold"))
l1.grid(row=2, column=1, padx=20)
root.mainloop()
