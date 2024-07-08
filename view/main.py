import tkinter
import customtkinter

def new_func():
        w = customtkinter.CTk()
        w.geometry("1920x1080")
        w.title("Welcome")
        l1 = customtkinter.CTkLabel(master=w, text="WELCOME TO HELL", font=("Gothic Century",60))
        l1.place(relx= 0.5, rely= 0.5 , anchor=tkinter.CENTER)
        w.mainloop()


def signup_form(l1):
    
    frame = customtkinter.CTkFrame(master=l1, width=320, height=600, corner_radius=30)
    frame.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER,)


    # CREATING A LABEL TO WHICH WILL BE OUR TITLE
    l2 = customtkinter.CTkLabel(master=frame,
                                text="Sign Up",
                                font=("Century Gothic",20))
    l2.place(x=50, y=45)

    #======================= CREATING DIFFERENT INSERT FORMS FOR USER TO INSERT INFORMATION INTO
    # FIRST_NAME ENTRY FORM
    entry1 = customtkinter.CTkEntry(master=frame
                                    ,width=220,
                                    placeholder_text="First Name")
    entry1.place(x=50, y=110)


    # PASSWORD ENTRY FORM
    entry2 = customtkinter.CTkEntry(master=frame,
                                    width=220, 
                                    placeholder_text="Last Name")
    entry2.place(x=50, y=165)
    
    
    entry3 = customtkinter.CTkEntry(master=frame,
                                    width=220, 
                                    placeholder_text="Phone")
    entry3.place(x=50, y=220)
    
    entry4 = customtkinter.CTkEntry(master=frame,
                                    width=220, 
                                    placeholder_text="Password")
    entry4.place(x=50, y=275)


    # FORGOT PASSWORD LABEL
    l2 = customtkinter.CTkLabel(master=frame, 
                                text="Forgot Password",
                                font=("Century Gothic",12))
    l2.place(x=175, y=200)


    #========================== CREATING DIFFERENT BUTTONS FOR SIGNUP AND LOGIN
    # SIGN UP BUTTON
    button1 = customtkinter.CTkButton(master=frame, width=220,
                                      text="Signup",
                                      corner_radius=6,  
                                    fg_color="#006CA5",
                                    hover_color="#02367B",
                                    
                                    )
    button1.place(x=50, y=240)

    # SIGNUP BUTTON
    button2 = customtkinter.CTkButton(master=frame, 
                                    width=80,
                                    height=20,
                                    text="Login",
                                    corner_radius=6,  
                                    fg_color="#006CA5",
                                    hover_color="#02367B",
                                    compound="left",
                                    text_color="black",
                                    text_color_disabled="white",
                                    )
    button2.place(x=50, y=290)

    # CONTACT BUTTON
    button3 = customtkinter.CTkButton(master=frame,
                                    width=80, 
                                    height=20, 
                                    text="Contact Us", 
                                    corner_radius=6,  
                                    fg_color="#006CA5",
                                    hover_color="#02367B",
                                    compound="left",
                                    text_color="black",
                                    text_color_disabled="white")
    button3.place(x=190, y=290)