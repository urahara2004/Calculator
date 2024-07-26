from tkinter import *
#module for importing images 
#from PIL import ImageTk, Image

root =  Tk()
root.geometry("300x435")
root.resizable(width=False,height=False)
root.title('calculator by "KRISHNA JADHAV"')
#root.iconbitmap("C:/Users/Administrator/Desktop/ACU.ico")
root.config(bg="grey")


e=Entry(root,width="45",borderwidth="5",bg="#ffffff",fg="black")
#ee=Entry(root,bg="orange",fg="black")




def addb(num):
    cur=e.get()
   # e.insert(0,e.get())
    e.delete(0,END)
    e.insert(0,str(cur)+str(num))
    
def clear():
      e.delete(0,END)


    
    
      
def add():
    first_num=e.get()
    global f_num
    global math
    math="sum"
    f_num=int(first_num)
    e.delete(0,END)

def equ():
    global sec_num
    sec_num=e.get()
    e.delete(0,END)
    if math=="sum":
        global answer
        answer=int( f_num)+int(sec_num)
        e.insert( 0, answer)
        
    if math=="sub":
     
        answer=int( f_num)-int(sec_num)
        e.insert( 0, answer)
        
    if math=="mul":
       
        answer=int( f_num)*int(sec_num)
        e.insert( 0, answer)
        
    if math=="div":
   
        answer=int( f_num)/int(sec_num)
        e.insert( 0, answer)



    
def sub():
    first_num=e.get()
    global f_num
    global math
    math="sub"
    f_num=int(first_num)
    e.delete(0,END)


def mul():
    first_num=e.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_num)
    e.delete(0,END)

def div():
    first_num=e.get()
    global f_num
    global math
    math="div"
    f_num=int(first_num)
    e.delete(0,END)



button1=Button(root,text="1",padx=40,pady=20,command=lambda: addb(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda: addb(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda: addb(3)) 
button4=Button(root,text="4",padx=40,pady=20,command=lambda: addb(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda: addb(5)) 
button6=Button(root,text="6",padx=40,pady=20,command=lambda: addb(6)) 
button7=Button(root,text="7",padx=40,pady=20,command=lambda: addb(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda: addb(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda: addb(9))
button0=Button(root,text="0",padx=40,pady=20,command=lambda: addb(0))
buttonadd=Button(root,text="+",font=("lucida",10,"bold"),padx=40,pady=20,bg="#ffffff",command=add)
buttonsub=Button(root,text="-",padx=42,pady=20,bg="#ffffff",command=sub,font=("lucida",10,"bold"))
buttonmul=Button(root,text="*",padx=42,pady=20,bg="#ffffff",command=mul,font=("lucida",10,"bold"))
buttondiv=Button(root,text="/",padx=42,pady=20,bg="#ffffff",command=div,font=("lucida",10,"bold"))
buttonequ=Button(root,text="=",padx=90,pady=20,font=("lucida",10,"bold"),bg="#ffffff",command=equ)
buttonclear=Button(root,text="clear",padx=78,pady=20,bg="#ffffff",font=("lucida",10,"bold"),command=clear)
buttonexit=Button(root,text="exit",padx=100,pady=20,bg="#ffffff",font=("lucida",20,"bold"),command=root.quit)


#ee.grid(row=0,column=4,padx=3,pady=20)

e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
button1.grid(row= 3, column= 0)
button2.grid(row= 3, column= 1)
button3.grid(row= 3, column= 2)

button4.grid(row= 2, column= 0)
button5.grid(row= 2, column= 1)
button6.grid(row= 2, column= 2)

button7.grid(row= 1, column= 0)
button8.grid(row= 1, column= 1)
button9.grid(row= 1, column= 2)

button0.grid(row= 4, column= 0)

buttonadd.grid(row= 5, column= 0)
buttonsub.grid(row=6,column=0)
buttonmul.grid(row= 6, column= 1)
buttonequ.grid(row= 5, column= 1,columnspan=2)
buttondiv.grid(row= 6, column= 2)
buttonclear.grid(row= 4, column=1 ,columnspan=2)
buttonexit.grid(row= 7, column=0 ,columnspan=3)



root.mainloop()
