from tkinter import *

from check_availability  import *
from booking import *
m= Tk()
m.geometry("1700x1500")#resize
m.title("LE VOYAGE")
canvas=Canvas(m,width=300,height=300)
canvas.pack(fill=BOTH, expand=TRUE)
img = PhotoImage(file="frontback.png")
canvas.create_image(0,0,image=img, anchor=NW)
label1=Label(m,text="WELCOME   TO ",bg="#f5c2a9",width=36,font=("comic sans",50,"bold" ),relief="groove")
label1.place(x=0,y=0)
label1=Label(m,text="LE  VOYAGE ",bg="#ec93ed",width=36,font=("comic sans",50,"bold" ),relief="groove")
label1.place(x=0,y=70)
but1=Button(m,text="CHECK AVAILABILITY ", width=20,bg="black",fg="white",font=("comic sans",15,"bold" ),command=check).place(x=300,y=600)
but2=Button(m,text=" RESERVATION ", width=20,bg="black",fg="white",font=("comic sans",15,"bold" ),command=reserve).place(x=650,y=600)
# but3=Button(m,text=" GENERATE BILL ", width=20,bg="black",fg="white",font=("comic sans",15,"bold" )).place(x=800,y=600)
m.mainloop()