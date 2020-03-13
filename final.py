#import modules
 
from tkinter import *
import os
import cv2
import numpy as np
import cv2
import time

# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("New User Registration")
    register_screen.geometry("400x350")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below to register").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width="10", height="1", command = register_user).pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Go Back", width="10", height="1", command=delete_reg_screen).pack()
 
 



# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("User Login")
    login_screen.geometry("400x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width="20", height="1", command = login_verify).pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Go Back", width="20", height="1", command = delete_login_screen).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="").pack()
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            ab=open("config.txt", 'r')
            configlist=ab.readlines();
            configlist[0]="0\n"
            configlist[1]=int(configlist[1])+1
            configlist[1]=str(configlist[1])
            print(configlist)
            ab.close()
            ab=open("config.txt", 'w')
            ab.writelines(configlist)
            login_sucess()
            
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 


def personality():
    import webbrowser
    url = "https://www.16personalities.com/free-personality-test"
    webbrowser.open_new_tab(url)


def beatcapture():
    login_success_screen.destroy()
    login_screen.destroy()
    import heartbeat

def blink_record():
    login_success_screen.destroy()
    login_screen.destroy()
    import EyeBlinkCount

def audiocapture():
    login_success_screen.destroy()
    login_screen.destroy()
    #import liveaaudio

def video_record():
    login_success_screen.destroy()
    login_screen.destroy()
    import capture
    #exec('capture')
    import audiospeech 
    #exec('audiospeech')
    #time.sleep(2)
    #ffmpeg -i capture.avi -c:a aac -b:a 128k -c:v libx264 -crf 23 output.mp4
    #ffmpeg -i output.mp4 -ab 160k -ac 2 -ar 44100 -vn Sample.wav
    #import waveanalyse
    #exec('waveanalyse')
#main dashboard


def dashboard():
	login_success_screen.destroy()
	login_screen.destroy()
	global dashboard_screen
	dashboard_screen = Toplevel(main_screen)
	dashboard_screen.title("Veritas - Home Page")
	dashboard_screen.geometry("800x800")
	Label(dashboard_screen, text="Welcome To The Portal.. Please select anyone of the below options. ").pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Personality Test", width="30", height="3", command = personality).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Blink Detection", width="30", height="3", command = blink_record).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Video Analysis", width="30", height="3", command = video_record).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="HeartBeat Measurer", width="30", height="3", command = beatcapture).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Audio Analyser", width="30", height="3", command = audiocapture).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Logout", width="30", height="3", command = delete_dashboard_screen).pack()
	Label(dashboard_screen, text="").pack()
	Button(dashboard_screen, text="Quit Application", width="30", height="3", command =delete_main_screen).pack()

def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x100")
    Label(login_success_screen, text="Login Success",bg="green", width="300", height="2").pack()
    Label(login_success_screen, text="").pack()
    Button(login_success_screen, text="Go To Main Program", command=dashboard).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Error !!")
    password_not_recog_screen.geometry("300x100")
    Label(password_not_recog_screen, text="Invalid Password ", bg="red", width="300", height="2").pack()
    Label(password_not_recog_screen, text="").pack()
    Button(password_not_recog_screen, text="Go Back", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Error !!")
    user_not_found_screen.geometry("300x100")
    Label(user_not_found_screen, text="User Not Found", bg="red",width="300", height="2").pack()
    Label(user_not_found_screen, text="").pack()
    Button(user_not_found_screen, text="Go Back", command=delete_user_not_found_screen).pack()
 

 

# Deleting popups
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
def delete_main_screen():
    main_screen.destroy()
   

def delete_reg_screen():
    register_screen.destroy()
    
def delete_login_screen():
    login_screen.destroy()

def delete_dashboard_screen():
    dashboard_screen.destroy()

# Designing Main(first) window
 

def main_account_screen():
    global main_screen
    f=open('result.txt','w+')
    main_screen = Tk()
    main_screen.geometry("500x400")
    main_screen.title("Veritas - Login/Register Page")
    Label(text="Select Your Choice", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    Label(text="").pack()
    Button(text="Quit Application", width="30", height="2", command =delete_main_screen).pack()
    main_screen.mainloop()
 
main_account_screen()
