#Create a database named "login" in sql and create a table named "info" with columns name userid(primary key) , password.
#Copy the text given below to create it.
'''
create database login;
use login;
create table info(userid varchar(50) primary key);
alter table info add password varchar(50)
'''
#FUNCTIONS
def destroy():
    w.destroy()

def checkin1(p,c):
    if c=="CNF":
        C = Canvas(w, bg="blue", height=250, width=300)
        filename = PhotoImage(file = "verified.png")
        background_label = Label(w, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        l="update passenger set checkin="+"'"+c+"'"+"where PNR="+"'"+p+"'"
        mycursor.execute(l)
        mydb.commit()
        Done=Button(w,width=15,text="Confirm",command=destroy,bg="light green",font=("times now roman",12)).place(x=125,y=600)
        mainloop()
    else:
        C = Canvas(w, bg="blue", height=250, width=300)
        filename = PhotoImage(file = "cancelled.png")
        background_label = Label(w, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        l="update passenger set checkin="+"'"+c+"'"+"where PNR="+"'"+p+"'"
        mycursor.execute(l)
        mydb.commit()
        Done=Button(w,width=15,text="Confirm",command=destroy,bg="light green",font=("times now roman",12)).place(x=125,y=600)
        mainloop()
def checkin():
    def verify(pnr1,contact1):
        def checkin(p,c):
            if c=="CNF":
                messagebox.showinfo("CONFIRMATION","WEB CHECKIN DONE")
                l="update passenger set checkin="+"'"+c+"'"+"where PNR="+"'"+p+"'"
                mycursor.execute(l)
                mydb.commit()
                Done=Button(w,width=15,text="Confirm",command=destroy,bg="light green",font=("times now roman",12)).place(x=125,y=600)
                mainloop()
            else:
                messagebox.showerror("CONFIRMATION","TICKET CANCELED")
                l="update passenger set checkin="+"'"+c+"'"+"where PNR="+"'"+p+"'"
                mycursor.execute(l)
                mydb.commit()
                Done=Button(w,width=15,text="Confirm",command=destroy,bg="light green",font=("times now roman",12)).place(x=125,y=600)
                mainloop()
        p=pnr1.get()
        b=contact1.get()
        l="select Contact_number from passenger where PNR ="+"'"+p+"'"
        mycursor.execute(l)
        for i in mycursor:
            c=(i[0])
            if c==b:
                C = Canvas(w, bg="blue", height=250, width=300)
                filename = PhotoImage(file = "showt.png")
                background_label = Label(w, image=filename)
                background_label.place(x=0, y=0, relwidth=1, relheight=1)
                C.pack()
                #show tickets details
                l="select * from passenger where PNR ="+"'"+p+"'"+";"
                mycursor.execute(l)
                a=[]
                for i in mycursor:
                    a.append(i[0])
                    a.append(i[1])
                    a.append(i[2])
                    a.append(i[3])
                    a.append(i[4])
                    a.append(i[5])
                    a.append(i[6])
                    a.append(i[7])
                    a.append(i[8])
                    a.append(i[9])
                    a.append(i[10])
                    a.append(i[11])
                    a.append(i[12])
                det = Label( w,width=20,text="Name: "+str(a[0]),bg="light blue",font=("times now roman",16)).place(x=20,y=80)
                det = Label( w,width=10,text="Age: "+str(a[1]),bg="light blue",font=("times now roman",16)).place(x=270,y=80)
                det = Label( w,width=10,text="Sex: "+str(a[2]),bg="light blue",font=("times now roman",16)).place(x=400,y=80)
                det = Label( w,width=30,text="Contact Number:"+str(a[3]),bg="light blue",font=("times now roman",16)).place(x=530,y=80)
                det = Label( w,width=18,text="From:"+str(a[4]),bg="light blue",font=("times now roman",16)).place(x=900,y=80)
                det = Label( w,width=18,text="To:"+str(a[5]),bg="light blue",font=("times now roman",16)).place(x=1125,y=80)
                det = Label( w,width=20,text="Number Of Tickets:"+str(a[6]),bg="light blue",font=("times now roman",16)).place(x=20,y=160)
                det = Label( w,width=15,text="Class:"+str(a[7]),bg="light blue",font=("times now roman",16)).place(x=280,y=160)
                det = Label( w,width=15,text="Date:"+str(a[8])+"  "+str(a[9]),bg="light blue",font=("times now roman",16)).place(x=480,y=160)
                det = Label( w,width=20,text="PNR:"+str(a[10]),bg="light blue",font=("times now roman",16)).place(x=680,y=160)
                det = Label( w,width=30,text="Aadhar Number:"+str(a[12]),bg="light blue",font=("times now roman",16)).place(x=940,y=160)
                confirm=Button(w,width=15,text="Confirm",command=lambda:checkin(p,'CNF'),bg="light green",font=("times now roman",12)).place(x=100,y=450)
                cancle=Button(w,width=15,text="Cancle",command=lambda:checkin(p,'CNL'),bg="Red",font=("times now roman",12)).place(x=250,y=450)
                mainloop()
            else:
                messagebox.showerror("INVALID","Access Denied")
                Done=Button(w,width=15,text="Done",command=destroy,bg="light green",font=("times now roman",12)).place(x=120,y=600)
                w.destroy()
                mainloop()
                
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "checkin.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=20,text="PNR: ",bg="black",fg="white",font=("times now roman",16)).place(x=120,y=140)
    det = Label( w,width=20,text="Contact Number: ",bg="black",fg="white",font=("times now roman",16)).place(x=120,y=285)
    C.pack()
    pnr1=Entry(w,width=55,bg="white")
    pnr1.place(x=120,y=170)
    contact1=Entry(w,width=55,bg="white")
    contact1.place(x=120,y=310)
    det = Label( w,width=20,text="Web - Checkin Page",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    Done=Button(w,width=15,text="Done",command=lambda:verify(pnr1,contact1),bg="white",font=("times now roman",12)).place(x=120,y=600)
    mainloop()
    
def verify(pnr1,aadhar1):
    a=pnr1.get()
    b=aadhar1.get()
    l="select Aadhar_number from passenger where PNR ="+"'"+a+"'"+";"
    mycursor.execute(l)
    for i in mycursor:
        c=(i[0])
        if c==b:
            C = Canvas(w, bg="blue", height=250, width=300)
            filename = PhotoImage(file = "showt.png")
            background_label = Label(w, image=filename)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            l="select * from passenger where PNR ="+"'"+a+"'"+";"
            mycursor.execute(l)
            a=[]
            for i in mycursor:
                a.append(i[0])
                a.append(i[1])
                a.append(i[2])
                a.append(i[3])
                a.append(i[4])
                a.append(i[5])
                a.append(i[6])
                a.append(i[7])
                a.append(i[8])
                a.append(i[9])
                a.append(i[10])
                a.append(i[11])
                a.append(i[12])
            det = Label( w,width=20,text="Name: "+str(a[0]),bg="light blue",font=("times now roman",16)).place(x=20,y=80)
            det = Label( w,width=10,text="Age: "+str(a[1]),bg="light blue",font=("times now roman",16)).place(x=270,y=80)
            det = Label( w,width=10,text="Sex: "+str(a[2]),bg="light blue",font=("times now roman",16)).place(x=400,y=80)
            det = Label( w,width=30,text="Contact Number:"+str(a[3]),bg="light blue",font=("times now roman",16)).place(x=530,y=80)
            det = Label( w,width=18,text="From:"+str(a[4]),bg="light blue",font=("times now roman",16)).place(x=900,y=80)
            det = Label( w,width=18,text="To:"+str(a[5]),bg="light blue",font=("times now roman",16)).place(x=1125,y=80)
            det = Label( w,width=20,text="Number Of Tickets:"+str(a[6]),bg="light blue",font=("times now roman",16)).place(x=20,y=160)
            det = Label( w,width=15,text="Class:"+str(a[7]),bg="light blue",font=("times now roman",16)).place(x=280,y=160)
            det = Label( w,width=15,text="Date:"+str(a[8])+"  "+str(a[9]),bg="light blue",font=("times now roman",16)).place(x=480,y=160)
            det = Label( w,width=20,text="PNR:"+str(a[10]),bg="light blue",font=("times now roman",16)).place(x=680,y=160)
            det = Label( w,width=30,text="Aadhar Number:"+str(a[12]),bg="light blue",font=("times now roman",16)).place(x=940,y=160)
            det = Label( w,width=45,text="YOU HAVE BEEN VERIFIED TO ENTER THE STATION",bg="white",fg="dark blue",font=("times now roman",16)).place(x=425,y=300)
            C.pack()
            Done=Button(w,width=15,text="Done",command=destroy,bg="white",font=("times now roman",12)).place(x=120,y=600)
            mainloop()
        else:
            messagebox.showerror("Invalid Details","Verification Denied")
            destroy()

def PNR():
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "pnr.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=12,text="PNR Number: ",bg="red",font=("times now roman",16)).place(x=125,y=125)
    det = Label( w,width=15,text="Aadhar Number: ",bg="red",font=("times now roman",16)).place(x=125,y=235)
    C.pack()
    pnr1=Entry(w,width=27,bg="lightgrey")
    pnr1.place(x=125,y=160)
    aadhar1=Entry(w,width=32,bg="lightgrey")
    aadhar1.place(x=125,y=270)
    Done=Button(w,width=15,text="Verify",command=lambda:verify(pnr1,aadhar1),bg="light green",font=("times now roman",12)).place(x=120,y=600)
    det = Label( w,width=20,text="PNR Verification Page",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    mainloop()

def details(trains1,PNR,seats):
    def show(seats):
        train=trains1.get()
        train=train[:-4:1]
        Name=name1.get()
        Age=Age1.get()
        Sex=Sex1.get()
        pnr=str(PNR)
        Contact_Number=Contact_Number1.get()
        Aadhar_number=Aadhar_Number1.get()
        if len(Contact_Number)==10 and len(Aadhar_number)==12:
            True
        elif len(Contact_Number)!=10:
            messagebox.showerror("RETRY", "Please Enter Valid Contact Number")
            details(trains1,pnr,seats)
        else:
            messagebox.showerror("RETRY", "Please Enter Valid Aadhar Number")
            details(trains1,pnr,seats)
        l="update passenger set Name="+"'" + Name + "'"+","+"Age="+"'" + Age +"'"+","+"Sex="+"'" + Sex + "'" + "," +"Contact_Number="+"'" + Contact_Number +"'"+ "," +"Aadhar_number="+"'" + Aadhar_number + "'""," +"train="+"'" + train + "'"+"where PNR="+"'"+pnr+"'"
        mycursor.execute(l)
        l="update trains set seat=seat-"+"'"+seats+"'"+"where train like"+"'"+train[0:5]+"%'"+";"
        mycursor.execute(l)
        mydb.commit()
        l="select * from passenger where PNR ="+"'"+pnr+"'"+";"
        mycursor.execute(l)
        C = Canvas(w, bg="blue", height=250, width=300)
        filename = PhotoImage(file = "showt.png")
        background_label = Label(w, image=filename)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        C.pack()
        a=[]
        for i in mycursor:
            a.append(i[0])
            a.append(i[1])
            a.append(i[2])
            a.append(i[3])
            a.append(i[4])
            a.append(i[5])
            a.append(i[6])
            a.append(i[7])
            a.append(i[8])
            a.append(i[9])
            a.append(i[10])
            a.append(i[11])
            a.append(i[12])
        det = Label( w,width=20,text="Name: "+str(a[0]),bg="light blue",font=("times now roman",16)).place(x=20,y=80)
        det = Label( w,width=10,text="Age: "+str(a[1]),bg="light blue",font=("times now roman",16)).place(x=270,y=80)
        det = Label( w,width=10,text="Sex: "+str(a[2]),bg="light blue",font=("times now roman",16)).place(x=400,y=80)
        det = Label( w,width=30,text="Contact Number:"+str(a[3]),bg="light blue",font=("times now roman",16)).place(x=530,y=80)
        det = Label( w,width=18,text="From:"+str(a[4]),bg="light blue",font=("times now roman",16)).place(x=900,y=80)
        det = Label( w,width=18,text="To:"+str(a[5]),bg="light blue",font=("times now roman",16)).place(x=1125,y=80)
        det = Label( w,width=20,text="Number Of Tickets:"+str(a[6]),bg="light blue",font=("times now roman",16)).place(x=20,y=160)
        det = Label( w,width=15,text="Class:"+str(a[7]),bg="light blue",font=("times now roman",16)).place(x=280,y=160)
        det = Label( w,width=15,text="Date:"+str(a[8])+"  "+str(a[9]),bg="light blue",font=("times now roman",16)).place(x=480,y=160)
        det = Label( w,width=20,text="PNR:"+str(a[10]),bg="light blue",font=("times now roman",16)).place(x=680,y=160)
        det = Label( w,width=30,text="Aadhar Number:"+str(a[12]),bg="light blue",font=("times now roman",16)).place(x=940,y=160)
        messagebox.showinfo("BOOKING", "Ticket Booking Successful")
        #ticket status
        Done=Button(w,width=20,text="Do WEB CHECKIN later",command=destroy,bg="light green",font=("times now roman",12)).place(x=120,y=600)
        mainloop()
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "details.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=5,text="Name: ",bg="orange",font=("times now roman",16)).place(x=225,y=120)
    det = Label( w,width=5,text="Age: ",bg="orange",font=("times now roman",16)).place(x=225,y=207)
    det = Label( w,width=5,text="Sex: ",bg="orange",font=("times now roman",16)).place(x=225,y=285)
    det = Label( w,width=17,text="Contact Number: ",bg="orange",font=("times now roman",16)).place(x=225,y=380)
    det = Label( w,width=17,text="Aadhar Number: ",bg="orange",font=("times now roman",16)).place(x=225,y=468)
    det = Label( w,width=20,text="Personal Details",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    C.pack()
    name1=Entry(w,width=55,bg="lightgrey")
    name1.place(x=320,y=120)
    Age1=Entry(w,width=55,bg="lightgrey")
    Age1.place(x=320,y=207)
    OPTIONS = [
        "Male",
        "Female",
        "Others"
    ]
    Sex1 = StringVar(w)
    Sex1.set(OPTIONS[0])
    p = OptionMenu(w, Sex1,*OPTIONS)
    p.place(x=320,y=285)
    Contact_Number1=Entry(w,width=55,bg="lightgrey")
    Contact_Number1.place(x=450,y=380)
    Aadhar_Number1=Entry(w,width=55,bg="lightgrey")
    Aadhar_Number1.place(x=450,y=468)
    Done=Button(w,width=15,text="Done",command=lambda:show(seats),bg="orange",font=("times now roman",12)).place(x=120,y=600)
    mainloop()

def trains(pnr,Fr_om,t_o,seats):
    l="SELECT * FROM trains WHERE Fr_m ="+"'"+Fr_om+"'"+" AND t_o ="+"'"+t_o+"'";
    mycursor.execute(l)
    det = Label( w,width=30,text="Available Trains And Seats",bg="light blue",font=("times now roman",16)).place(x=650,y=100)
    Y=100
    t=[]
    s=[]
    for i in mycursor:
        t.append(i[2]+","+i[4])
    trains1 = StringVar(w)
    trains1.set(t[0])
    p = OptionMenu(w, trains1,*t)
    p.place(x=650,y=200)
    Done=Button(w,width=5,text="Book",command=lambda:details(trains1,pnr,seats),bg="orange",font=("times now roman",12)).place(x=825,y=200)
       
def book():
    pnr=random.randint(111111,999999)
    def show():
        Fr_om=From1.get()
        t_o=To1.get()
        Seats=Seats1.get()
        Class=Class1.get()
        Date=Date1.get()
        Month=Month1.get()
        Year=Year1.get()
        PNR=str(pnr)
        checkin="PND"
        l="insert into passenger (Fr_om , t_o , Seats , Class , Date ,Month ,Year, PNR, checkin ) values ("+ "'" + Fr_om + "'" + "," + "'" + t_o + "'" + "," + "'" + Seats + "'" + ","+ "'" + Class + "'" + ","+ "'" + Date + "'" +","+ "'" + Month + "'"  + ","+ "'" + Year + "'"  + "," + "'" + PNR + "'" + "," + "'" + checkin + "'" + ")"
        mycursor.execute(l)
        mydb.commit()
        trains(PNR,Fr_om,t_o,Seats)
        
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "booking.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=6,text="From: ",bg="orange",font=("times now roman",16)).place(x=225,y=105)
    det = Label( w,width=6,text="To: ",bg="orange",font=("times now roman",16)).place(x=225,y=190)
    det = Label( w,width=6,text="Date: ",bg="orange",font=("times now roman",16)).place(x=225,y=275)
    det = Label( w,width=19,text="Number Of Passengers: ",bg="orange",font=("times now roman",16)).place(x=225,y=365)
    det = Label( w,width=6,text="Class: ",bg="orange",font=("times now roman",16)).place(x=225,y=445)
    C.pack()
    OPTIONS = [
    "Delhi,NDLS",
    "Jaipur,JP",
    "Kolkata,KOAA",
    "Banglore,YPR",
    "Chennei,MAS",
    "Vijayawada",
    "Kanpur,CNB",
    "Lucknow,LKO",
    "Kharagpur,KGP",
    "Cuttack,CTC"
    ]
    From1 = StringVar(w)
    From1.set(OPTIONS[0])
    p = OptionMenu(w, From1,*OPTIONS)
    p.place(x=325,y=105)
    OPTIONS = [
    "Mumbai,LTT",
    "Gorakhpur,GKP",
    "Jalpaiguri,NJP",
    "Mangaluru,MAJN",
    "Patna,PNBE",
    "Varanasi,BSB",
    "Sealadah,SDAH",
    "Vishakhapatnam,VSKP",
    "Nagpur,NGP",
    "Pragayraj,PRY"
    ]
    To1 = StringVar(w)
    To1.set(OPTIONS[0])
    p = OptionMenu(w, To1,*OPTIONS)
    p.place(x=325,y=190)
    OPTIONS = [
    "1",
    "2",
    "3",
    "4",
    "5"
    ]
    Seats1 = StringVar(w)
    Seats1.set(OPTIONS[0])
    p = OptionMenu(w, Seats1,*OPTIONS)
    p.place(x=480,y=365)
    OPTIONS = [
    "AC-1",
    "AC-2",
    "SL",
    "CC"
    ]
    Class1 = StringVar(w)
    Class1.set(OPTIONS[0])
    p = OptionMenu(w, Class1,*OPTIONS)
    p.place(x=350,y=445)
    #Date
    OPTIONS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    ]
    Date1 = StringVar(w)
    Date1.set(OPTIONS[0])
    p = OptionMenu(w, Date1,*OPTIONS)
    p.place(x=340,y=275)
    
    #Month
    OPTIONS = ['January',
               'February',
               'March',
               'April',
               'May',
               'June',
               'July',
               'August',
               'September',
               'October',
               'November',
               'December'
               ]
    Month1 = StringVar(w)
    Month1.set(OPTIONS[0])
    p = OptionMenu(w, Month1,*OPTIONS)
    p.place(x=400,y=275)
    #Year
    OPTIONS = ['2023',
               '2024',
               '2025',
               '2026',
               '2027',
               '2028',
               '2029',
               '2030'
               ]
    Year1 = StringVar(w)
    Year1.set(OPTIONS[0])
    p = OptionMenu(w, Year1,*OPTIONS)
    p.place(x=500,y=275)
    det = Label( w,width=20,text="Ticket Booking Page",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    Done=Button(w,width=5,text="Done",command=show,bg="orange",font=("times now roman",16)).place(x=225,y=525)
    mainloop()
def login(userid,password):
    a=userid.get()
    b=password.get()
    l="select password from info where userid ="+"'"+a+"'"+";"
    mycursor.execute(l)
    for i in mycursor:
        c=(i[0])
        if b==c:
            messagebox.showinfo("LOGING IN", "Login Successful")
            book()
        else:
            messagebox.showerror("LOGING IN", "Wrong Password TRY AGAIN")
def newsignup(a,name1,Age1,Sex1,Contact_Number1):
    Name=name1.get()
    Age=Age1.get()
    Sex=Sex1.get()
    Contact_Number=Contact_Number1.get()
    if len(Contact_Number)!=10:
            messagebox.showerror("RETRY", "Please Enter Valid Contact Number")
            detailsregis(a)
    else:
        True
    l="update info set Name="+"'" + Name + "'"+","+"Age="+"'" + Age +"'"+","+"Sex="+"'" + Sex + "'" + "," +"Contact_Number="+"'" + Contact_Number +"'"+"where userid="+"'"+a+"'"
    mycursor.execute(l)
    mydb.commit()
    messagebox.showinfo("NEW SIGN UP", "New ID Created")
    w.destroy()

def detailsregis(a):
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "details.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=5,text="Name: ",bg="orange",font=("times now roman",16)).place(x=225,y=120)
    det = Label( w,width=5,text="Age: ",bg="orange",font=("times now roman",16)).place(x=225,y=207)
    det = Label( w,width=5,text="Sex: ",bg="orange",font=("times now roman",16)).place(x=225,y=285)
    det = Label( w,width=17,text="Contact Number: ",bg="orange",font=("times now roman",16)).place(x=225,y=380)
    det = Label( w,width=20,text="Registration Page",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    C.pack()
    name1=Entry(w,width=55,bg="lightgrey")
    name1.place(x=320,y=120)
    Age1=Entry(w,width=55,bg="lightgrey")
    Age1.place(x=320,y=207)
    OPTIONS = [
        "Male",
        "Female",
        "Others"
    ]
    Sex1 = StringVar(w)
    Sex1.set(OPTIONS[0])
    p = OptionMenu(w, Sex1,*OPTIONS)
    p.place(x=320,y=285)
    Contact_Number1=Entry(w,width=55,bg="lightgrey")
    Contact_Number1.place(x=450,y=380)
    Done=Button(w,width=15,text="Done",command=lambda:newsignup(a,name1,Age1,Sex1,Contact_Number1),bg="orange",font=("times now roman",12)).place(x=120,y=600)
    mainloop()

def register(userid,password):
    a=userid.get()
    b=password.get()
    l="insert into info (userid ,password) values ("+ "'" + a + "'" + "," + "'" + b + "'" + ")"
    mycursor.execute(l)
    mydb.commit()
    messagebox.showinfo("REGISTERED", "New Userid and Password Created")
    detailsregis(a)
    
def change(a):
    def changed():
        c=newpassword.get()
        b=newpassword2.get()
        if c==b:
            l="update info set password="+"'"+b+"'"+"where userid="+"'"+a+"'"
            mycursor.execute(l)
            mydb.commit()
            messagebox.showinfo("CHANGING PASSWORD", "Password Updated")
            w.destroy()
        else:
            messagebox.showerror("CHANGING PASSWORD", "Password Didn't matched")
    C = Canvas(w, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "login.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=25,text="Changing Password Page",bg="grey",fg="white",font=("times now roman",35)).place(x=450,y=50)
    det = Label( w,width=18,text="Enter New Password: ",bg="light blue",font=("times now roman",16)).place(x=300,y=305)
    det = Label( w,width=20,text="Re- Enter New Password: ",bg="light blue",font=("times now roman",16)).place(x=300,y=415)
    C.pack()
    user= Label(w,width=12,text = "User ID: "+str(a),font=('Helvetica',18),bg="lightgrey").place(x = 300, y = 245)
    newpassword=Entry(w,width=30,bg="lightgrey",show="*")
    newpassword.place(x=300,y=340)
    newpassword2=Entry(w,width=30,bg="lightgrey",show="*")
    newpassword2.place(x=300,y=440)
    change=Button(w,width=20,text="Change",command=changed,bg="light blue",font=("times now roman",12)).place(x=400,y=480)
    mainloop()

def changepassword(userid,password):
    a=userid.get()
    b=password.get()
    l="select password from info where userid ="+"'"+a+"'"+";"
    mycursor.execute(l)
    for i in mycursor:
        c=(i[0])
        if b==c:
            change(a)
        else:
            print("Wrong Password TRY AGAIN")
def home():
    c=Canvas(w, width = 1350, height= 760)
    filename = PhotoImage(file = "login.png")
    background_label = Label(w, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    det = Label( w,width=8,text="USER ID: ",bg="light blue",font=("times now roman",16)).place(x=300,y=275)
    det = Label( w,width=11,text="PASSWORD: ",bg="light blue",font=("times now roman",16)).place(x=300,y=395)
    det = Label( w,width=20,text="Login Page",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
    c.pack()
    userid=Entry(w,width=30,bg="lightgrey")
    userid.place(x=300,y=300)
    password=Entry(w,width=30,bg="lightgrey",show="*")
    password.place(x=300,y=420)
    login1=Button(w,width=20,text="Login",command=lambda:login(userid,password),bg="light blue",font=("times now roman",12)).place(x=400,y=480)
    register1=Button(w,width=20,text="New Sign Up",command=lambda:register(userid,password),bg="light grey",font=("times now roman",12)).place(x=270,y=550)
    changepassword11=Button(w,width=20,text="Change Password",command=lambda:changepassword(userid,password),bg="light grey",font=("times now roman",12)).place(x=520,y=550)
    mainloop()

    
#MAIN
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1111",database="railway")
mycursor=mydb.cursor()
import os
from PIL import Image as img
from PIL import ImageTk
import random
from tkinter import Tk, Label
from tkinter import *
from tkinter import messagebox
w=Tk()
w.title("IRCTC")
w.resizable(0,0)
c=Canvas(w, width = 1350, height= 760)
c.pack()
lp=PhotoImage(file="home.png")
c.create_image(0,0,anchor=NW, image=lp)
b1=Button(w,width=20,text="Ticket Booking",command=home,bg="light blue",font=("times now roman",16)).place(x=550,y=200)
b3=Button(w,width=20,text="Web Checkin",command=checkin,bg="light blue",font=("times now roman",16)).place(x=550,y=300)
b2=Button(w,width=20,text="PNR Verification",command=PNR,bg="light blue",font=("times now roman",16)).place(x=550,y=400)
det = Label( w,width=20,text="SMART TRACKS",bg="grey",fg="white",font=("times now roman",30)).place(x=450,y=50)
mainloop()
