#Hospital management system

from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
root=Tk()
root.title('Welcome to Hospital')
root.configure(background='grey')

#root.geometry("1600x600")

rwidth=root.winfo_screenwidth()
rheight=root.winfo_screenheight()
root.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

#f0
#f0
#_________________________________Button def_____________________________
def admin():
        #print('admin')
        root.withdraw()
        root1.deiconify()
        

def doctor():
        print('')

def reception():
        print('')
#_________________________________f1_____________________________________
f1=Frame(root,height=800,width=1500,bd=4,relief='solid',padx=50,pady=20,bg='skyblue')
f1.grid(row=1,column=1,padx=10,pady=10)

#__________________________________f2____________________________________
myfont=Font(family='Aerial',size=20,slant='italic')

f2=Frame(f1,height=40,width=1400,bd=4,relief='solid',padx=50,pady=20)
f2.pack()
#grid(row=0,column=0,padx=10,pady=10)

l2=Label(f2,text='HOSPITAL MANAGEMENT SYSTEM',font=myfont,fg='Black',bg='white')
l2.grid(row=0,column=15,padx=150,pady=10)
#------------------------------------------------------------------------

l1=Label(f1,text='Login As',font=myfont,fg='Black',bg='white',anchor='w')
l1.pack(side=LEFT,padx=5,pady=10)

l3=Label(f1,text='Welcome to Hospital  ',bd=3,relief='solid',font=myfont,fg='Black',anchor='n')
l3.pack(padx=10,pady=50)

b1=Button(f1,text='Admin',height=5,width=10,command=admin,font=myfont,fg='Black')
b1.pack(side=LEFT,padx=100,pady=150)

b2=Button(f1,text='Doctor',height=5,width=10,command=doctor,font=myfont,fg='Black')
b2.pack(side=LEFT,padx=100,pady=150)

b3=Button(f1,text='Reception',height=5,width=10,command=reception,font=myfont,fg='Black')
b3.pack(side=LEFT,padx=130,pady=150)

b4=Button(f1,text='Exit',height=1,width=4,command=root.wm_withdraw,font=myfont,fg='Black')
b4.pack(anchor=CENTER,padx=8)

#_____________________________________window1_________________________________________
root1=Tk()
root1.title('Welcome to Hospital')
root1.configure(background='white')

rwidth=root1.winfo_screenwidth()
rheight=root1.winfo_screenheight()
root1.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')

username=StringVar()
password=StringVar()

def login():
        print("username",username.get())
        print("password",password.get())
        if(username.get=='admin'and password.get=='admin'):
                root.withdraw()
                root1.deiconify()
        else:
                messagebox.showinfo('Welcome admin','Login Successfully')
                root.withdraw()
                root1.withdraw()
                root2.deiconify()    


f3=Frame(root1,height=600,width=600,bd=4,padx=100,pady=20,relief='solid',bg='sky blue')
f3.grid(row=4,column=10,padx=480,pady=200)

l4=Label(f3,text='Username',font=myfont,fg='Black')
l4.grid(row=0,column=0,padx=10,pady=20)

e4=Entry(f3,textvariable=username,font=myfont,fg='Black')
e4.grid(row=0,column=2,padx=10,pady=20)

l5=Label(f3,text='Password',font=myfont,fg='Black')
l5.grid(row=2,column=0,padx=10,pady=20)

e5=Entry(f3,textvariable=password,show='*',font=myfont,fg='Black')
e5.grid(row=2,column=2,padx=10,pady=20)

b5=Button(f3,text='Login',command=login,font=myfont,fg='Black')
b5.grid(row=4,column=2,padx=10,pady=20)

#______________________________________window2________________________________________

root2=Tk()
root2.title('Welcome to Hospital')
root2.configure(background='grey')

rwidth=root2.winfo_screenwidth()
rheight=root2.winfo_screenheight()
root2.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=16,slant='italic')



def patient_info():
        print(' ')

def doctor_info():
        print(' ')

f4=Frame(root2,height=800,width=1500,bd=4,padx=50,pady=20,relief='solid',bg='sky blue')
f4.grid(row=0,column=1,padx=10,pady=80)

f5=Frame(f4,height=40,width=1400,bd=4,relief='solid',padx=50,pady=10)
f5.pack()

l6=Label(f5,text='ADMIN PORTAL',font=myfont,fg='Black')
l6.grid(row=1,column=12,padx=6,pady=20)

l7=Label(f4,text='Welcome to Admin Portal',font=myfont,fg='Black',bg='white',anchor='w')
l7.pack(side=LEFT,padx=10,pady=10)


b6=Button(f4,text='Patient info',height=5,width=10,command=patient_info,font=myfont,fg='Black')
b6.pack(side=LEFT,padx=100,pady=150)

b7=Button(f4,text='Doctor info',height=5,width=10,command=doctor_info,font=myfont,fg='Black')
b7.pack(side=LEFT,padx=100,pady=150)

b8=Button(f4,text='Reception',height=5,width=10,command=reception,font=myfont,fg='Black')
b8.pack(side=LEFT,padx=130,pady=150)

b9=Button(f4,text='Exit',height=1,width=4,command=root2.wm_withdraw,font=myfont,fg='Black')
b9.pack(anchor=CENTER,padx=20)


username=StringVar()
password=StringVar()

def login():
        print("username",username.get())
        print("password",password.get())
        if(username.get=='admin'and password.get=='admin'):
                root.withdraw()
                root1.deiconify()
        else:
                messagebox.showinfo('Welcome admin','Login Successfully')
                root.withdraw()
                root1.withdraw()
                root2.withdraw()
                root3.deiconify()

#-------------------------------------------DEF BUTTON ROOT3----------------------------------------------

def b10():
        root3.withdraw()
        root4.deiconify()

#---------------------------------------ROOT3-----------------------------------------------------------------------------------

root3=Tk()
root3.title('Welcome to Hospital')
root3.configure(background='burlywood4')

rwidth=root3.winfo_screenwidth()
rheight=root3.winfo_screenheight()
root3.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=20,slant='italic')

f6=Frame (root3,height=40,width=1500,bd=5,relief='solid',padx=50,pady=100,bg='white')
f6.pack(pady=6)

l8=Label(f6,text='RECEPTIONIST MANAGEMENT',font=myfont,fg='Black',bd=4,bg='skyblue')
l8.grid(padx=7,pady=15,row=0,column=2)

l9=Label(f6,text='''Welcome to
        Receptionist
        Management''',height=10,width=15,font=myfont,fg='Black',bg='light green',anchor='w')
l9.grid(padx=10,pady=6,row=2,column=0)

b10=Button(f6,text='Add New',command=b10,height=5,width=10,font=myfont,fg='Black')
b10.grid(row=2,column=2,padx=5,pady=5)

b11=Button(f6,text='Update',height=5,width=10,font=myfont,fg='Black')
b11.grid(row=2,column=3,padx=5,pady=5)

b12=Button(f6,text='Delete',height=5,width=10,font=myfont,fg='Black')
b12.grid(row=2,column=4,padx=5,pady=5)

b13=Button(f6,text='Search',height=5,width=10,font=myfont,fg='Black')
b13.grid(row=2,column=5,padx=5,pady=5)

b14=Button(f6,text='View',height=5,width=10,font=myfont,fg='Black')
b14.grid(row=2,column=6,padx=5,pady=5)

#-------------------------------------------------------------------------ROOT 4------------------------------------------------------------------------------------------------------------

root4=Tk()
root4.title('Welcome to Hospital')
root.configure(background='burlywood4')

rwidth=root4.winfo_screenwidth()
rheight=root4.winfo_screenheight()
root4.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=18,slant='italic')

f7=Frame(root4,height=40,width=1500,bd=4,relief='solid',padx=50,pady=10)
f7.pack(pady=5)

l10=Label(f7,text='Add Receptionist',height=5,width=60,font=myfont,fg='Black',bg='sky blue')
l10.grid(padx=5,pady=10,row=0,column=1,columnspan=4)



l11=Label(f7,text='Date',font=myfont,fg='white',bg='skyblue')
l11.grid(padx=5,pady=5,row=2,column=0)

e6=Entry(f7,font=myfont,fg='burlywood4')
e6.grid(row=2,column=1)




l12=Label(f7,text='Id',font=myfont,fg='white',bg='skyblue')
l12.grid(padx=5,pady=5,row=3,column=0)

e7=Entry(f7,font=myfont,fg='burlywood4')
e7.grid(row=3,column=1)




l13=Label(f7,text='Name',font=myfont,fg='white',bg='skyblue')
l13.grid(padx=5,pady=5,row=4,column=0)

e8=Entry(f7,font=myfont,fg='black')
e8.grid(row=4,column=1)




l14=Label(f7,text='Age',font=myfont,fg='white',bg='skyblue')
l14.grid(padx=5,pady=5,row=5,column=0)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=5,column=1)





l15=Label(f7,text='Gender',font=myfont,fg='white',bg='skyblue')
l15.grid(padx=5,pady=5,row=6,column=0)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=6,column=1)





l16=Label(f7,text='Blood Group',font=myfont,fg='white',bg='skyblue')
l16.grid(padx=5,pady=5,row=2,column=3)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=2,column=4)



l17=Label(f7,text='Phoneno',font=myfont,fg='white',bg='skyblue')
l17.grid(padx=5,pady=5,row=3,column=3)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=3,column=4)




l18=Label(f7,text='Email',font=myfont,fg='white',bg='skyblue')
l18.grid(padx=5,pady=5,row=4,column=3)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=4,column=4)




l19=Label(f7,text='Address',font=myfont,fg='white',bg='skyblue')                                                                              
l19.grid(padx=5,pady=5,row=5,column=3)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=5,column=4)




l20=Label(f7,text='Martial Status',font=myfont,fg='white',bg='skyblue')
l20.grid(padx=5,pady=5,row=6,column=3)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=6,column=4)




l21=Label(f7,text='Username',font=myfont,fg='white',bg='skyblue')
l21.grid(padx=5,pady=5,row=2,column=5)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=2,column=6)





l22=Label(f7,text='Password',font=myfont,fg='white',bg='skyblue')
l22.grid(padx=5,pady=5,row=3,column=5)

e8=Entry(f7,font=myfont,fg='burlywood4')
e8.grid(row=3,column=6)



b15=Button(f7,text='Clear',height=3,width=10,font=myfont,fg='Black')
b15.grid(row=7,column=3,padx=5,pady=5)



b16=Button(f7,text='Add',height=3,width=10,font=myfont,fg='Black')
b16.grid(row=7,column=5,padx=5,pady=5)

#---------------------------------------------------------------------------------ROOT 5-----------------------------------------------------------------------------------------------------



root5=Tk()
root5.title('Welcome to Hospital')
root5.configure(background='burlywood4')

rwidth=root5.winfo_screenwidth()
rheight=root5.winfo_screenheight()
root5.geometry(('%dx%d')%(rwidth,rheight))

myfont=Font(family='Aerial',size=20,slant='italic')

f8=Frame (root5,height=40,width=1500,bd=5,relief='solid',padx=50,pady=100,bg='white')
f8.pack(pady=6)

l23=Label(f8,text='DOCTOR PANEL',font=myfont,fg='Black',bd=4,bg='skyblue')
l23.grid(padx=7,pady=15,row=0,column=2)

l24=Label(f8,text='''Welcome to
        Doctor
         Panel''',height=10,width=15,font=myfont,fg='Black',bg='light green',anchor='w')
l24.grid(padx=10,pady=6,row=2,column=0)

b17=Button(f8,text='Add New',command=b10,height=5,width=10,font=myfont,fg='Black')
b17.grid(row=2,column=2,padx=5,pady=5)

b18=Button(f8,text='Update',height=5,width=10,font=myfont,fg='Black')
b18.grid(row=2,column=3,padx=5,pady=5)

b19=Button(f8,text='Delete',height=5,width=10,font=myfont,fg='Black')
b19.grid(row=2,column=4,padx=5,pady=5)

b20=Button(f8,text='Search',height=5,width=10,font=myfont,fg='Black')
b20.grid(row=2,column=5,padx=5,pady=5)

b21=Button(f8,text='View',height=5,width=10,font=myfont,fg='Black')
b21.grid(row=2,column=6,padx=5,pady=5)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
