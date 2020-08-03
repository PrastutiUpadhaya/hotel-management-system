from tkinter import *
root = Tk()
root.geometry("300x300")#resize
root.title("AVAILABILITY STATUS ")
root.configure(background="#e6edf5")
var1=StringVar()
var2=StringVar()
radio_var=StringVar()
but1=StringVar
#create image
#canvas=Canvas(root,width=300,height=300)
#canvas.pack(fill=BOTH,expand=TRUE)
#image_byt = urlopen("https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi1lMOfqNXlAhUJv48KHfDdAbcQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.welcome-hotels.com%2Fen%2Fhotels%2Fmarburg%2F&psig=AOvVaw0zcOQEq-qFzrajxKVvtihp&ust=1573119173572577").read()
#image_b64 = base64.encodestring(image_byt)
img = PhotoImage(file="hotel.jpeg")
canvas.create_image(0,0,image=img,anchor='nw')

#branch=droplist
lab1=Label(root,text="Branch : " ,fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
lab1.place(x=110,y=120)
list=["Mumbai","Delhi","Pune","Bangalore","Rajasthan"]
droplist=OptionMenu(root,var1,*list)
var1.set("Select the branch")
droplist.configure(width=20)
droplist.place(x=200,y=120)
#room type = droplist
lab2=Label(root,text="Room type  : " ,fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
lab2.place(x=110,y=160)
list2=[ '1','2','3']
droplist2=OptionMenu(root,var2,*list2)
var2.set("Number of beds")
droplist2.configure(width=20)
droplist2.place(x=200,y=160)
#roomview=radio button
lab3=Label(root,text="Room View  : " ,fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
lab3.place(x=110,y=200)
r1=Radiobutton(root,text="Yes",variable=radio_var,value="true").place(x=230,y=200)
r2=Radiobutton(root,text="No",variable=radio_var,value="false").place(x=320,y=200)
#check in dates
lab4=Label(root,text="Check in  : ",fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
lab4.place(x=110,y=240)
lab5=Label(root,text="Check out  : ",fg="black",bg="#e6edf5",font=("comic sans",10,"bold" ))
lab5.place(x=110,y=280)

# submit

c1=Button(root,text="SUBMIT",width='10',fg="#5e3919",bg="#c5f0f0",font=("arial",10,"bold"),relief="solid").place(x=200,y=360)
root.mainloop()