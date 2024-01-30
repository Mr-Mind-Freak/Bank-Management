from tkinter import *
from tkinter import messagebox as mb
import sqlite3

class Perform():
    def __init__(self,window):
        window.title('Bank Operations')
        self.__conn = sqlite3.connect('Bank.db')
        self.__cur =self.__conn.cursor()
        self.__cur.execute('CREATE TABLE IF NOT EXISTS CUSTOMER (ACNO TEXT NOT NULL\
                            PRIMARY KEY,NAME TEXT NOT NULL,AMOUNT INT );')
        self.__conn.commit()
        self.__ac = StringVar()
        self.__name = StringVar()
        self.__amount = IntVar()
        self.__menubar = Menu(window)
        self.__frame = Frame(window,bg='#030d31')
        self.__acnolabel = Label(self.__frame,text='Enter account no: ',font=('Arial Black',25,'bold'),\
                                 bg='#030d31',fg='white')
        self.__acnoentry = Entry(self.__frame,textvariable=self.__ac,width=20,font=('Open Sans',16))
        self.__acname = Label(self.__frame,text='Account name: ',font=('Arial Black',25,'bold'),\
                              bg='#030d31',fg='white')
        self.__acnamentry = Entry(self.__frame,textvariable=self.__name,width=20,font=('Open Sans',16))
        self.__aciamt = Label(self.__frame,text='Amount: ',font=('Arial Black',25,'bold'),bg='#030d31',\
                              fg='white')
        self.__aciamtentry = Entry(self.__frame,textvariable=self.__amount,width=20,font=('Open Sans',16))
        self.__button = Button(self.__frame,text='Confirm',bg='#09c567',fg='black',font=('Nirmala Ui',20,),\
                               width=8)
        
    def setup(self,window):
        window.config(menu=self.__menubar)    
        self.__frame.pack(padx=20,pady=50)
        self.__menubar.add_command(label='Create account',command=self.create)
        self.__menubar.add_separator()
        self.__menubar.add_command(label='Deposit',command=self.deposit)
        self.__menubar.add_separator()
        self.__menubar.add_command(label='Withdraw',command=self.withdraw)
        self.__menubar.add_separator()
        self.__menubar.add_command(label='Show balance',command=self.balance)
        self.__menubar.add_separator()
        self.__menubar.add_command(label='Exit',command=quit)
        self.__acnolabel.grid(row=0,column=0)
        self.__acnoentry.grid(row=0,column=1)
        self.__acname.grid(row=1,column=0)
        self.__acnamentry.grid(row=1,column=1)
        self.__aciamt.grid(row=2,column=0)
        self.__aciamtentry.grid(row=2,column=1)
        self.__button.grid(row=3,columnspan=2)     

    def create(self):
        self.__ac.set('')
        self.__name.set('')
        self.__amount.set(0)
        self.__button.config(command=self.cclick)    

    def deposit(self):
        self.__ac.set('')
        self.__name.set('')
        self.__amount.set(0)
        self.__button.config(command=self.dclick)

    def withdraw(self):
        self.__ac.set('')
        self.__name.set('')
        self.__amount.set(0)
        self.__button.config(command=self.wclick)

    def balance(self):
        try:
            self.__cur.execute('SELECT ACNO,NAME,AMOUNT FROM CUSTOMER WHERE ACNO = ?',(self.__ac.get())) 
            lst = []
            for index in self.__cur.fetchall():
                lst.append(index)
            ac = str(lst[0][0])
            name = str(lst[0][1])
            at = str(lst[0][2])
            mb.showinfo(title='Balance',message='Ac no = '+ac+"\nName = "+name+"\nAmount = "+ at)

        except sqlite3.Error as e:
            print(e)    
            print('Failed to show balance') 
        else:
            pass  

    def cclick(self):
        try:
            self.__cur.execute("INSERT INTO CUSTOMER (ACNO, NAME, AMOUNT) VALUES (?, ?, ?);",\
                               (self.__ac.get(),self.__name.get(),self.__amount.get()))    
            self.__conn.commit()
        except sqlite3.Error as e:
            print(e)    
            print('Failed to insert datas')
        else:
            mb.showinfo(title='status',message='Account Successfully created')

    def dclick(self):
        try:
            self.__cur.execute('SELECT AMOUNT FROM CUSTOMER WHERE ACNO =?;',(self.__ac.get()))
            amt = self.__cur.fetchall()[0][0]
            amt += int(self.__amount.get())
            self.__cur.execute('UPDATE CUSTOMER SET AMOUNT = ? WHERE ACNO = ?',(str(amt),self.__ac.get()))
            self.__conn.commit()
        except sqlite3.Error as e:
            print(e)
            print('Failed to fetch data on deposit')
        else:
            mb.showinfo(title='status',message='Amount = {} Successfully \
                        deposit\nBalance = {}'.format(self.__amount.get(),amt))  

    def wclick(self):
        try:
            self.__cur.execute('SELECT AMOUNT FROM CUSTOMER WHERE ACNO =?;',(self.__ac.get()))
            amt = self.__cur.fetchall()[0][0]
            amt -= int(self.__amount.get())
            self.__cur.execute('UPDATE CUSTOMER SET AMOUNT = ? WHERE ACNO = ?;',(str(amt),self.__ac.get()))
            self.__conn.commit()
        except sqlite3.Error as e:
            print(e)
            print('Failed to fetch data on withdraw')  
        else:
            mb.showinfo(title='status',message='Amount = {} Successfully \
                        withdrawed\nBalance = {}'.format(self.__amount.get(),amt))        