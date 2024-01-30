from tkinter import *
import login

class WelcomePage:
    def __init__(self,window,pic):
        window.title('Welcome Page')
        self.__frame = Frame(window,bg='#030d31')
        self.__label = Label(self.__frame,image=pic,text='Welcome To Mr.Kind Bank',\
                           font=('Arial Black',25,'bold'),bg='#030d31',fg='white',compound=TOP)
        self.__button = Button(self.__frame,text='Next',bg='#09c567',fg='black',\
                             font=('Nirmala Ui',20,),command=lambda: self.click(window),width=8)
        
    def setup(self):    
        self.__frame.pack(pady=30)    
        self.__label.pack()
        self.__button.pack(pady=10)

    def click(self,window):
        self.__frame.destroy()    
        page2 = login.UserCheck(window)    
        page2.setup()


if __name__ == '__main__':
    window = Tk()
    pic = PhotoImage(file='bank-pic.png')
    window.config(bg='#030d31')
    window.iconphoto(True,pic)
    window.geometry('600x600')
    page1 = WelcomePage(window,pic)
    page1.setup()
    window.mainloop() 