import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("600x400")
app.title("Library Management System")

# USING A BACKGROUND IMAGE

img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\DredSek\Pictures\GUI_BACKGROUND.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()

frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=30)
frame.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER,)

l2 = customtkinter.CTkLabel(master=frame, text="Login to your account", font=("Century Gothic",20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y=110)

app.mainloop()