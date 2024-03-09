from tkinter import *
# main.py
from FinanceTracker import User

user = User()


root =Tk()
root.title("Expense management system")
frameuser = LabelFrame(root,text="User Interact", padx=5, pady=10)
frameuser.grid(row=0,column=1,padx=10, pady=10)
framebuttons = LabelFrame(root, text="Buttons", padx=15 , pady=10)
framebuttons.grid(row=0,column=0,padx=10 , pady=10)
displayframe = LabelFrame(root,text="Display Management System", padx=5, pady=5)
displayframe.grid(row=0,column=2,padx=10, pady=10)
Label(frameuser,text="This is for user inputs").pack()

def deletetransaction():
    delete_description = delete_desc_input.get()
    response = user.delete_transaction(delete_description)
    summary_text.delete(1.0, END)
    summary_text.insert(INSERT,response)
# for delete
delete_desc_input = Entry(frameuser)
delete_description_label = Label(frameuser, text="Enter the description to remove: ")
buttonsubmit_delete = Button(frameuser,text="Submit",command=deletetransaction)

def loadtransactiondelete():
    cleareverything()


    delete_description_label.pack()
    delete_desc_input.pack()
    buttonsubmit_delete.pack()

def addtransaction():
    amount = float(textbox_amount.get())
    description = textbox_description.get()
    type = textbox_type.get()
    user.add_transaction(amount, description, type)
    user.view_transactions()

# for addition
textbox_amount = Entry(frameuser)
textbox_description = Entry(frameuser)
textbox_type = Entry(frameuser)
amount = Label(frameuser, text="Amount:")
description = Label(frameuser, text="Description:")
typetranscation = Label(frameuser, text="Type (Income/Expense):")
buttonsubmit = Button(frameuser,text="Submit",command=addtransaction)



def loadtransactionaddition():
    cleareverything()

    amount.pack()
    textbox_amount.pack()

    description.pack()
    textbox_description.pack()

    typetranscation.pack()
    textbox_type.pack()

    buttonsubmit.pack()

# for update
updatedes = Entry(frameuser)
updatewith = Entry(frameuser)
value_text = Entry(frameuser)
update_label = Label(frameuser, text="Enter transaction name: ")
updatewith_label = Label(frameuser, text="Enter \n type \n amount  \n description \n")
value_label = Label(frameuser, text="Enter the value to update")
def addupdate():
    descriptionupdate = updatedes.get()
    updatewhat = updatewith.get()
    val = value_text.get()
    user.update_transaction(descriptionupdate,updatewhat,val)
    user.view_transactions()

buttonsubmitupdate = Button(frameuser,text="Submit",command=addupdate)

def cleareverything():
    updatedes.pack_forget()
    updatewith.pack_forget()
    update_label.pack_forget()
    updatewith_label.pack_forget()
    buttonsubmitupdate.pack_forget()
    value_text.pack_forget()
    value_label.pack_forget()
    textbox_amount.pack_forget()
    textbox_description.pack_forget()
    textbox_type.pack_forget()
    buttonsubmit.pack_forget()
    amount.pack_forget()
    description.pack_forget()
    typetranscation.pack_forget()
    delete_desc_input.pack_forget()
    delete_description_label.pack_forget()
    buttonsubmit_delete.pack_forget()

def loadtransactionupdate():

    cleareverything()

    update_label.pack()
    updatedes.pack()

    updatewith_label.pack()
    updatewith.pack()

    value_label.pack()
    value_text.pack()


    buttonsubmitupdate.pack()
def showsummary():
    text = user.display_summary()
    summary_text.delete("1.0", "end")
    summary_text.insert(INSERT, text)

def savetoJSON():
    user.save_transactions()
    summary_text.delete("1.0", "end")
    summary_text.insert(INSERT,"Transactions saved")

def load():
    transactions_text.delete("1.0", "end")
    user.load_transactions()
    for transaction in user.transactions:
        transactions_text.insert(INSERT,transaction)
        transactions_text.insert(INSERT,"\n")

def viewtransactions():
    transactions_text.delete("1.0", "end")
    for transaction in user.transactions:
        transactions_text.insert(INSERT,transaction)
        transactions_text.insert(INSERT, "\n")



button0 = Button(framebuttons,text="Load Transactions",padx=15 , pady=5,width=20,command=load)
button0.pack(pady=10)
button = Button(framebuttons,text="Add a Transaction",padx=15 , pady=5,width=20,command=loadtransactionaddition)
button.pack(pady=10)
button2 = Button(framebuttons,text="View Transactions",padx=15 , pady=5,width=20,command=viewtransactions)
button2.pack(pady=10)
buttonupdate = Button(framebuttons,text="Update a Transaction",padx=15 , pady=5,width=20,command=loadtransactionupdate)
buttonupdate.pack(pady=10)
button3 = Button(framebuttons,text="Delete a Transaction",padx=15 , pady=5,width=20 , command=loadtransactiondelete)
button3.pack(pady=10)
button4 = Button(framebuttons,text="Display Summary",padx=15 , pady=5,width=20 , command=showsummary)
button4.pack(pady=10)
button5 = Button(framebuttons,text="Save Transactions",padx=15 , pady=5,width=20, command=savetoJSON)
button5.pack(pady=10)
button6 = Button(framebuttons,text="Exit program",padx=15 , pady=5,width=20 , command=root.quit)
button6.pack(pady=10)

transactions_text = Text(displayframe, height=10, width=50)
welcome_text = user.display_menu()
transactions_text.insert(INSERT,welcome_text)
transactions_text.pack()

summary_text = Text(displayframe, height=5, width=50)
summary_text.pack()

root.mainloop()