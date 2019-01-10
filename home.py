from tkinter import *
import sqlite3
from tkinter import messagebox
import time

con = sqlite3.connect("rem.db")
cur=con.cursor()
top= Tk()
top.configure(background='gray')

#textvariable for insertion
t = StringVar()
d = StringVar()
ti= IntVar()
da = StringVar()
#textvariable for updation
id_u= StringVar()
title_u= StringVar()
desc_u= StringVar()
time_u= StringVar()
date_u= StringVar()
#.....................FUNCTION CALL TO PERFORM CREATE TASK..................................
def callcreate():
    t1 = Toplevel(background='gray')
    t1.minsize(width=500,height=500)
    lhd = Label(t1, text="NEW REMINDER",bg="gray" ,fg="white")
    lhd.place(x=35, y=20)

    lttl = Label(t1, text="Title",bg="gray" ,fg="white")
    lttl.place(x=35, y=50)
    tentry = Entry(t1,textvariable=t)
    tentry.place(x=125, y=50)

    ldesc = Label(t1, text="Description",bg="gray" ,fg="white")
    ldesc.place(x=35, y=80)
    tdesc = Text(t1,height=5, width=30)
    tdesc.place(x=125, y=80)

    ltime = Label(t1, text="Time(24hr)",bg="gray" ,fg="white")
    ltime.place(x=35, y=180)
    ttime = Entry(t1,textvariable=ti)
    ttime.place(x=125, y=180)

    ldate = Label(t1, text="Date",bg="gray" ,fg="white")
    ldate.place(x=35, y=210)
    tdate = Entry(t1,textvariable=da)
    tdate.place(x=125, y=210)
    #FUNCTION TO INSERT REMINDER INTO TABLE remin
    def dbinsert():
        tt = t.get()
        d1 = tdesc.get(1.0, END)
        ti1 = ti.get()
        da1 = da.get()
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS remind(id INTEGER PRIMARY KEY ,rtitle VARCHAR(40) ,rdesc VARCHAR(55), rtime VARCHAR(45),rdate VARCHAR(45))")
        con.commit()
        cur.execute("INSERT INTO remind(rtitle,rdesc,rtime,rdate) VALUES(?,?,?,?)",(tt,d1,ti1,da1))
        con.commit()
        t1.destroy()
        messagebox.showinfo("Success", "Reminder added")
    b= Button(t1, text="Submit" , command=dbinsert,bd=5)
    b.place(x=35,y=250)

#............................FUNCTION CALL TO PERFORM UPDATE TASK.................................
def callupdate():
    con = sqlite3.connect("rem.db")
    t1 = Toplevel(background='gray')
    cur.execute("SELECT * FROM remind")
    results = cur.fetchall()
    lsel = Label(t1, text="SELECT RECORD TO UPDATE",bg="gray" ,fg="white")
    lsel.place(x=35, y=80)
    list = Listbox(t1, height=20, width=50)
    list.place(x=200, y=80)
    for row in results:
        list.insert(END, row)

    # assigning for updation
    def dbsubmit():
        t2=Toplevel(background='gray')
        value = list.get(ACTIVE)
        id_l= Label(t2,textvariable=id_u,bg="gray", fg="white")
        title_e= Entry(t2,textvariable=title_u)
        desc_e = Entry(t2,textvariable=desc_u)
        time_e = Entry(t2,textvariable=time_u)
        date_e = Entry(t2,textvariable=date_u)

        id_u.set(value[0])
        title_u.set(value[1])
        desc_u.set(value[2])
        time_u.set(value[3])
        date_u.set(value[4])

        lid = Label(t2, text="Remainer No:", bg="gray", fg="white")
        lid.place(x=35, y=20)
        lttl = Label(t2, text="Title", bg="gray", fg="white")
        lttl.place(x=35, y=50)
        ldesc = Label(t2, text="Description", bg="gray", fg="white")
        ldesc.place(x=35, y=80)
        ltime = Label(t2, text="Time(24hr)", bg="gray", fg="white")
        ltime.place(x=35, y=110)
        ldate = Label(t2, text="Date", bg="gray", fg="white")
        ldate.place(x=35, y=140)

        id_l.place(x=125, y=20)
        title_e.place(x=125,y=50)
        desc_e.place(x=125,y=80)
        time_e.place(x=125,y=110)
        date_e.place(x=125,y=140)

    # perform updation
        def dbupdate ():
            con = sqlite3.connect("rem.db")
            cur = con.cursor()
            id=value[0]
            nw_title =title_u.get()
            nw_desc =desc_u.get()
            nw_time =time_u.get()
            nw_date =date_u.get()
            cur.execute("UPDATE remind SET rtitle=?,rdesc=?,rtime=?,rdate=? WHERE id=?",(nw_title,nw_desc,nw_time,nw_date,id))
            con.commit()
            t2.destroy()
            t1.destroy()
            messagebox.showinfo("Success", "Reminder updated")
        b = Button(t2, text="UPDATE", command=dbupdate, bd=5)
        b.place(x=70, y=170)
    b = Button(t1, text="Submit", command=dbsubmit,bd=5)
    b.place(x=510, y=80)

#.................................FUNCTION CALL TO PERFORM VIEW TASK...............................................
def callview():
     con = sqlite3.connect("rem.db")
     t1 = Toplevel(background='gray')
     cur.execute("SELECT * FROM remind")
     results = cur.fetchall()
     lsel=Label(t1, text="ALL RECORDS", bg="gray", fg="white")
     lsel.place(x=35, y=80)
     list =Listbox(t1,height=20, width=80)
     list.place(x=125, y=80)

     for row in results:
         list.insert(END,row)
     def dbview():
        t1.destroy()
     b = Button(t1, text="ok", command=dbview, bd=5)
     b.place(x=650, y=80)

# HOME PAGE CODING
w = Label(top, text="REMINDER APPLICATION",bg="gray" ,fg="white")
w.place(x=32, y=20)
b1 = Button(top, text="CREATE", command=callcreate ,bd=5)
b1.place(x=35, y=50)
b2 = Button(top, text="UPDATE", command=callupdate,bd=5)
b2.place(x=35, y=90)
b3 = Button(top, text="VIEW" , command=callview,bd=5)
b3.place(x=35, y=130)
top.mainloop()
