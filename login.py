from tkinter import *
from tkinter import messagebox as mb
import operations as op

class UserCheck():
    def __init__(self,window):
        window.title('Log in Page')
        pic = PhotoImage(file='login-pic.png')
        window.iconphoto(True,pic)
        self.__frame = Frame(window,bg='#030d31')
        self.__userl = Label(self.__frame,text='User name: ',bg='#030d31',font=('Nirmala Ui',18,'italic')\
                             ,fg='white')
        self.__usere = Entry(self.__frame,width=10,font=('Open Sans',16))
        self.__label = Label(self.__frame,text='Log In',font=('Arial Black',25,'bold'),\
                             bg='#030d31',fg='white')
        self.__passl = Label(self.__frame,text='Password: ',bg='#030d31',font=('Nirmala Ui',18,'italic'),\
                             fg='white')
        self.__passe = Entry(self.__frame,width=10,font=('Open Sans',16))
        self.__button = Button(self.__frame,text='Check',bg='#09c567',fg='black',font=('Nirmala Ui',20,),\
                               command=lambda: self.click(window),width=8)
        
    def setup(self):
        self.__frame.pack(padx=100,pady=100)
        self.__label.grid(row=0,columnspan=2)
        self.__userl.grid(row=1,column=0,pady=50,padx=50)
        self.__usere.grid(row=1,column=1,pady=50,padx=50)
        self.__passl.grid(row=2,column=0,pady=50,padx=50)
        self.__passe.grid(row=2,column=1,pady=50,padx=50)
        self.__button.grid(row=3,columnspan=2)    

    def click(self,window):
        if self.__usere.get() == '1111' and self.__passe.get() == '2222':
            mb.showinfo(title='Result',message='Successfully loged in')
            self.__frame.destroy()
            page3 = op.Perform(window) 
            page3.setup(window)
        else:
            mb.showwarning(title='Result',message='Incorrect password or user name')    