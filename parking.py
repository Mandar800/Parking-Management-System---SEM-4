from tkinter import *
import sqlite3

conn = sqlite3.connect('SPM.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS SPM (slot TEXT Primary key,State TEXT,Car TEXT,Name TEXT, phno TEXT)')
c.execute('select * From SPM')
print(c.fetchall())

root = Tk()
left = Frame(root)
side = Frame(root)
left.pack(side=LEFT)
side.pack(side=RIGHT)
tf = Frame(left)
bf = Frame(left)
tf.pack(side=TOP)
bf.pack(side=BOTTOM)
root.title("Simple Parking Manager")

Name = StringVar()
NP = StringVar()
PH = StringVar()


def onclick(args,s):
    if s['bg'] == 'green':
            print(args)
            n = Name.get()
            np = NP.get()
            p = PH.get()
            c.execute('INSERT INTO SPM (slot , State,Car,Name,phno) VALUES(?,?,?,?,?)', (args, 1, np, n, p))
            conn.commit()
            print(' database updated')
            s.configure(bg='red',text=n+" "+np)
    else:
        print('in else')
        a = str(args)
        s.configure(bg='green',text='Slot '+a)
        c.execute('Delete From SPM Where slot='+a+'')
        conn.commit()
        print('database updated')


s1 = Button(tf, text="Slot 1", fg="white", bg="green", height=20, width=15, command=lambda: onclick(1, s1),relief="raised")
s2 = Button(tf, text="Slot 2", fg="white", bg="green", width=15, height=20, command=lambda: onclick(2, s2),relief="raised")
s3 = Button(tf, text="Slot 3", fg="white", bg="green", width=15, height=20, command=lambda: onclick(3, s3),relief="raised")
s4 = Button(tf, text="Slot 4", fg="white", bg="green", width=15, height=20, command=lambda: onclick(4, s4),relief="raised")
s5 = Button(tf, text="Slot 5", fg="white", bg="green", width=15, height=20, command=lambda: onclick(5, s5),relief="raised")
s6 = Button(bf, text="Slot 6", fg="white", bg="green", height=20, width=15, command=lambda: onclick(6, s6),relief="raised")
s7 = Button(bf, text="Slot 7", fg="white", bg="green", width=15, height=20, command=lambda: onclick(7, s7),relief="raised")
s8 = Button(bf, text="Slot 8", fg="white", bg="green", width=15, height=20, command=lambda: onclick(8, s8),relief="raised")
s9 = Button(bf, text="Slot 9", fg="white", bg="green", width=15, height=20, command=lambda: onclick(9, s9),relief="raised")
s10 = Button(bf, text="Slot 10", fg="white", bg="green", width=15, height=20, command=lambda: onclick(10, s10),relief="raised")
s1.grid(row=0, column=0)
s2.grid(row=0, column=1)
s3.grid(row=0, column=2)
s4.grid(row=0, column=3)
s5.grid(row=0, column=4)
s6.grid(row=1, column=0)
s7.grid(row=1, column=1)
s8.grid(row=1, column=2)
s9.grid(row=1, column=3)
s10.grid(row=1, column=4)
name = Label(side, text="Name")
Np = Label(side, text="Car No.Plate")
ph = Label(side, text="Phone No.:")
ename = Entry(side, textvariable=Name)
enp = Entry(side, textvariable=NP)
eph = Entry(side, textvariable=PH)
name.grid(row=0, column=0)
Np.grid(row=1)
ph.grid(row=2)
ename.grid(row=0, column=1)
enp.grid(row=1, column=1)
eph.grid(row=2, column=1)

c.execute('select * From SPM')
for row in c.fetchall():
    n=row[3]
    c=row[2]
    if row[0] == '1':
        s1.configure(bg='red',text=n+' '+c)
    if row[0] == '2':
        s2.configure(bg='red',text=n+' '+c)
    if row[0] == '3':
        s3.configure(bg='red',text=n+' '+c)
    if row[0] == '4':
        s4.configure(bg='red',text=n+' '+c)
    if row[0] == '5':
        s5.configure(bg='red',text=n+' '+c)
    if row[0] == '6':
        s6.configure(bg='red',text=n+' '+c)
    if row[0] == '7':
        s7.configure(bg='red',text=n+' '+c)
    if row[0] == '8':
        s8.configure(bg='red',text=n+' '+c)
    if row[0] == '9':
        s9.configure(bg='red',text=n+' '+c)
    if row[0] == '10':
        s10.configure(bg='red',text=n+' '+c)

root.mainloop()
