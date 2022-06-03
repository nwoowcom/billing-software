from tkinter import*
import math,random,os
from tkinter import messagebox
import tkinter
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Ghosting Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Ghosting Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #====Variables=====
        #====Cosmatics====
        self.soap=IntVar()
        self.face_cream=IntVar()
        self.face_wash=IntVar()
        self.spray=IntVar()
        self.gell=IntVar()
        self.loshan=IntVar()
        #=====grocery===
        self.rice=IntVar()
        self.food_oil=IntVar()
        self.daal=IntVar()
        self.wheat=IntVar()
        self.sugar=IntVar()
        self.tea=IntVar()
        #====Cold Drinks====
        self.maza=IntVar()
        self.cock=IntVar()
        self.frooti=IntVar()
        self.thumbup=IntVar()
        self.limca=IntVar()
        self.sprite=IntVar()

        #===Total Product Price and tax Variable===
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.cold_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.cold_drink_tax=StringVar()

        #====Customer====
        self.c_name=StringVar()
        self.c_phone=StringVar()

        
        self.bill_no=StringVar()
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        #=======Customer Detail Frame
        f1=LabelFrame(self.root,bd=10,relief=GROOVE,text="customer Details",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        f1.place(x=0,y=60,relwidth=1)

        cname_lbl=Label(f1,text="Customer Name",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_text=Entry(f1,width=12,textvariable=self.c_name,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        
        cphn_lbl=Label(f1,text=" Phone Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphn_text=Entry(f1,width=12,textvariable=self.c_phone,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        c_bill_lbl=Label(f1,text=" Bill Number",bg=bg_color,fg="white",font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
        c_bill_text=Entry(f1,width=12,textvariable=self.search_bill,font="arial 15",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
 
        bill_btn=Button(f1,text="Search",command=self.find_bill,width=8,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=10)


        #====Cosmetic Frame=====
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=150,width=300,height=380)

        bath_lbl=Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.soap,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        face_c_lbl=Label(F2,text="Face Cream",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_c_txt=Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        face_w_lbl=Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        Hair_s_lbl=Label(F2,text="Hair Spary",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        Hair_s_txt=Entry(F2,width=10,textvariable=self.spray,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        Hair_g_lbl=Label(F2,text="Hair Gell",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        Hair_g_txt=Entry(F2,width=10,textvariable=self.gell,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        body_lbl=Label(F2,text="Body Loshan",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.loshan,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #====Grocery Frame=====
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery ",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=310,y=150,width=300,height=380)

        rice_lbl=Label(F3,text="Rice",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        rice_txt=Entry(F3,width=10,textvariable=self.rice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        oli_lbl=Label(F3,text="Food oil",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        oli_txt=Entry(F3,width=10,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        daal_lbl=Label(F3,text="Daal",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        daal_txt=Entry(F3,width=10,textvariable=self.daal,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        wheat_lbl=Label(F3,text="Wheat",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        wheat_txt=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sugar_lbl=Label(F3,text="Sugar",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sugar_txt=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        tea_lbl=Label(F3,text="Tea",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

         #====Cold Frame=====
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cold Drinks ",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=615,y=150,width=300,height=380)

        maza_lbl=Label(F4,text="Maza",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        maza_txt=Entry(F4,width=10,textvariable=self.maza,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        cock_lbl=Label(F4,text="Coca Cola",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        cock_txt=Entry(F4,width=10,textvariable=self.cock,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        frooti_lbl=Label(F4,text="Frooti",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        frooti_txt=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        up_lbl=Label(F4,text="Thumbs Up",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        up_txt=Entry(F4,width=10,textvariable=self.thumbup,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        limca_lbl=Label(F4,text="Limca",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        limca_txt=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)

        sprite_lbl=Label(F4,text="Sprite",font=("times new roman",16,"bold"),bg=bg_color,fg="white").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        sprite_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)


        #====Bill Area===
        F5=LabelFrame(self.root,bd=9,relief=GROOVE)
        F5.place(x=920,y=150,width=350,height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)


        #========Button Frame=======
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=530,relwidth=1,height=120)
        m1_lbl=Label(F6,text="Total cosmetic price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=0,padx=15,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.cosmetic_price,font="arial 8 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=1)

        m2_lbl=Label(F6,text="Total Grocery price",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=0,padx=15,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,font="arial 8 bold",textvariable=self.grocery_price,bd=7,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=1)

        m3_lbl=Label(F6,text="Total Cold Drinks price",bg=bg_color,fg="white",font=("times new roman",11,"bold")).grid(row=2,column=0,padx=15,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,font="arial 8 bold",textvariable=self.cold_price,bd=7,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)



        c1_lbl=Label(F6,text="cosmetic Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=0,column=2,padx=15,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.cosmetic_tax,font="arial 8 bold",bd=7,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=1)

        c2_lbl=Label(F6,text=" Grocery Tax",bg=bg_color,fg="white",font=("times new roman",12,"bold")).grid(row=1,column=2,padx=15,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.grocery_tax,font="arial 8 bold",bd=7,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)

        c3_lbl=Label(F6,text=" Cold Drinks Tax",bg=bg_color,fg="white",font=("times new roman",10,"bold")).grid(row=2,column=2,padx=15,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.cold_drink_tax,font="arial 8 bold",bd=7,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=1)
        
        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=725,width=550,height=80)

        total_btn=Button(btn_F,command=self.total,text="Total",bg="cadetblue",fg="white",bd=5,pady=11,width=14,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_F,text="Genrate Bill",command=self.bill_area,bg="cadetblue",fg="white",bd=5,pady=11,width=14,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_F,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",bd=5,pady=11,width=14,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_F,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",bd=5,pady=11,width=12,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()


    def total(self):
        self.c_bs_p=self.soap.get()*20
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_hg_p=self.gell.get()*140
        self.c_s_p=self.spray.get()*130
        self.c_bl_p=self.loshan.get()*180
        self.total_cosmetic_price=float(
                                    self.c_bs_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_hg_p+
                                    self.c_s_p+
                                    self.c_bl_p
                                    )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmetic_price))   
        self.c_tax=round((self.total_cosmetic_price*0.05),2)                   
        self.cosmetic_tax.set("Rs."+str(self.c_tax))
        
        self.g_r_p=self.rice.get()*40
        self.g_f_p=self.food_oil.get()*120
        self.g_d_p=self.daal.get()*60
        self.g_w_p=self.wheat.get()*180
        self.g_s_p=self.sugar.get()*140
        self.g_t_p=self.tea.get()*180
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_f_p+
                                    self.g_d_p+
                                    self.g_w_p+
                                    self.g_s_p+
                                    self.g_t_p
                                    )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))  
        self.g_tax=round((self.total_grocery_price*0.1),2)                      
        self.grocery_tax.set("Rs."+str(self.g_tax))
        
        self.d_m_p=self.maza.get()*60
        self.d_c_p=self.cock.get()*60
        self.d_f_p=self.frooti.get()*50
        self.d_t_p=self.thumbup.get()*45
        self.d_l_p=self.limca.get()*40
        self.d_s_p=self.sprite.get()*60
        self.total_cold_price=float(
                                    self.d_m_p+
                                    self.d_c_p+
                                    self.d_f_p+
                                    self.d_t_p+
                                    self.d_l_p+
                                    self.d_s_p
                                    )
        self.cold_price.set("Rs. "+str(self.total_cold_price)) 
        self.d_tax=round((self.total_cold_price*0.05),2)                         
        self.cold_drink_tax.set("Rs. "+str(self.d_tax))
        
        self.total_bill=float(  self.total_cosmetic_price+
                                self.total_grocery_price+
                                self.total_cold_price+
                                self.c_tax+
                                self.g_tax+
                                self.d_tax
                              )   

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\twelcome webcode Reatil\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.bill_no.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END,f"\n Phone Number : {self.c_phone.get()}")
        self.txtarea.insert(END,f"\n======================================")
        self.txtarea.insert(END,f"\n Products\t\tqty\t\tPrice")
        self.txtarea.insert(END,f"\n======================================")
    def bill_area(self): 
        if self.c_name.get()=="" or self.c_phone.get()=="":
            messagebox.showerror("Error","Customer details are must")
        elif self.cosmetic_price.get()=="Rs. 0.0" and self.grocery_price.get()=="Rs. 0.0" and self.cold_price.get()=="":
            messagebox.showerror("Error","No Product Puchased")
        else:
             self.welcome_bill()        
       
        #=====cosmetics====
             if self.soap.get()!=0:
               self.txtarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_bs_p}")
             if self.face_cream.get()!=0:
               self.txtarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
             if self.face_wash.get()!=0:
               self.txtarea.insert(END,f"\n Face Wash\t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
             if self.gell.get()!=0:
                self.txtarea.insert(END,f"\n Hair Gell\t\t{self.gell.get()}\t\t{self.c_hg_p}")
             if self.spray.get()!=0:
                   self.txtarea.insert(END,f"\n spray\t\t{self.spray.get()}\t\t{self.c_s_p}")
             if self.loshan.get()!=0:
               self.txtarea.insert(END,f"\n Body Loshan\t\t{self.loshan.get()}\t\t{self.c_bl_p}") 

        #=====Grocery====
             if self.rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
             if self.food_oil.get()!=0:
              self.txtarea.insert(END,f"\n Food OIl\t\t{self.food_oil.get()}\t\t{self.g_f_p}")
             if self.daal.get()!=0:
               self.txtarea.insert(END,f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
             if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
             if self.sugar.get()!=0:
               self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.g_s_p}")
             if self.tea.get()!=0:
               self.txtarea.insert(END,f"\n Tea\t\t{self.tea.get()}\t\t{self.g_t_p}")    

        #=====Cold Drinks====
             if self.maza.get()!=0:
               self.txtarea.insert(END,f"\n Maza\t\t{self.maza.get()}\t\t{self.d_m_p}")
             if self.cock.get()!=0:
               self.txtarea.insert(END,f"\n Coca COla\t\t{self.cock.get()}\t\t{self.d_c_p}")
             if self.frooti.get()!=0:
               self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.d_f_p}")
             if self.thumbup.get()!=0:
               self.txtarea.insert(END,f"\n Thums up\t\t{self.thumbup.get()}\t\t{self.d_t_p}")
             if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.d_l_p}")
             if self.sprite.get()!=0:
               self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.d_s_p}") 

             self.txtarea.insert(END,f"\n-------------------------------------")
             if self.cosmetic_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nCosmetic Tax \t\t\t{self.cosmetic_tax.get()}")
             if self.grocery_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nGrocery Tax \t\t\t{self.grocery_tax.get()}")
             if self.cold_drink_tax.get()!="Rs. 0.0":
               self.txtarea.insert(END,f"\nCold Drinks Tax \t\t\t{self.cold_drink_tax.get()}")

             self.txtarea.insert(END,f"\n Total Bill : \t\t\tRs. {str(self.total_bill)}")               
             self.txtarea.insert(END,f"\n-------------------------------------") 
             self.save_bill()


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get('1.0',END)
            f1=open("C:\\Users\\susmi\\Desktop\\dev/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} save successfully")
        else:
            return 
            
    def find_bill(self):
      present="no"
      for i in os.listdir("C:\\Users\\susmi\\Desktop\\dev/"):
        if i.split('.')[0]==self.search_bill.get():
             f1=open(f"C:\\Users\\susmi\\Desktop\\dev/{i}","r")
             self.txtarea.delete(END)
             for d in f1:
               self.txtarea.insert(END,d)
             f1.close()
             present="yes"
      if present=="no":
        messagebox.showerror("Error","Invalid bill no.")


    def clear_data(self):
      op=messagebox.askyesno("Clear","Do you really to Clear?")
      if op>0:

        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        #=====grocery===
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        #====Cold Drinks====
        self.maza.set(0)
        self.cock.set(0)
        self.frooti.set(0)
        self.thumbup.set(0)
        self.limca.set(0)
        self.sprite.set(0)

        #===Total Product Price and tax Variable===
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.cold_price.set("")

        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.cold_drink_tax.set("")

        #====Customer====
        self.c_name.set("")
        self.c_phone.set("")

        
        self.bill_no.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()

    def Exit_app(self):
      op=messagebox.askyesno("Exit","Do you really to exit?")
      if op>0:
        self.root.destroy()


root=Tk()
obj = Bill_App(root)
root.mainloop()
