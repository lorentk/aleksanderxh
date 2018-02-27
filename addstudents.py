from Tkinter import *
import sqlite3
import tkMessageBox

# konektohemi ne databaze
conn = sqlite3.connect('database.db')
# kursori per te levizur ne db
c = conn.cursor()

# id
ids = []


# tkinter window
class Application:
    def __init__(self, master):
        self.master = master

        # i krijojme frames
        self.left = Frame(master, width=800, height=720, bg='steelblue')
        self.left.pack(side=LEFT)

        self.right = Frame(master, width=400, height=720, bg='steelblue')
        self.right.pack(side=RIGHT)

        # labels per dritaret
        self.heading = Label(self.left, text="SH.M.L. Aleksander Xhuvani", font=('arial 40 bold'), fg='black',
                             bg='steelblue')
        self.heading.place(x=0, y=0)
        # emri i nxenesit
        self.name = Label(self.left, text="Emri i nxenesit", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.name.place(x=0, y=100)

        # mosha
        self.age = Label(self.left, text="Data e lindjes", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.age.place(x=0, y=140)

        # gjinia
        self.gender = Label(self.left, text="Gjinia", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.gender.place(x=0, y=180)

        # Vendbanimi
        self.location = Label(self.left, text="Vendbanimi", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.location.place(x=0, y=220)

        # emri i prindit
        self.time = Label(self.left, text="Emri i prindit", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.time.place(x=0, y=260)

        # nr.tel
        self.phone = Label(self.left, text="Nurmi i telefonit", font=('arial 18 bold'), fg='white', bg='steelblue')
        self.phone.place(x=0, y=300)

        # Hyrjet per labelat============================================================
        self.name_ent = Entry(self.left, width=30)
        self.name_ent.place(x=250, y=100)

        self.age_ent = Entry(self.left, width=30)
        self.age_ent.place(x=250, y=140)

        self.gender_ent = Entry(self.left, width=30)
        self.gender_ent.place(x=250, y=180)

        self.location_ent = Entry(self.left, width=30)
        self.location_ent.place(x=250, y=220)

        self.time_ent = Entry(self.left, width=30)
        self.time_ent.place(x=250, y=260)

        self.phone_ent = Entry(self.left, width=30)
        self.phone_ent.place(x=250, y=300)

        # butoni per me performu komanda
        self.submit = Button(self.left, text="Shto nxenesin", width=20, height=2, bg='steelblue',
                             command=self.add_appointment)
        self.submit.place(x=300, y=340)

        # merret numri prej appointments n'db 
        sql2 = "SELECT ID FROM appointments "
        self.result = c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # i merr id
        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]
        # i shfaq nx ne anen e djatht te dritares
        self.logs = Label(self.right, text="Stats.", font=('arial 28 bold'), fg='white', bg='steelblue')
        self.logs.place(x=0, y=0)

        self.box = Text(self.right, width=50, height=40)
        self.box.place(x=20, y=60)
        self.box.insert(END, "Te gjithe nxenesit  :  " + str(self.final_id))

    # funksioni per me vepru kur klikohet butoni
    def add_appointment(self):
        # inputs t'user
        self.val1 = self.name_ent.get()
        self.val2 = self.age_ent.get()
        self.val3 = self.gender_ent.get()
        self.val4 = self.location_ent.get()
        self.val5 = self.time_ent.get()
        self.val6 = self.phone_ent.get()

        # kontrollojme nese input i user-it eshte i zbrazur
        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkMessageBox.showinfo("Verejtje", "Ju lutem mbushini te gjitha kutite")
        else:
            # tash nese eshte gjithcka ne rregull shtojme te dhenat ne db
            sql = "INSERT INTO 'appointments' (name, age, gender, location, scheduled_time, phone) VALUES(?, ?, ?, ?, ?, ?)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5, self.val6))
            conn.commit()
            tkMessageBox.showinfo("Operacioni u krye me sukses", "Nxenesi " + str(self.val1) + " u shtua ne bazen e te dhenave")




# krijojme objektin
root = Tk()
b = Application(root)

# rezolucioni i dritares ne pixel
root.geometry("1200x720+0+0")

# vendosim nese dritarja mund te zmadhohet/zvoglohet
root.resizable(True, True)

# tittuli i dritares
root.title("Regjistrimi i nxensve")

# fundi i loop
root.mainloop()
