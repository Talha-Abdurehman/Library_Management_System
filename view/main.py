import tkinter
import customtkinter

def new_func():
        w = customtkinter.CTk()
        w.geometry("1920x1080")
        w.title("Welcome")
        l1 = customtkinter.CTkLabel(master=w, text="WELCOME TO HELL", font=("Gothic Century",60))
        l1.place(relx= 0.5, rely= 0.5 , anchor=tkinter.CENTER)
        w.mainloop()
