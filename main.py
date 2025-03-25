from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import os
import sys

def main():
    win = Tk()
    ob = LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1526x790+0+0")
        self.win.title("Restaurant Billing System")

        self.title_label = Label(self.win,text="Restaurant Management System",font=("Arial",35,"bold"),bg="powderblue",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame = Frame(self.win,bg="powderblue",bd=6,relief=GROOVE)
        self.main_frame.place(x=250,y=150,width=800,height=450)

        self.login_lbl = Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="Powderblue",font=("sans-serif",25,"bold"))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame = LabelFrame(self.main_frame,text="Enter Details",bd=6,relief=GROOVE,bg="powderblue",font=("sans-serif",18))
        self.entry_frame.pack(fill=BOTH,expand=1)

        self.entus_lbl = Label(self.entry_frame,text="Enter System ID",bg="powderblue",font=("sans-serif",15))
        self.entus_lbl.grid(row=0,column=0)

        #==========================Variables==================================#

        self.username = StringVar()
        self.password = StringVar()

        #=====================================================================#

        self.entus_ent = Entry(self.entry_frame,font=("sans-serif",15),bd=6,textvariable=self.username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        self.entpass_lbl = Label(self.entry_frame,text="Enter Password",bg="powderblue",font=("sans-serif",15))
        self.entpass_lbl.grid(row=1,column=0)

        self.entpass_ent = Entry(self.entry_frame, font=("sans-serif",15),bd=6,textvariable=self.password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        #===========================Functions==================================#

        def check_login():
            #This function will check user login credentials
            if self.username.get() == "1234" and self.password.get() == "1234":
                self.billing_btn.config(state="normal")
            else:
                pass
        
        def reset():
            self.username.set("")
            self.password.set("")

        def Billing_sect():
            self.newWindow = Toplevel(self.win)
            self.app = Window2(self.newWindow)

        #======================================================================#

        #===========================Buttons====================================#

        self.button_frame = LabelFrame(self.entry_frame,text="Options",font=("Arial",15),bg="powderblue",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn = Button(self.button_frame,text="Login",font=("Arial",15),width=15,bd=5,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn = Button(self.button_frame,text="Billing",font=("Arial",15),width=15,bd=5,command=Billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn = Button(self.button_frame,text="Reset",font=("Arial",15),width=15,bd=5,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)

        #==================================================================#

class Window2:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1526x790+0+0")
        self.win.title("Bill Generator")

        self.title_label = Label(self.win,text="Bill Generator",font=("Arial",35,"bold"),bg="powderblue",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        #==========================VARIABLES===============================#

        bill_no = random.randint(100,999)
        bill_no_tk = IntVar()
        bill_no_tk.set(bill_no)

        calc_var = StringVar()

        cust_nm = StringVar()
        cust_cot = StringVar()
        date_pr = StringVar()
        item_pur = StringVar()
        item_qty = StringVar()
        cone = StringVar()

        date_pr.set(datetime.now())

        total_list = []
        self.grd_total = 0

        #==================================================================#

        #============================ENTRY=================================#

        self.entry_frame = LabelFrame(self.win,text="Enter Details",bg="powderblue",font=("Arial",20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl = Label(self.entry_frame,text="Bill Number ",font=("Arial",15),bg="powderblue")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent = Entry(self.entry_frame,bd=5,font=("Arial",15),textvariable=bill_no_tk)
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.cust_nm_lbl = Label(self.entry_frame,text="Customer Name ",font=("Arial",15),bg="powderblue")
        self.cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.cust_nm_ent = Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=("Arial",15))
        self.cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lbl = Label(self.entry_frame,text="Customer Contact ",font=("Arial",15),bg="powderblue")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent = Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=("Arial",15))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl = Label(self.entry_frame,text="Date ",font=("Arial",15),bg="powderblue")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent = Entry(self.entry_frame,bd=5,textvariable=date_pr,font=("Arial",15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)

        self.item_pur_lbl = Label(self.entry_frame,text="Item Purchased ",font=("Arial",15),bg="powderblue")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent = Entry(self.entry_frame,bd=5,textvariable=item_pur,font=("Arial",15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qty_lbl = Label(self.entry_frame,text="Item Quantity ",font=("Arial",15),bg="powderblue")
        self.item_qty_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qty_ent = Entry(self.entry_frame,bd=5,textvariable=item_qty,font=("Arial",15))
        self.item_qty_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl = Label(self.entry_frame,text="Cost of One Item ",font=("Arial",15),bg="powderblue")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent = Entry(self.entry_frame,bd=5,textvariable=cone,font=("Arial",15))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        #==================Functions====================================#

        def default_bill():
            self.bill_txt.insert(END,"\t\t\t\t\t\tABC's Kitchen")
            self.bill_txt.insert(END,"\n\t\t\t\t     7 Street, Near Alpha-I, Greater Noida")
            self.bill_txt.insert(END,"\n\t\t\t\t\t   Contact - +91-9999XXXX99")
            self.bill_txt.insert(END,"\n===========================================================================================================")
            self.bill_txt.insert(END,f"\nBill Number : {bill_no_tk.get()}")

        def genbill():
            if cust_nm.get() == "" or (cust_cot.get() == "" or len(cust_cot.get()) != 10):
                messagebox.showerror("Error!","Please enter all the fields correctly!")
            else:
                self.bill_txt.insert(END,f"\nCustomer Name : {cust_nm.get()}")
                self.bill_txt.insert(END,f"\nCustomer Contact : {cust_cot.get()}")    
                self.bill_txt.insert(END,f"\nDate : {date_pr.get()}")
                self.bill_txt.insert(END,"\n===========================================================================================================")
                self.bill_txt.insert(END,"\nProduct Name\t\t\t\t\t\t\t\t    Quantity\t\t  Per Item Cost\t\t    Total")
                self.bill_txt.insert(END,"\n===========================================================================================================")
                self.add_btn.config(state="normal")
                self.total_btn.config(state="normal")
            
        def clear():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")
            cone.set("")

        def reset():
            total_list.clear()
            self.grd_total = 0
            self.bill_txt.delete("1.0",END)
            clear()
            default_bill()
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")

        def add():
            if item_pur.get() == "" or item_qty.get() == "":
                messagebox.showerror("Error!","Please enter all the fields correctly!")
            else:
                qty = int(item_qty.get())
                cones = int(cone.get())
                total = qty * cones
                total_list.append(total)
                self.bill_txt.insert(END,f"{item_pur.get()}\t\t\t\t\t\t\t\t        {item_qty.get()}\t\t       ₹{cone.get()}\t\t      ₹{total}\n")

        def total():
            for item in total_list:
                self.grd_total = self.grd_total + item
            self.bill_txt.insert(END,"\n===========================================================================================================")
            self.bill_txt.insert(END,f"\t\t\t\t\t\t\t\t\t\t\t\tGrand Total : {self.grd_total}")
            self.bill_txt.insert(END,"\n===========================================================================================================")
            self.save_btn.config(state="normal") 

        def save():
            user_choice = messagebox.askyesno("Confirm?",f"Do you want to save the bill {bill_no_tk.get()}",parent=self.win)
            if user_choice > 0:
                self.bill_content = self.bill_txt.get("1.0",END)
                try:
                    dir_path = os.path.dirname(__file__)
                    with open(os.path.join(dir_path, "Bills", f"{bill_no_tk.get()}.txt"), "w") as f:
                        f.write(self.bill_content)
                    messagebox.showinfo("Success!",f"Bill {bill_no_tk.get()} has been saved successfully!",parent=self.win)
                except Exception as e:
                    messagebox.showerror("Error!",f"Error due to {e}")
            else:
                return 


        #===============================================================#

        #==================Buttons======================================#

        self.button_frame = LabelFrame(self.entry_frame,bd=5,text="Options",bg="Powderblue",font=("Arial",15))
        self.button_frame.place(x=20,y=280,width=394,height=300)

        self.add_btn = Button(self.button_frame,bd=3,text="Add",font=("Arial",12),width=12,height=3,command=add)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn = Button(self.button_frame,bd=3,text="Generate",font=("Arial",12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn = Button(self.button_frame,bd=3,text="Clear",font=("Arial",12),width=12,height=3,command=clear)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn = Button(self.button_frame,bd=3,text="Total",font=("Arial",12),width=12,height=3,command=total)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn = Button(self.button_frame,bd=3,text="Reset",font=("Arial",12),width=12,height=3,command=reset)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn = Button(self.button_frame,bd=3,text="Save",font=("Arial",12),width=12,height=3,command=save)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)

        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

        #===============================================================#

        #==========================CALCULATOR===========================#

        self.calc_frame = Frame(self.win,bd=3,bg="Powderblue",relief=GROOVE)
        self.calc_frame.place(x=570,y=110,width=895,height=280)

        self.num_ent = Entry(self.calc_frame,bd=15,background="Powderblue",textvariable=None,font=("Arial",12),width=95,justify=RIGHT)
        self.num_ent.grid(row=0,column=0,columnspan=11)

        def press_btn(event):
            text = event.widget.cget("text")
            if text == "=":
                try:
                    value = eval(self.num_ent.get())
                    self.num_ent.delete(0, END)
                    self.num_ent.insert(END, str(value))
                except:
                    self.num_ent.delete(0, END)
                    self.num_ent.insert(END, "Error")
            elif text == "C":
                self.num_ent.delete(0, END)
            else:
                self.num_ent.insert(END, text)

        self.buttons = [
            "7", "8", "9", "+",
            "4", "5", "6", "-",
            "1", "2", "3", "*",
            ".", "0", "/", "="
        ]

        row_val = 1
        col_val = 0

        for button in self.buttons:
            btn = Button(self.calc_frame,bg="Powderblue",text=button,bd=8,width=18,height=1,font=("Arial",15))
            btn.grid(row=row_val, column=col_val, padx=1, pady=2)
            btn.bind("<Button-1>", press_btn)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        #===============================================================#

        #===========================Bill Frame==========================#

        self.bill_frame = LabelFrame(self.win,text="Billing Area",font=("Arial",18),bg="Powderblue",bd=8,relief=GROOVE)
        self.bill_frame.place(x=570,y=400,width=895,height=342)

        self.y_scroll = Scrollbar(self.bill_frame,orient=VERTICAL)
        self.bill_txt = Text(self.bill_frame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_txt.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)
        self.bill_txt.pack(fill=BOTH,expand=TRUE)

        default_bill()

        #==============================================================#

if __name__ == "__main__":
    main()



import random
from datetime import datetime
import os

# ========================== Classes and Functions ==============================

class BillingSystem:
    def __init__(self):
        self.bill_no = random.randint(100, 999)
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total_list = []
        self.grd_total = 0

    def login(self):
        print("Welcome to the Restaurant Billing System")
        system_id = input("Enter System ID: ")
        password = input("Enter Password: ")
        if system_id == "1234" and password == "1234":
            print("Login successful!")
            self.billing_menu()
        else:
            print("Login failed. Incorrect System ID or Password.")
            self.login()

    def billing_menu(self):
        while True:
            print("\nBilling Menu:")
            print("1. Generate Bill")
            print("2. Add Item to Bill")
            print("3. Display Total")
            print("4. Reset Bill")
            print("5. Save Bill")
            print("6. Exit")
            choice = input("Enter choice: ")
            if choice == '1':
                self.generate_bill()
            elif choice == '2':
                self.add_item()
            elif choice == '3':
                self.display_total()
            elif choice == '4':
                self.reset_bill()
            elif choice == '5':
                self.save_bill()
            elif choice == '6':
                print("Exiting the billing system.")
                break
            else:
                print("Invalid choice. Try again.")

    def generate_bill(self):
        cust_name = input("Enter Customer Name: ")
        cust_contact = input("Enter Customer Contact: ")
        
        if len(cust_contact) != 10 or not cust_contact.isdigit():
            print("Invalid contact number. It should be a 10-digit number.")
            return
        
        self.bill_content = f"""
        ===============================================
        ABC's Kitchen
        Address: 7 Street, Near Alpha-I, Greater Noida
        Contact: +91-9999XXXX99
        ===============================================
        Bill Number: {self.bill_no}
        Customer Name: {cust_name}
        Customer Contact: {cust_contact}
        Date: {self.date}
        ===============================================
        Item Name\t\tQty\t\tPer Item Cost\t\tTotal
        -----------------------------------------------
        """
        print("\nBill generated successfully!\n")

    def add_item(self):
        item_name = input("Enter Item Name: ")
        item_qty = input("Enter Quantity: ")
        item_cost = input("Enter Cost of One Item: ")

        if not item_qty.isdigit() or not item_cost.isdigit():
            print("Invalid input for quantity or cost. Enter numeric values.")
            return

        item_qty = int(item_qty)
        item_cost = int(item_cost)
        total = item_qty * item_cost
        self.total_list.append(total)
        
        self.bill_content += f"{item_name}\t\t{item_qty}\t\t₹{item_cost}\t\t₹{total}\n"
        print("Item added successfully.")

    def display_total(self):
        self.grd_total = sum(self.total_list)
        print(f"\n===============================================\nGrand Total: ₹{self.grd_total}\n===============================================\n")

    def reset_bill(self):
        self.total_list.clear()
        self.grd_total = 0
        print("Bill has been reset.")
        self.generate_bill()

    def save_bill(self):
        save_confirmation = input(f"Do you want to save the bill {self.bill_no}? (yes/no): ").strip().lower()
        if save_confirmation == 'yes':
            if not os.path.exists("Bills"):
                os.makedirs("Bills")
            with open(f"Bills/{self.bill_no}.txt", "w") as f:
                f.write(self.bill_content)
                f.write(f"\n===============================================\nGrand Total: ₹{self.grd_total}\n===============================================")
            print(f"Bill {self.bill_no} has been saved successfully!")
        else:
            print("Bill not saved.")

# ============================== Main Code Execution ============================

if __name__ == "__main__":
    system = BillingSystem()
    system.login()
