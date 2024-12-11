from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # ================================================creating Variable=========================================

        self.nameoftable=StringVar()
        self.ref=StringVar()
        self.dose=StringVar()
        self.lot=StringVar()
        self.nooftablet=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.drname=StringVar()

        self.patientid=StringVar()
        self.patientname=StringVar()
        self.address=StringVar()
        self.contact=StringVar()
        self.bloodgroup=StringVar()
        self.occupation=StringVar()
        self.roomno=StringVar()
        







        lbltitle=Label(self.root,bd=10,relief=RIDGE,text="Hospital Management System",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # =======================Data Frame===========================================================================

        Dataframe=Frame(self.root,bd=10,relief=RIDGE)
        Dataframe.place(x=0,y=100,width=1265,height=290)
        
        DataframeLeft=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,
                                        font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=800,height=250)
        DataframeRight=LabelFrame(Dataframe,bd=5,relief=RIDGE,padx=10,
                                        font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=810,y=5,width=420,height=250)

    #   ===================Button Frame=============================================================================

        Buttonframe=Frame(self.root,bd=10,relief=RIDGE)
        Buttonframe.place(x=0,y=400,width=1265,height=60)

        # ==========================Detail Frame==========================================================================

        Detailsframe=Frame(self.root,bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=470,width=1265,height=150)

        # ===========================================DataframeLeft============================================================

        lblNameTablet=Label(DataframeLeft,font=("arial",12,"bold"),text="Name of Tablet",padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.nameoftable,font=("arial",12,"bold"),width=20)
        comNametablet["values"]=("Paracetamol","Nice","coronavirus vaccine","Ativan","Cepon")
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Reference",padx=2)
        lblref.grid(row=1,column=0)
        txtref=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ref,width=20)
        txtref.grid(row=1,column=1)

        lbldose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose",padx=2)
        lbldose.grid(row=2,column=0)
        txtdose=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.dose,width=20)
        txtdose.grid(row=2,column=1)

        lblnooftablet=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablet",padx=2)
        lblnooftablet.grid(row=3,column=0)
        txtnooftablet=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nooftablet,width=20)
        txtnooftablet.grid(row=3,column=1)

        lblnooflot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot",padx=2)
        lblnooflot.grid(row=4,column=0)
        txtnooflot=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.lot,width=20)
        txtnooflot.grid(row=4,column=1)

        lblissuedate=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date",padx=2)
        lblissuedate.grid(row=5,column=0)
        txtissuedate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.issuedate,width=20)
        txtissuedate.grid(row=5,column=1)

        lblexpdate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date",padx=2)
        lblexpdate.grid(row=6,column=0)
        txtexpdate=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.expdate,width=20)
        txtexpdate.grid(row=6,column=1)
        
        lbldrname=Label(DataframeLeft,font=("arial",12,"bold"),text="Dr Name",padx=2)
        lbldrname.grid(row=6,column=0)
        txtdrname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.drname,width=20)
        txtdrname.grid(row=6,column=1)



        

        lblpatientid=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient ID",padx=2)
        lblpatientid.grid(row=0,column=2)
        txtpatientid=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.patientid,width=20)
        txtpatientid.grid(row=0,column=3)

        lblpatientname=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name",padx=2)
        lblpatientname.grid(row=1,column=2)
        txtpatientname=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.patientname,width=20)
        txtpatientname.grid(row=1,column=3)

        lbladdress=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablet",padx=2)
        lbladdress.grid(row=2,column=2)
        txtaddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.address,width=20)
        txtaddress.grid(row=2,column=3)

        lblcontact=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot",padx=2)
        lblcontact.grid(row=3,column=2)
        txtcontact=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.contact,width=20)
        txtcontact.grid(row=3,column=3)

        lblbloodgroup=Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date",padx=2)
        lblbloodgroup.grid(row=4,column=2)
        txtbloodgroup=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.bloodgroup,width=20)
        txtbloodgroup.grid(row=4,column=3)

        lbloccupation=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date",padx=2)
        lbloccupation.grid(row=5,column=2)
        txtoccupation=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.occupation,width=20)
        txtoccupation.grid(row=5,column=3)
        
        lblroomno=Label(DataframeLeft,font=("arial",12,"bold"),text="Room no",padx=2)
        lblroomno.grid(row=6,column=2)
        txtroomno=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.roomno,width=20)
        txtroomno.grid(row=6,column=3)

        # ====================================DataframeRight===================================================================

        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=42,height=10,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        # ========================Buttonframe==================================================================================

        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Prescription Data",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",8,"bold"),width=28,height=10,padx=2,pady=6)
        btnExit.grid(row=0,column=5)

    #    ============================Detailframe Table===============================================================================
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftable","ref","dose","nooftablet","lot","issuedate","expdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference no")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablet",text="No of Tablet")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")

        self.hospital_table["show"]="headings"

        self.hospital_table.pack(fill=BOTH,expand=1)

        # ==============================================Functionality decelaration=========================================

        def iPrescreptionData(self):
            if self.nameoftable()=="" or self.ref.get()=="":
                messagebox.showerror("error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
                my_cursor=conn.cursor() 
                my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                         self.nameoftable(),
                                                                                        
                                                                                         self.ref(),
                                                                                         self.dose(),
                                                                                         self.lot(),
                                                                                         self.nooftablet(),
                                                                                         self.issuedate(),
                                                                                         self.expdate(),
                                                                                         self.drname(),
                                                                                         self.patientid(),
                                                                                
                                                                                         self.patientname(),
                                                                                         self.address(),
                                                                                         self.contactself.contact(),
                                                                                         self.bloodgroup(),
                                                                                         self.occupation(),
                                                                                         self.roomno(),
                                                                                         ))
                conn.commit()
                conn.close() 
                messagebox.showinfo("success","record has been inserted")
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Test@123",database="mydata")
        my_cursor=conn.cursor() 
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            




                                                                                          

            



        
root=Tk()
ob=Hospital(root)
root.mainloop()
