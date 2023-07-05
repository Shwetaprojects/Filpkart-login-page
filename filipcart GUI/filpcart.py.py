from tkinter import * 
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox 

def handle_login():
    email = email_input.get()
    password = password_input.get()
     
     
    if  email == 'shwetakgawali@gmail.com' and password == '1234':
            messagebox.showinfo('yayyyy','Login Successfull ')
    else:
            messagebox.showerror('Error','login Failed')

root = Tk()

root.title('login form')

root.iconbitmap('flipkart-icon.ico')

#root.minsize(100,100)       #for minimize size of gui screen
#root.maxsize(400,400)      #for maximize gui screen

root.geometry("350x300")     #speciffy screen size as we want

root.configure(background='#0096DC')
img = Image.open('flipcart_logo.png')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img) #label is use to insert imege and text  in gui

img_label.pack(pady=(10,10)) #geomatery manager - use to set the image on gui 


text_label = Label(root,text='Flipcart',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))



email_label = Label(root,text='Enter Email',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5)) #PADY is use to set gap in to texts
email_label.config(font=('verdana',12))


email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))


password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5)) #PADY is use to set gap in to texts (hight)
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))


login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=1,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',14))

root.mainloop()
