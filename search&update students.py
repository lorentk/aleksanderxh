# ky "program" sherben per kerkimin dhe ndryshimin e te dhenave te nxenesve
# importojm modulet
from Tkinter import *
import tkMessageBox
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

class Application:
    def __init__(self, master):
        self.master = master
        # labeli kryesor
        self.heading = Label(master, text="Kerko/Perditso nxenesit",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=400, y=0)

        
        self.name = Label(master, text="Shkruaj emrin e nxenesit", font=('arial 18 bold'))
        self.name.place(x=450, y=100)

       
        self.namenet = Entry(master, width=50)
        self.namenet.place(x=450, y=148)

        # butoni kerko
        self.search = Button(master, text="Kerko", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=550, y=178)
    # funksioni per butonin kerko
    def search_db(self):
        self.input = self.namenet.get()
        # marrim t'dhena n'db
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        # perditsimi 
        self.uname = Label(self.master, text="Emri dhe mbiemri", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="Data e Lindjes", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Gjinia", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="Vendbanimi", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="Emri i prindit", font=('arial 18 bold'))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text="Numri i tel.", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

       # -------
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        # butoni per me ekzekutu komanden e perditsimit/ndryshimit
        self.update = Button(self.master, text="Perditso", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # butoni per me fshi 
        self.delete = Button(self.master, text="Fshij", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    def update_db(self):
        # deklarimi i t'dhenave t'ndryshuara
        self.var1 = self.ent1.get() #updated name
        self.var2 = self.ent2.get() #updated age
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
        c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.var6, self.namenet.get(),))
        conn.commit()
        tkMessageBox.showinfo("U perditsua", "U perditsua me sukses.")
    def delete_db(self):
        # fshirja
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkMessageBox.showinfo("U fshi!", "U fshi me sukses!")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()
# krijimi i objektit
root = Tk()
b = Application(root)
root.geometry("1200x720+0+0")
root.resizable(True, True)
root.title("Kerko nxenesit")
root.mainloop()
