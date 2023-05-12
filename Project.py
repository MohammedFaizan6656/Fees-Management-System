from tkinter import ttk
import tkinter as tk
from tkinter import *
import mysql.connector

mydb=mysql.connector.connect(
    host="phpmyadmin.stem.arvixe.com",
    user="AITDEMO",
    password="ait@123",
    database="aitdemo",
)



def saverecord():
    a=txtid.get()
    b=txtfullname.get()
    c=txtDateofBirth.get()
    d=txtaddress.get()
    e=txtcontactNo.get()
    f=txtqualifi.get()
    g=txtcourse.get()
    h=txtTotalfees.get()
    i=txtcourseDuration.get()
    j=txtpaidFees.get()
    k=txtBalancefees.get()
    
    mycursor=mydb.cursor()
    mycursor.execute("insert into addmission(id,fullname,DateofBirth,address,contactNo,qualifi,course,Totalfees,courseDuration,paidFees,Balancefees)values("+a+",'"+b+"','"+c+"','"+d+"',"+e+",'"+f+"','"+g+"',"+h+",'"+i+"',"+j+","+k+")")
    mydb.commit()
    print("Record inserted ")    
#saverecord()

def Delete():
    mydb=mysql.connector.connect(
    host="phpmyadmin.stem.arvixe.com",
    user="AITDEMO",
    password="ait@123",
    database="aitdemo",
)
    mycursor=mydb.cursor()
    mycursor.execute("delete from addmission where id="+ txtid.get())
    mydb.commit()
    print("Record Deleted")
    
def Search():
    mydb=mysql.connector.connect(
    host="phpmyadmin.stem.arvixe.com",
    user="AITDEMO",
    password="ait@123",
    database="aitdemo",
)
    mycursor=mydb.cursor()
    id = txtid.get()
    sql_select_Query = "select * from addmission where id="+ txtid.get()
    cursor=mydb.cursor()
    cursor.execute(sql_select_Query)
    #get all records
    records = cursor.fetchall()

    for row in records:
        #print("id=",row[0], )
        txtid.insert(0,row[0])
        txtfullname.insert(0,row[1])
        txtDateofBirth.insert(0,row[2])
        txtaddress.insert(0,row[3])
        txtcontactNo.insert(0,row[4])
        txtqualifi.insert(0,row[5])
        txtcourse.insert(0,row[6])
        txtTotalfees.insert(0,row[7])
        txtcourseDuration.insert(0,row[8])
        txtpaidFees.insert(0,row[9])
        txtBalancefees.insert(0,row[10])
def Update():
    
    mydb=mysql.connector.connect(
    host="phpmyadmin.stem.arvixe.com",
    user="AITDEMO",
    password="ait@123",
    database="aitdemo",
)
    mycursor=mydb.cursor()
    mycursor.execute("update addmission set fullname='"+txtfullname.get()+"',contactNo="+txtcontactNo.get()+",Balancefees="+txtBalancefees.get()+" where id="+txtid.get())
    mydb.commit()
    print("Record Updated")


def view():
    
    mydb=mysql.connector.connect(
    host="phpmyadmin.stem.arvixe.com",
    user="AITDEMO",
    password="ait@123",
    database="aitdemo",
    )
    mycursor=mydb.cursor()

    mycursor.execute("SELECT `id`, `fullname`, `DateofBirth`, `Address`, `contactNo`, `qualifi`, `course`, `Totalfees`, `courseDuration`, `paidFees`, `Balancefees` FROM `addmission`")
    myresult=mycursor.fetchall()
    a=tk.Tk()
    
    tree=ttk.Treeview(a,column=("C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11"),show="headings")    
    tree.column("#1",anchor=tk.CENTER)
    tree.heading("#1",text="id")
    tree.column("#1",width="50")
    tree.column("#2",anchor=tk.CENTER)
    tree.heading("#2",text="fullname")
    tree.column("#3",anchor=tk.CENTER)
    tree.heading("#3",text="DateofBirth")
    tree.column("#4",anchor=tk.CENTER)
    tree.heading("#4",text="Address")
    tree.column("#5",anchor=tk.CENTER)
    tree.heading("#5",text="contactNo")
    tree.column("#6",anchor=tk.CENTER)
    tree.heading("#6",text="qualifi")
    tree.column("#6",width="50")
    tree.column("#7",anchor=tk.CENTER)
    tree.heading("#7",text="course")
    tree.column("#7",width="50")
    tree.column("#8",anchor=tk.CENTER)
    tree.heading("#8",text="Totalfees")
    tree.column("#8",width="50")
    tree.column("#9",anchor=tk.CENTER)
    tree.heading("#9",text="courseDuration")
    tree.column("#10",anchor=tk.CENTER)
    tree.heading("#10",text="paidFees")
    tree.column("#11",anchor=tk.CENTER)
    tree.heading("#11",text="Balancefees")
    tree.pack()

    for x in myresult:
        print(x)
        tree.insert("",tk.END, values=x)
a=Tk()
a.title("Addmission Data")
a.geometry("700x700")
a.configure(bg="salmon")
lbl=Label(a,text="AIT Instititude",bg="wheat",fg="brown")
lbl.grid(row=0,column=0)

c=Label(a,text="id")
c.grid(row=1,column=0)
c.configure(bg="salmon")
txtid=Entry(a,width=25,bg="gray")
txtid.grid(row=1,column=1)


d=Label(a,text="fullname")
d.grid(row=2,column=0)
d.configure(bg="salmon")
txtfullname=Entry(a,width=25,bg="gray")
txtfullname.grid(row=2,column=1)


e=Label(a,text="DateofBirth")
e.grid(row=3,column=0)
e.configure(bg="salmon")
txtDateofBirth=Entry(a,width=25,bg="gray")
txtDateofBirth.grid(row=3,column=1)

f=Label(a,text="address")
f.grid(row=4,column=0)
f.configure(bg='salmon')
txtaddress=Entry(a,width=25,bg="gray")
txtaddress.grid(row=4,column=1)

g=Label(a,text="contactNo")
g.grid(row=5,column=0)
g.configure(bg="salmon")
txtcontactNo=Entry(a,width=25,bg="gray")
txtcontactNo.grid(row=5,column=1)

h=Label(a,text="qualifi")
h.grid(row=6,column=0)
h.configure(bg="salmon")
txtqualifi=Entry(a,width=25,bg="gray")
txtqualifi.grid(row=6,column=1)

i=Label(a,text="course")
i.grid(row=7,column=0)
i.configure(bg="salmon")
txtcourse=Entry(a,width=25,bg="gray")
txtcourse.grid(row=7,column=1)

j=Label(a,text="Totalfees")
j.grid(row=8,column=0)
j.configure(bg="salmon")
txtTotalfees=Entry(a,width=25,bg="gray")
txtTotalfees.grid(row=8,column=1)

k=Label(a,text="courseDuration")
k.grid(row=9,column=0)
k.configure(bg="salmon")
txtcourseDuration=Entry(a,width=25,bg="gray")
txtcourseDuration.grid(row=9,column=1)

l=Label(a,text="paidFees")
l.grid(row=10,column=0)
l.configure(bg="salmon")
txtpaidFees=Entry(a,width=25,bg="gray")
txtpaidFees.grid(row=10,column=1)

m=Label(a,text="Balancefees")
m.grid(row=11,column=0)
m.configure(bg="salmon")
txtBalancefees=Entry(a,width=25,bg="gray")
txtBalancefees.grid(row=11,column=1)

k=Button(a,text="save",command=saverecord,bg="wheat",fg="brown")
k.grid(column=1,row=0)

o=Button(a,text="Remove",command=Delete, bg="wheat", fg="brown")
o.grid(column=2, row=0)

p=Button(a,text="Search",command=Search,bg="wheat", fg="brown")
p.grid(column=3,row=0)

q=Button(a,text="Update",command=Update,bg="wheat",fg="brown")
q.grid(column=4,row=0)

r=tk.Button(text="Display Data",command=view,bg="wheat",fg="brown")
r.grid(column=5,row=0)


a.mainloop()


















                 
