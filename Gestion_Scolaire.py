from tkinter import *
from tkinter import ttk
from pymongo import *
from tkinter import messagebox


class Student:
    # --------------------- Create Page -------------------------
    def __init__(self, root):
        self.root = root
        self.root.geometry('1350x690+1+1')
        self.root.title('Gestion Scolaire')
        self.root.configure(background='#C3ACD0')
        self.root.resizable(False,False)
        title = Label(self.root,
              text = 'inscription des étudiants',
              bg = '#674188',
              font = ('poppins',14,'bold'),
              fg="white"
                      )
        title.pack(fill=X)
        #--------------- Frame Management---------------------------------
        Frame_managment = Frame(self.root, bg='white')
        Frame_managment.place(x=1137,y=30,width=210,h=400)
                #---------------------varibales-------------------------
        self.id = StringVar()
        self.Nom = StringVar()
        self.Email = StringVar()
        self.Tel = StringVar()
        self.certificats = StringVar()
        self.gender = StringVar()
        self.addresse = StringVar()
        self.delete = StringVar()
        self.search = StringVar()
        self.search_var = StringVar()
                #-----ID-----
        Id_label = Label(Frame_managment,text= "ID (int)", bg="white")
        Id_label.pack()
        Entry_id = Entry(Frame_managment, bd='2',textvariable= self.id, justify='center')
        Entry_id.pack()
                # -----Name d'etudiant-----
        Name_label = Label(Frame_managment, text="Name d'etudiant", bg="white")
        Name_label.pack()
        Entry_Name = Entry(Frame_managment, bd='2',textvariable= self.Nom,  justify='center')
        Entry_Name.pack()
                # -----Email d'etusiant-----
        Email_label = Label(Frame_managment, text="Email d'etudiant", bg="white")
        Email_label.pack()
        Entry_Email = Entry(Frame_managment, bd='2',textvariable= self.Email,  justify='center')
        Entry_Email.pack()
                # -----Phone d'etudiant-----
        Phone_label = Label(Frame_managment, text="Tel d'etudiant", bg="white")
        Phone_label.pack()
        Entry_Phone = Entry(Frame_managment, bd='2', textvariable= self.Tel, justify='center')
        Entry_Phone.pack()
                # -----Certies d'etudiant-----
        certie_label = Label(Frame_managment, text="certificats d'etudiant", bg="white")
        certie_label.pack()
        Entry_certie = Entry(Frame_managment, bd='2', textvariable= self.certificats, justify='center')
        Entry_certie.pack()
                # -----Gender d'etudiant-----
        Genre_label = Label(Frame_managment, text="genre d'etudiant", bg="white")
        Genre_label.pack()
        Entry_Genre = ttk.Combobox(Frame_managment,textvariable= self.gender)
        Entry_Genre['value'] = ('Homme', "femme")
        Entry_Genre.pack()
                # -----Address d'etudiant-----
        add_label = Label(Frame_managment, text="L'addresse d'etudiant", bg="white")
        add_label.pack()
        Entry_Add = Entry(Frame_managment, bd='2',textvariable= self.addresse,  justify='center')
        Entry_Add.pack()
                # -----Delete d'etudiant-----
        Delete_label = Label(Frame_managment,fg= 'red', text="Supprimer un etudiant (ID)", bg="white")
        Delete_label.pack()
        Entry_Delete = Entry(Frame_managment, bd='2',textvariable= self.delete,  justify='center')
        Entry_Delete.pack()
        #----------Panneau de contrôle------------
        Frame_buttons = Frame(self.root, bg='white')
        Frame_buttons.place(x=1137, y=437, width=210, h=253)
                #--------------lable de panneau-----------
        Delete_label = Label(Frame_buttons, fg='white', text="Panneau de contrôle", bg="#674188")
        Delete_label.pack(fill=X)
                #--------------buttons-------------------------
        add_btn= Button(Frame_buttons, text="Ajouter", bg="#674188", fg="white",command=self.Add_Student)
        add_btn.place(x=33,y=33,width=150,h=33)

        delete_btn =Button(Frame_buttons, text="Supprimer", bg="#674188", fg="white",command=self.Delete)
        delete_btn.place(x=33,y=70,width=150,h=33)

        update_btn =Button(Frame_buttons, text="Modifier", bg="#674188", fg="white",command=self.Update)
        update_btn.place(x=33,y=107,width=150,h=33)

        clear_btn =Button(Frame_buttons, text="Vider", bg="#674188", fg="white", command=self.Clear)
        clear_btn.place(x=33,y=144,width=150,h=33)

        about_btn = Button(Frame_buttons, text="About us", bg="#674188", fg="white", command=self.About)
        about_btn.place(x=33,y=181,width=150,h=33)

        exit_btn = Button(Frame_buttons, text="Exite", bg="#674188", fg="white", command=root.quit)
        exit_btn.place(x=33,y=218,width=150,h=33)

        # --------------- Frame Search ---------------------------------
        Frame_Rech = Frame(self.root, bg='white')
        Frame_Rech.place(x=1, y=30, width=1134, h=30)

            #------------- Recherche-------------------------------------

        Box_Search = ttk.Combobox(Frame_Rech, textvariable=self.search_var, justify='center')
        Box_Search['value'] = ('_id', "name", "gender", "tel")
        Box_Search.place(x=880, y=12)

        Entry_search = Entry(Frame_Rech, bd='2', textvariable=self.search, justify='center')
        Entry_search.place(x=730, y=12)

        Search_btn =Button(Frame_Rech, text="Rechercher", bg="#EBC7E6", fg="white", command=self.Search)
        Search_btn.place(x=620, y=2, width=100, h=30)

        # --------------- Frame Données---------------------------------
        Frame_Donnees = Frame(self.root, bg='#EBC7E6')
        Frame_Donnees.place(x=1, y=60, width=1134, h=630)

        Scrool_X = Scrollbar(Frame_Donnees, orient=HORIZONTAL)
        Scrool_Y = Scrollbar(Frame_Donnees, orient=VERTICAL)

        self.student_table = ttk.Treeview(Frame_Donnees,
                                          columns = ('Id','Nom', 'Email','Tel','certificats','gender','Addresse'),
                                          xscrollcommand = Scrool_X.set,
                                          yscrollcommand = Scrool_Y.set
                                          )
        self.student_table.place(x=18,y=1,width=1130,h=600)
        Scrool_X.pack(side= BOTTOM,fill=X)
        Scrool_Y.pack(side= LEFT,fill=Y)

        self.student_table['show'] = 'headings'
        self.student_table.heading('Id',text="ID")
        self.student_table.heading('Nom',text="Nom")
        self.student_table.heading('Email',text="Email")
        self.student_table.heading('Tel',text="Tel")
        self.student_table.heading('certificats',text="certificats")
        self.student_table.heading('gender',text="gender")
        self.student_table.heading('Addresse',text="Addresse")

        self.student_table.column('Id',width=17)
        self.student_table.column('Nom',width=100)
        self.student_table.column('Email',width=70)
        self.student_table.column('Tel',width=65)
        self.student_table.column('certificats',width=65)
        self.student_table.column('gender',width=30)
        self.student_table.column('Addresse',width=125)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_all()
    def Add_Student(self):
        cnx = MongoClient(host='localhost',port=27017)
        db = cnx.Gestion_S
        Student_Coll = db.Student
        Student = {"_id" : self.id.get(),
                   "name": self.Nom.get(),
                   "email": self.Email.get(),
                   "tel": self.Tel.get(),
                   "certificats" : self.certificats.get(),
                   "gender" : self.gender.get(),
                   "address" : self.addresse.get()
                   }
        Student_Coll.insert_one(Student)
        self.fetch_all()
        self.Clear()



    def fetch_all(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.Gestion_S

        collection = db['Student']
        rows = list(collection.find())

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=list(row.values()))


    def Delete(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.Gestion_S
        collection = db['Student']

        collection.delete_one({'_id' : self.delete.get()})
        self.fetch_all()


    def Clear(self):
        self.id.set('')
        self.Nom.set('')
        self.Email.set('')
        self.Tel.set('')
        self.certificats.set('')
        self.gender.set('')
        self.addresse.set('')
        self.delete.set('')

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        self.id.set(row[0])
        self.Nom.set(row[1])
        self.Email.set(row[2])
        self.Tel.set(row[3])
        self.certificats.set(row[4])
        self.gender.set(row[5])
        self.addresse.set(row[6])

    def Update(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.Gestion_S
        Student_Coll = db.Student
        Student = {
                   "name": self.Nom.get(),
                   "email": self.Email.get(),
                   "tel": self.Tel.get(),
                   "certificats": self.certificats.get(),
                   "gender": self.gender.get(),
                   "address": self.addresse.get()
                   }
        Student_Coll.update_one({"_id": self.id.get()},{"$set" : Student})
        self.fetch_all()
        self.Clear()

    def Search(self):
        cnx = MongoClient(host='localhost', port=27017)
        db = cnx.Gestion_S

        collection = db['Student']
        rows = list(collection.find({str(self.search_var.get()) : str(self.search.get())}))

        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=list(row.values()))

    def About(self):
        messagebox.showinfo('developper Berroho Ibtissam', 'Welcome to our first project')










root = Tk()
object = Student(root)
root.mainloop()