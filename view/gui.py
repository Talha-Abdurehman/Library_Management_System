# IMPORTING DIFFERENT LIBRARIES
import sys, os, tkinter, customtkinter
from main import *
from PIL import ImageTk, Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from db_functions.login import LRegister as lr

# SETTING APPEARANCE FOR THE MAIN APP
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")



# INITIALIZING THE APP
app = customtkinter.CTk()
app.geometry("1280x768")
app.title("Library Management System")


# ==================================== LOGIN FUNCTION ========================================
def btn_func():
    
    fname = entry1.get()
    pswd = entry2.get()
    

    if lr.login(fname, pswd) == 1: 
        app.destroy()
        new_func()

    else: 
        l2 = customtkinter.CTkLabel(master=frame, text="wrong credentials", text_color="red", font=("Century Gothic",12))
        l2.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        
        dummy_frame = customtkinter.CTkFrame(master=app)
        dummy_frame.place(x=-10000,y=-10000)
        
        print("Hello Niggas")
        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        
        dummy_frame.focus()        

        entry1._placeholder_text = "First Name"
        entry2._placeholder_text = "Password"

        
# ==================================== SIGN UP FUNCTION ========================================
 
    
def signup_btn():
    frame.destroy()
    signup_form(l1, login_btn)
       
 
    
def login_btn():
    frame.destroy()
    login_form(l1, signup_btn, btn_func)
        


        
        
    
    
    

    

    



# USING A BACKGROUND IMAGE
img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\DredSek\Pictures\GUI_BACKGROUND.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()


# CREATING A LOGIN FRAME
frame = customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=30)
frame.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER,)


# CREATING A LABEL TO WHICH WILL BE OUR TITLE
l2 = customtkinter.CTkLabel(master=frame, text="LOG IN", font=("Century Gothic",20))
l2.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

l3 = customtkinter.CTkLabel(master=frame, text="Made By Talha Abdurehman With ❤️", font=("Century Gothic",10))
l3.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

#======================= CREATING DIFFERENT INSERT FORMS FOR USER TO INSERT INFORMATION INTO
# FIRST_NAME ENTRY FORM
entry1 = customtkinter.CTkEntry(master=frame
                                ,width=220,
                                placeholder_text="first Name")
entry1.place(x=50, y=110)


# PASSWORD ENTRY FORM
entry2 = customtkinter.CTkEntry(master=frame,
                                width=220, 
                                placeholder_text="Password")
entry2.place(x=50, y=165)


# FORGOT PASSWORD LABEL
l2 = customtkinter.CTkLabel(master=frame, 
                            text="Forgot Password",
                            font=("Century Gothic",12))
l2.place(x=175, y=200)


#========================== CREATING DIFFERENT BUTTONS FOR SIGNUP AND LOGIN
# LOGIN BUTTON
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", corner_radius=6,  
                                  fg_color="#006CA5",
                                  hover_color="#02367B",
                                  command=btn_func,
                                  )
button1.place(x=50, y=240)

# SIGNUP BUTTON
button2 = customtkinter.CTkButton(master=frame, width=80, height=20, text="Sign Up", corner_radius=6,  
                                  fg_color="#006CA5",
                                  hover_color="#02367B",
                                  compound="left",
                                  text_color="black",
                                  text_color_disabled="white",
                                  command=signup_btn)
button2.place(x=50, y=290)

# CONTACT BUTTON
button3 = customtkinter.CTkButton(master=frame, width=80, height=20, text="Contact Us", corner_radius=6,  
                                  fg_color="#006CA5",
                                  hover_color="#02367B",
                                  compound="left",
                                  text_color="black",
                                  text_color_disabled="white")
button3.place(x=190, y=290)


# THIS IS THE DEADPOINT FOR THE APP WHERE IT ENDS
app.mainloop()