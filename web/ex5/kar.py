from tkinter import *
ob = Tk()
ob.title("Velan calculator")
e = Entry(ob,width = 20,borderwidth = 5)
e.grid(row = 0, column = 0,columnspan = 3,padx = 10,pady = 10)
def fun(num ):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(num))
def clear():
    e.delete(0,END)
    
button1 = Button(ob,text = "1",padx = 40,pady =20,command = lambda : fun(1))
button2 = Button(ob,text = "2",padx = 40,pady =20,command = lambda : fun(2))
button3 = Button(ob,text = "3",padx = 40,pady =20,command = lambda : fun(3))
button4 = Button(ob,text = "4",padx = 40,pady =20,command = lambda : fun(4))
button5 = Button(ob,text = "5",padx = 40,pady =20,command = lambda : fun(5))
button6 = Button(ob,text = "6",padx = 40,pady =20,command = lambda : fun(6))
button7 = Button(ob,text = "7",padx = 40,pady =20,command = lambda : fun(7))
button8 = Button(ob,text = "8",padx = 40,pady =20,command = lambda : fun(8))
button9 = Button(ob,text = "9",padx = 40,pady =20,command = lambda : fun(9))
button10 = Button(ob,text = "0",padx = 40,pady =20,command = lambda : fun(0))
button11 = Button(ob,text = "+",padx = 40,pady =20,command = lambda : sum)
button12 = Button(ob,text = "clear",padx = 38,pady =20,command = lambda : clear())

button1.grid(row =3, column =1)
button2.grid(row =3, column =2)
button3.grid(row =3, column =3)
button4.grid(row =4, column =1)
button5.grid(row =4, column =2)
button6.grid(row =4, column =3)
button7.grid(row =5, column =1)
button8.grid(row =5, column =2)
button9.grid(row =5, column =3)
button10.grid(row =6, column =1)
button12.grid(row =6,column =1)



ob.mainloop()