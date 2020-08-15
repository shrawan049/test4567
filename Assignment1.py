from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import random
import time;
import datetime
import tempfile
import os

class Pharmacy:
    def __init__(self,root):
        self.root= root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1170x850") 
        self.root.configure(background="blue")

        cmbNametablets= StringVar()
        Ref= StringVar()
        Dose=StringVar()
        ItemsName= StringVar()
        IssuedDate= StringVar()
        ExpDate= StringVar()
        Name= StringVar()
        Address= StringVar()
        ContactDetails= StringVar()
        Reff=StringVar()
        Prescription= StringVar()


        def iExit():
            iExit= tkinter.messagebox.askyesno("Do you want to exit?")
            if iExit>0:
                root.destroy()
                return 

        def iPrescription():
                self.txtPrescription.insert(END, "Name of Tablets: \t\t" + ItemsName.get()+ "\n" )
                return

        def iPrescriptionData():
                op= messagebox.askyesno("save data" , "Do you want to save data?")
                if op==1:
                        try:
                                self.txtFrameDetail.insert(END, cmbNametablets.get()+ "\t"+  Ref.get()+ "\t" + ItemsName.get()+ "\t" + Dose.get()+ "\t"+ IssuedDate.get()+ "\t"+
                                ExpDate.get()+
                                "\t" + Name.get()+ "\t" + Address.get()+ "\t" + ContactDetails.get()+ "\t" + Reff.get() + "\n" )

                                f1=open("data/"+ str(self.iPrescriptionData.get()) +".txt" , "a")
                                f1.write(self.iprescriptionData)
                                f1.close()
                        except TypeError:
                                messagebox.showerror("error", "data not saved")
                else:
                    return

        def iDelete():
                cmbNametablets.set("")
                self.cboNameTablet.current(0)
                Ref.set("")
                Dose.set("")
                ItemsName.set("")
                IssuedDate.set("")
                ExpDate.set("")
                Name.set("")
                Address.set("") 
                ContactDetails.set("")
                Reff.set("")                             
                return
        
        def iPrint():
                q= self.txtFrameDetail.get("1.0", "end-1c")
                filename=tempfile.mktemp(".txt")
                open(filename, "w").write(q)
                os.startfile(filename, "print")


            
        def iReset():
                cmbNametablets.set("")
                self.cboNameTablet.current(0)
                Ref.set("")
                Dose.set("")
                ItemsName.set("")
                IssuedDate.set("")
                ExpDate.set("")
                Name.set("")
                Address.set("") 
                ContactDetails.set("")
                Reff.set("")                             
                self.txtPrescription.delete("1.0", END)
                self.txtFrameDetail.delete("1.0", END)           
                return

            
            
        MainFrame= Frame(self.root)

        MainFrame.grid()

        TitleFrame= Frame(MainFrame, bd=20, width=1000, padx=20, relief=RIDGE, bg="light blue")
        TitleFrame.pack(side=TOP)

        self.lblTitle= Label(TitleFrame, font= ("arial", 40, "bold"), fg="Red", text= "24/7 Pharmacy", bg="light blue")
        self.lblTitle.grid()

        FrameDetail= Frame(MainFrame, bd=20, width=200, height=90, padx=4, pady=4, bg="light blue", relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        ButtonFrame= Frame(MainFrame, bd=20, width=200, height=90, padx=10, pady=5, bg= "light blue", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
#----------------------------------------------------DataFrame---------------------------------------------------------------------------------------------------
        DataFrame= Frame(MainFrame, bd=10, width=520, height=100, padx=8, pady=8, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)
#----------------------------------------------------DataFrame Right---------------------------------------------------------------------------------------------
        DataFrameRIGHT= Frame(DataFrame, bd=10, width=600, height=100, padx=40, pady=40, bg= "light blue", relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

        self.lblPrescriptions= Label(DataFrameRIGHT, font= ("arial", 15, "bold"), text= "Prescriptions:", fg="black", bg="light blue")
        self.lblPrescriptions.grid(row=0, column=0, sticky=W)
        self.txtPrescription= Text(DataFrameRIGHT, font= ("arial", 12, "italic"), width=30, height=9, padx=5, pady=10)
        self.txtPrescription.grid(row=1, column=0)
            
#--------------------------------------------------DataFrame Left-------------------------------------------------------------------------------------------------

        DataFrameLEFT= Frame(DataFrame, bd=20, width=600, height=300, padx=40, pady=40, bg="light blue", relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        self.lblDetails= Label(DataFrameLEFT, font= ("arial", 20, "italic"), text= "Patient Details:", bg="light yellow")
        self.lblDetails.grid(row=0, column=0, sticky=W)


        self.lblquantity= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "No of items:")
        self.lblquantity.grid(row=1, column=0, sticky=W)

        self.cboNameTablet= ttk.Combobox(DataFrameLEFT, textvariable=cmbNametablets , state="readonly", font= ("arial", 20, "bold"), width=5)
        self.cboNameTablet["value"]=("", "1", "2", "3", "4", "5","6", "7", "8", "9", "10")
        self.cboNameTablet.current(0)
        self.cboNameTablet.grid(row=1, column=1)

        
        self.lblRef= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Reference No.")
        self.lblRef.grid(row=1, column=2, sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= Ref)
        self.txtRef.grid(row=1, column=3)

        

        self.lblNameTablet= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Name of items:")
        self.lblNameTablet.grid(row=2, column=0, sticky=W)
        self.txtNameTablet = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= ItemsName)
        self.txtNameTablet.grid(row=2, column=1)

        self.lblDose= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Doses(per day):")
        self.lblDose.grid(row=2, column=2, sticky=W)
        self.txtDose = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= Dose)
        self.txtDose.grid(row=2, column=3)       

        self.lblIssuedDate= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Issued Date:")
        self.lblIssuedDate.grid(row=3, column=0, sticky=W)
        self.txtIssuedDate = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= IssuedDate)
        self.txtIssuedDate.grid(row=3, column=1)

        self.lblExpDate= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Expiry Date:")
        self.lblExpDate.grid(row=3, column=2, sticky=W)
        self.txtExpDate = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= ExpDate)
        self.txtExpDate.grid(row=3, column=3)

        self.lblName= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Patients Name:")
        self.lblName.grid(row=4, column=0, sticky=W)
        self.txtName = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= Name)
        self.txtName.grid(row=4, column=1)

        self.lblAddress= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Address:")
        self.lblAddress.grid(row=4, column=2, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= Address)
        self.txtAddress.grid(row=4, column=3)
  
        self.lblContactDetails= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Contact Details:")
        self.lblContactDetails.grid(row=5, column=0, sticky=W)
        self.txtContactDetails = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= ContactDetails)
        self.txtContactDetails.grid(row=5, column=1)

        self.lblReff= Label(DataFrameLEFT, font= ("arial", 15, "italic"), text= "Referred By:")
        self.lblReff.grid(row=5, column=2, sticky=W)
        self.txtReff = Entry(DataFrameLEFT, font=("arial", 10, "bold"), textvariable= Reff)
        self.txtReff.grid(row=5, column=3)
#--------------------------------------------Adding Buttons-----------------------------------------------------------------------------------------------------------      
        self.btnPrescription= Button(ButtonFrame, text="prescriptions", font=("arial", 12, "bold"), width=13, 
                                                            command=iPrescription)
        self.btnPrescription.grid(row=0, column=0)

        
        self.btnPrescriptionData= Button(ButtonFrame, text="Prescription Data", font=("arial", 12, "bold"), width=13,
                                                    command=iPrescriptionData)
        self.btnPrescriptionData.grid(row=0, column=1)

        self.btnPrint= Button(ButtonFrame, text="print", font=("arial", 12, "bold"), width=13, 
                                                            command=iPrint)
        self.btnPrint.grid(row=0, column=2)


        self.btnDelete= Button(ButtonFrame, text="Delete", font=("arial", 12, "bold"), width=13,
                                                    command=iDelete)
        self.btnDelete.grid(row=0, column=3)

        self.btnReset= Button(ButtonFrame, text="Reset", font=("arial", 12, "bold"), width=13,
                                                    command=iReset)
        self.btnReset.grid(row=0, column=4)

        self.btnExit= Button(ButtonFrame, text="exit", font=("arial", 12, "bold"), width=13,
                                                    command=iExit )
        self.btnExit.grid(row=0, column=5)

#------------------------------------------FrameDetail--------------------------------------------------------------------------------------------------------------------

        self.lblLabel= Label(FrameDetail, font=("arial", 11, "bold"), pady= 5, 
                    text= "No. of Items\tRef. No.\t Name of Tablets\t Doseage\t Issued Date\t Exp. Date\tPatients Name\tAddress\t Contact Details\t Referred By" )
        self.lblLabel.grid(row=0, column=0)

        self.txtFrameDetail= Text(FrameDetail, font=("arial", 12, "bold"), width=124, height=8, padx=2, pady=4)
        self.txtFrameDetail.grid(row=1, column=0)






        
if __name__ == "__main__":
    root=Tk()
    application = Pharmacy(root)
    root.mainloop()
