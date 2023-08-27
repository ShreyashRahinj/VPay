from bz2 import compress
from ctypes import alignment
from time import sleep
from tkinter import *
from tkinter import font
import tkinter.messagebox as tmsg
import smtplib
import random
from PIL import ImageTk, Image
from multiprocessing.sharedctypes import Value
import webbrowser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from numpy import pad
root = Tk()
root.geometry("600x760+400+10")
root.title("VPay")

bg=PhotoImage(file="Vpaybg.png")
bg._reduce_()
bg1=PhotoImage(file="inup1.png")
bg1._reduce_()
bg2=PhotoImage(file="split1.png")
bg2._reduce_()
bg3=PhotoImage(file="photo1.png")
bg3._reduce_()
bg4=PhotoImage(file="Vpaybg.png")
bg4._reduce_()
image = Image.open("introimage.png")
image = image.resize((600, 640), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)



global dictsignup
f = open("records.txt", "r")
UserData = f.read()
dictsignup = UserData.split("\n")

f = open("usernamerecords.txt", "r")
username_string = f.read()
username_list = username_string.split("\n")
f = open("emailrecords.txt", "r")
f = open("emailrecords.txt", "r")
email_string = f.read()
email_list = email_string.split("\n")
dictemail={}

username = StringVar()
password = StringVar()
email = StringVar()
otp = IntVar()
upi=StringVar()
var=IntVar()
var.set(1)


def Signup():
    # frame0.destroy()
    
    intro_frame.destroy()
    up_frame = Frame(root, borderwidth=2,width=30,height=0)
    up_frame.grid(row=2, column=1, padx=5,pady=0)
    getemail_frame = Frame(root, borderwidth=2,height=15,bg="grey")
    getemail_frame.grid(row=2, column=1, padx=0,pady=30)
    verifyotp_frame = Frame(root, borderwidth=0,height=15,bg="white")
    verifyotp_frame.grid(row=2, column=1, padx=0,pady=30)
    Label(up_frame, text="Sign up", font="ROBOTO 20 bold",height=2,width=20,bg="orange",fg="white").grid(row=1, column=2,padx=5,pady=0)
    Label(up_frame, text="Username", font="ubuntu").grid(row=2, column=1)
    Label(up_frame, text="Password ", font="ubuntu").grid(row=3, column=1,pady=10)
    Entry(up_frame, textvariable=username,width=40).grid(row=2, column=2)
    Entry(up_frame, textvariable=password,width=40).grid(row=3, column=2)
    
    in_label=Label(root,image=bg1,width=600,height=580)
    in_label.grid(row=1,column=1)
    def Exit():
        root.quit()

    def signupsubmit():
        if username.get()+password.get() in dictsignup:
            tmsg.showinfo("Sign in", "Sign in successful")
            
        else:
            def verifyotp():
                verifyotp_frame.destroy()
                if otp.get() == OTP:
                    tmsg.showinfo("Email Verification",
                                  "Verified email successfully")
                    f = open("records.txt", "a+")
                    f.write(username.get() + password.get())
                    f.write("\n")
                    f = open("usernamerecords.txt", "a+")
                    f.write(username.get())
                    f.write("\n")
                    f = open("emailrecords.txt", "a+")
                    f.write(email.get())
                    f.write("\n")
                    in_label.destroy()
                    up_frame.destroy()
                    Label(root, text="Welcome to V Pay App",
                          font="ROBOTO 10",bg="purple",fg="white").grid(row=1, column=1)
                    Label(root, text="Press Exit and restart the app for enjoying the experience!!",
                          font="ROBOTO").grid(row=2, column=1,pady=10)
                    Button(root,text="Exit",command=Exit,width=10).grid(row=3,column=1)
                else:
                    tmsg.showinfo("Email Verification",
                                  "Verification Failed!")
            def getotp():
                getemail_frame.destroy()
                
                gmail_user = 'shreyash.22110311@viit.ac.in'
                gmail_password = ''

                sent_from = gmail_user
                to = [email.get()]
                subject = 'OTP for Email Verification in V-pay'
                body = f"'Hello sir , Thank you for using V-Pay ,This is your OTP for Email Verification', {OTP}"

                email_text = """
                From: %s
                To: %s
                Subject: %s

                %s
                """ % (sent_from, ", ".join(to), subject, body)
                try:
                    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                    smtp_server.ehlo()
                    smtp_server.login(gmail_user, gmail_password)
                    smtp_server.sendmail(sent_from, to, email_text)
                    smtp_server.close()
                    print("Email sent successfully!")
                    tmsg.showinfo("Email","Email sent successfully.")
                except Exception as ex:
                    print("Something went wrong….", ex)
                    tmsg.showinfo("Email","Something went wrong.\n Check your Email Id")

                Label(verifyotp_frame, text="Enter OTP").grid(row=1, column=2)
                Entry(verifyotp_frame, textvariable=otp,width=50).grid(row=2, column=2)
                Button(verifyotp_frame, text="Submit", command=verifyotp).grid(
                    row=6, column=2)
                in_label=Label(root,image=bg,width=600,height=580)
                in_label.grid(row=1,column=1)

            def verifyemail():
                global OTP
                OTP = random.randint(100, 999)
                print(OTP)
                up_frame.destroy()
                # label1.destroy()
                Label(getemail_frame, text="Enter your Email",font="Roboto 10").grid(row=1, column=2)
                Entry(getemail_frame, textvariable=email,width=50).grid(row=2, column=2)
                Button(getemail_frame, text="Submit", command=getotp).grid(
                    row=6, column=2)
                in_label=Label(root,image=bg,width=600,height=600)
                in_label.grid(row=1,column=1)
            verifyemail()

    Button(up_frame, text="Submit",font="Ubuntu 12 bold",bg="silver",command=signupsubmit,width=20).grid(row=6, column=2)

def Signin():
    
    # frame0.destroy()
    intro_frame.destroy()
    
    in_frame = Frame(root, borderwidth=0,height=20,width=30)   
    in_frame.grid(row=5, column=1, padx=5,pady=0)
    
    
    Label(in_frame,text="Sign in to VPay",font="ubuntu 30 bold",bg="red",fg="white",height=1).grid(row=1,column=2,pady=15)
    Label(in_frame,text="Username:",font="Roboto",bg="grey",fg="white").grid(row=2,column=1,padx=20)
    Label(in_frame,text="Password:",font="Roboto",bg="grey",fg="white").grid(row=5, column=1,padx=20,pady=10)

    Entry(in_frame, textvariable=username,width=35).grid(row=2,column=2,pady=10)
    Entry(in_frame, textvariable=password,width=35).grid(row=5, column=2)
    
    in_label=Label(root,image=bg1,width=600,height=54)
    in_label.grid(row=1,column=1)
    

    def signinsubmit():
        if username.get()+password.get() in dictsignup:
            tmsg.showinfo("Sign in","Sign in successful")
            in_label.destroy()
            in_frame.destroy()
            split_frame = Frame(root)
            split_frame.grid(row=0, column=0)
            viewlist_frame = Frame(root)
            viewlist_frame.grid(row=0, column=0)
            amount_var = IntVar()
            upi_var=StringVar()
            for i in range(len(email_list)):
                dictemail[username_list[i]]=email_list[i]
            sendemail_list = []

            def addemail():
                value = str(emailselect_list.get(emailselect_list.curselection()))
                sendemail_list.append(dictemail[value])

            def sendamount_mail():
                split_amount=int(amount_var.get()/len(sendemail_list))
                success=FALSE
                for j in range(len(sendemail_list)):
                    try:
                        sender="shreyash.22110311@viit.ac.in"
                        password="SSRahinj@48"
                        receiver=sendemail_list[j]

                        msg=MIMEMultipart()
                        msg["To"]=receiver
                        msg["From"]=sender
                        msg["Subject"]="QR Code"
                        QR=open("QR.png","rb").read()
                        QR_ready=MIMEImage(QR,"png",name="QR Code")
                        msg.attach(QR_ready)
                        text=MIMEText(f"The amount you have to pay is {split_amount} Rs.\nUPI Id for payment : {upi_var.get()}")

                        f = open("upi.txt", "a+")
                        f.write(upi_var.get())
                        f.write("\n")
                        msg.attach(text)
                        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
                            smtp.login(sender,password)
                            smtp.send_message(msg)
                        print ("Email sent successfully!")
                        success=TRUE
                    except Exception as ex:
                        print("Something went wrong....",ex)
                if success:
                    tmsg.showinfo("Email","Email sent successfully.")
            def Viewlist():
                global emailselect_list
                emailselect_list = Listbox(viewlist_frame)
                emailselect_list.grid(row=5, column=1)
                for i in range(len(email_list)):
                    emailselect_list.insert(END, username_list[i])
                Button(viewlist_frame, text="Add", command=addemail,width=17,bg="purple",fg="white").grid(row=6, column=1)
        else:
            tmsg.showinfo("Sign in","Sign in unsuccessful.\n Incorrect Username or Password.")
        def openapp():
            if var.get()==1:
                webbrowser.open("https://pay.google.com/about/")
            if var.get()==2:
                webbrowser.open("https://www.phonepe.com/")
            if var.get()==3:
                webbrowser.open("https://paytm.com/")
            if var.get()==4:
               webbrowser.open("https://www.amazon.in/amazonpay/home")
        def gethelp():
            webbrowser.open("http://127.0.0.1:5501/official_VPay.html")
        def option():
            radio1=Radiobutton(viewlist_frame,text="Gpay",variable=var,value=1).grid(row=9,column=1)
            radio1=Radiobutton(viewlist_frame,text="Phonepay",variable=var,value=2).grid(row=10,column=1)
            radio1=Radiobutton(viewlist_frame,text="Paytm",variable=var,value=3).grid(row=11,column=1)
            radio1=Radiobutton(viewlist_frame,text="AmazonPay",variable=var,value=4).grid(row=12,column=1)
            
        def Split():
            split_frame.destroy()
            # splitphoto_label1=Label(root,image=bg,width=600,height=280)
            # splitphoto_label1.grid(row=0,column=0)
            amount_label = Label(viewlist_frame, text="Enter the Amount",font="ROBOTO 10 ",bg="black",fg="white")
            amount_label.grid(row=2, column=0,pady=10)
            amount_entry = Entry(viewlist_frame, textvariable=amount_var,width=50)
            amount_entry.grid(row=2, column=1,padx=5)
            upi_label = Label(viewlist_frame, text="UPI Id",font="ROBOTO 10 ",bg="black",fg="white")
            upi_label.grid(row=3, column=0,pady=10)
            upi_entry = Entry(viewlist_frame, textvariable=upi_var,width=50)
            upi_entry.grid(row=3, column=1,padx=5)
            Button(viewlist_frame, text="View Friends", command=Viewlist,width=25,bg="pink",fg="purple").grid(row=4, column=1,pady=10)
            Button(viewlist_frame, text="Submit", command=sendamount_mail,width=30,bg="white",fg="red",font="ROBOTO 10 bold").grid(row=14, column=1,pady=10)
            # frame0=Frame(root)
            # frame0.grid(row=0,column=0)
            Button(viewlist_frame,text="Pay using",command=option,bg="pink",fg="black",width=20).grid(row=8,column=0,pady=10,padx=5)
            Button(viewlist_frame,text="Open",command=openapp,bg="black",fg="white",width=20).grid(row=13,column=0,pady=10,padx=5)
            def Exit():
                root.quit()
            Button(viewlist_frame,text="Exit",command=Exit,width=10,bg="black",fg="white").grid(row=15,column=2)
        splitphoto_label=Label(split_frame,image=bg,width=600,height=680)
        splitphoto_label.grid(row=1,column=1)
        Button(split_frame, text="Split the Bill!", command=Split,width=50,bg="black",fg="white").grid(row=5, column=1,pady=0)
        Button(split_frame, text="Get Help", command=gethelp,bg="black",fg="white").grid(row=6, column=1,pady=0)
    Button(in_frame,text="Submit",font="Ubuntu 12 bold",width=20,height="1",bg="black",fg="white",command=signinsubmit).grid(row=6,column=2,pady=10)
def start():
    sleep(2)
    intro_frame1.destroy()
    
    intro_label=Label(intro_frame,image=photo)
    intro_label.grid(row=1,column=1)
   
    Label(intro_frame, text="Welcome to V-Pay", font="Ubuntu",
                         fg="white", bg="OrangeRed", width=44,height=1).grid(row=2, column=1,pady=10)
    Button(intro_frame, text="            Sign In            ", bg="cyan",
                   fg="Black", relief=SUNKEN, command=Signin, width=30).grid(row=4, column=1)
    Button(intro_frame, text="            Sign Up            ", bg="salmon", fg="white",
                   relief=SUNKEN, command=Signup, width=30).grid(row=5, column=1, pady=10)
    
   
intro_frame = Frame(root, borderwidth=0, height=0)
intro_frame.grid(row=1, column=1)
intro_frame1 = Frame(root, borderwidth=0, height=0)
intro_frame1.grid(row=1, column=1)
label = Label(intro_frame1,image=bg4,width=600,height=720)
label.grid(row=1,column=1)
label1 = Label(intro_frame1,text="Loading....Please Wait",font="STAATLICHES 15 ")
label1.grid(row=2,column=1)

intro_frame1.after(200, start)


root.mainloop()