from tkinter import*
from tkinter import messagebox
import webbrowser
import os
import sys
import random
import time
ppro=Tk()
ppro.geometry('900x600+250+100')
ppro.title('suppermarket')
ppro.config(background='#FFFFFF')
ppro.iconbitmap('logo.ico')
ppro.resizable(False,False)
###################################
u1='https://web.whatsapp.com/'
u2='https://www.facebook.com/'


######################### 
# market app

def market():
    pro=Tk()
    pro.geometry('900x600+300+10')
    pro.title('supper market')
    pro.resizable('false','false')
    pro.iconbitmap('mmr.ico')
    title=Label(pro, text='الادارة',fg='white',bg='#0b2f3a',font='bold 15')
    title.pack(fill=X)
    #######################frame######################
    f1=Frame(pro,bd=2,width=400,height=200, bg='#1C5856')
    f1.place(x=650,y=29)
    t1=Label(f1,text=' :: بيانات المشتري',font='bold 15',
    background='#1C5856',fg='#B39494')
    t1.place(x=117,y=0)
    ########################################################label
    name=Label(f1,text='اسم المشتري ',fg='#FFFFFF',bg='#1C5856',font='blod 10',
    )
    name.place(x=190, y=30)
    phone=Label(f1,text='رقم المشتري',fg='#FFFFFF',bg='#1C5856',font='blod 10',
    )
    phone.place(x=190, y=60)
    num=Label(f1,text='رقم الفاتوره',fg='#FFFFFF',bg='#1C5856',font='blod 10',
    )
    num.place(x=190, y=90)
    #############################################
    name=StringVar()
    phone=StringVar()
    num=StringVar()
    x=random.randint(1000,9999)
    num.set(str(x))

    def data ():

        name.get()
        phone.get()
        welcome()
    def pl():


        roz1=mt1.get()*2
        mac2=mt2.get()*2
        tona3=mt3.get()*2
        fool4=mt4.get()*2 
        roz5=mt5.get()*2
        mac6=mt6.get()*2
        tona7=mt7.get()*2
        fool8=mt8.get()*2    
        roz9=mt9.get()*2
        mac10=mt10.get()*2
        pl1=float(roz1+
        mac2+
        tona3+
        fool4+
        roz5+
        mac6+
        tona7+
        fool8+
        roz9+
        mac10)
        all.set(str(pl1))
        
    def ppl():

        roz1=mt1.get()
        mac2=mt2.get()
        tona3=mt3.get()
        fool4=mt4.get()
        roz5=mt5.get()
        mac6=mt6.get()
        tona7=mt7.get()
        fool8=mt8.get()    
        roz9=mt9.get()
        mac10=mt10.get()    

        ppl1=float(roz1+mac2+tona3+fool4+roz5+mac6+tona7+fool8+roz9+mac10)
        alll.set(str(ppl1))    

    def clear():
        all.set(0)
        alll.set(0)

        mt1.set(0)
        mt2.set(0) 
        mt3.set(0) 
        mt4.set(0) 
        mt5.set(0) 
        mt6.set(0) 
        mt7.set(0) 
        mt8.set(0) 
        mt9.set(0) 
        mt10.set(0)  
        name.set('')
        num.set('')
        phone.set('')     

    def welcome():
        textarea.insert(END,'\n ==========================')
        textarea.insert(END,'\n ــــــــالفاتورةــــــــ')
        textarea.insert(END,'\n ==========================')
        textarea.insert(END,f"\n {num.get()}   ::  رقــم الفاتورة")
        textarea.insert(END,f"\n الاســــم :: {name.get()}")
        textarea.insert(END,f"\n {phone.get()} ::  رقــم الفـون")

    def save():
        ms=messagebox.askyesno('حغظ','هل تريد الحظ')
        if ms > 0:
            sav=textarea.get('1.0',END)
            f1=open('االفواتير/'+str(num.get()+'.txt')
                    ,'w',encoding='utf-8')
            f1.write(sav)
            f1.close()
            
        else:
            return    

    ###########################entry#################################
    en1=Entry(f1,textvariable=name)
    en1.place(x=5 ,y=30,width=150,height=25)
    en2=Entry(f1,textvariable=phone)
    en2.place(x=5 ,y=60,width=150,height=25)
    en3=Entry(f1,textvariable=num)
    en3.place(x=5 ,y=90,width=150,height=25)
    ##########################button######################################
    bu1=Button(f1,text='ادخال البيانات',font='bold 20',command=data) 
    bu1.place(x=50,y=120,width=170,height=40)       
    ########################frame###################
    lf1=Label(f1,text='{الفواتير}',font='13',bg='#1C5856',fg='#FFFFFF')
    lf1.place(x=110,y=170)
    ##################################################
    f2=Text(pro,bd=2,width=400,height=250,bg='#FFFFFF')
    f2.place(x=650,y=230)
    ################scrolbar #######################
    scrol=Scrollbar(f2,orient=VERTICAL)
    textarea=Text(f2,yscrollcommand=scrol.set)
    scrol.pack(side=LEFT,fill=Y)
    scrol.config(command=textarea.yview)
    textarea.pack(fill=BOTH,expand=1)
    ######################price#######################
    f3=Frame(pro,bd=2,width=650,height=200,bg='#1C5856',)
    f3.place(x=1,y=400)




    ############################################################
    bu2=Button(f3,text='الحسابات',bg='#FFFFFF',
    font='bold 15',command=pl)
    bu2.place(x=490, y=10,width=150,height=50)
    bu3=Button(f3,text='عدد المنتجات',bg='#FFFFFF',
    font='bold 15',command=ppl)
    bu3.place(x=490, y=100,width=150,height=50) 
    bu4=Button(f3,text='طباعه الفاتوره ',bg='#FFFFFF',
    font='bold 15',command=save)
    bu4.place(x=300, y=10,width=150,height=50)
    bu4=Button(f3,text='clear',bg='#FFFFFF',
    font='bold 15',command=clear)
    bu4.place(x=300, y=100,width=150,height=50) 
    #######################################################
    all=StringVar()
    alll=StringVar()
    ##########نوع المتفيرات
    mt1=IntVar()
    mt2=IntVar()
    mt3=IntVar()
    mt4=IntVar()
    mt5=IntVar()
    mt6=IntVar()
    mt7=IntVar()
    mt8=IntVar()
    mt9=IntVar()
    mt10=IntVar()
    #######################################################
    en4=Entry(f3,textvariable=all)
    en4.place(x=10,y=10,width=100,height=50)       

    en5=Entry(f3,textvariable=alll)
    en5.place(x=10,y=100,width=100,height=50) 

    ##################################################################
    lb1=Label(f3,text='الحساب',bg='#1C5856',font='bold 20')
    lb1.place(x=150 ,y=10)
    lb2=Label(f3,text='الكميه',bg='#1C5856',font='bold 20')
    lb2.place(x=150 ,y=100)    
    ##################################################

    ##################frame##########################################################################
    f4=Frame(pro,bd=2,width=300,height=320,bg='#1C5856')
    f4.place(x=10,y=40)
    lf3=Label(f4,text=' المنتجات البقوليات',bg='#848DB4',fg='#2C3D8A',font='bold 20')
    lf3.place(x=50,y=20,width=200,)
    lbb1=Label(f4,text='الرز',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb1.place(x=200 ,y=60)

    lbb2=Label(f4,text='المعكرونه',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb2.place(x=200 ,y=100)

    lbb3=Label(f4,text='الفاصوليا',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb3.place(x=200 ,y=140)

    lbb4=Label(f4,text='اللوبيا',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb4.place(x=200 ,y=180)

    lbb5=Label(f4,text='العدس',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb5.place(x=200 ,y=220) 

    enn1=Entry(f4,textvariable=mt1)
    enn1.place(x=50, y=65, width=100,height=30)

    enn2=Entry(f4,textvariable=mt2)
    enn2.place(x=50, y=105, width=100,height=30)

    enn3=Entry(f4,textvariable=mt3)
    enn3.place(x=50, y=145, width=100,height=30)

    enn4=Entry(f4,textvariable=mt4)
    enn4.place(x=50, y=185, width=100,height=30)

    enn5=Entry(f4,textvariable=mt5)
    enn5.place(x=50, y=225, width=100,height=30)
    #########################math########################

    ##############################################################
    f5=Frame(pro,bd=2,width=300,height=320,bg='#1C5856')
    f5.place(x=330,y=40)
    lf5=Label(f5,text=' الاغذيه المعلبه ',bg='#848DB4',fg='#2C3D8A',font='bold 20')
    lf5.place(x=50,y=20,width=200,)
    lbb1=Label(f5,text='تونه معلبة',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb1.place(x=200 ,y=60)

    lbb2=Label(f5,text='فول معلب',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb2.place(x=200 ,y=100)

    lbb3=Label(f5,text='زيتون معلب',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb3.place(x=200 ,y=140)

    lbb4=Label(f5,text='صلصه معلبه',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb4.place(x=200 ,y=180)

    lbb5=Label(f5,text='جبنه معلبه',bg='#1C5856',font='bold 15',fg='#FFFFFF')
    lbb5.place(x=200 ,y=220) 

    ennn1=Entry(f5,textvariable=mt6)
    ennn1.place(x=50, y=65, width=100,height=30)

    ennn2=Entry(f5,textvariable=mt7)
    ennn2.place(x=50, y=105, width=100,height=30)

    ennn3=Entry(f5,textvariable=mt8)
    ennn3.place(x=50, y=145, width=100,height=30)

    ennn4=Entry(f5,textvariable=mt9)
    ennn4.place(x=50, y=185, width=100,height=30)

    ennn5=Entry(f5,textvariable=mt10)
    ennn5.place(x=50, y=225, width=100,height=30)


    pro.mainloop()



#####################
def open1():
    webbrowser.open_new(u1)

def open2():
    webbrowser.open_new(u2)

def abuot1 ():
    messagebox.showinfo('المطور', 'البشمهندس محمد الشافعي')
def exit():
    ppro.destroy()

def log():
    user=en1.get()
    pas=en2.get()
    if user=='mmr' and pas=='1231':
        time.sleep(1.0)
        
        exit()
        
        market()
    
        
    else:
        messagebox.showinfo('خطأ','خاول مره اخري')                      


##############title#############
title=Label(ppro,text='اهلا بك في صفحه تسجيل الدخول الي السوبر ماركت',font='bold 15',
            bg='#00F1FF',fg='#000000')
title.pack(fill=X)

######################frame###########
f1=Frame(ppro,width=300 ,height=700,bg='#BDC3C7')
f1.place(x=600 ,y=29)



#####################
l1=Label(f1,text=' السوبر ماركت',bg='#FEFEFF', font='bold 15',width=30)
l1.place(x=1, y=50)

##########################
b1=Button(f1,text='حسابات السوشيال ميديا ', width=30,
          bg='#00F1FF',foreground="black",font='bold 15')
b1.place(x=1 ,y=100)
b2=Button(f1,text='واتس اب ', width=30,bg='#00F1FF',
          foreground="black",font='bold 15',command=open1)
b2.place(x=1 ,y=150)
b3=Button(f1,text=' قيس بوك ', width=30,bg='#00F1FF',
          foreground="black",font='bold 15',command=open2)
b3.place(x=1 ,y=200)
b3=Button(f1,text='مطور البرنامج', width=30,
          bg='#00F1FF',foreground="black",font='bold 15', command=abuot1)
b3.place(x=1 ,y=250)
#####################image######
photo=PhotoImage(file='im.png')

imo=Label(ppro,image=photo,)
imo.place(x=23, y=35,)


f2=Frame(ppro,width=600 ,height=650,bg='#BDC3C7')
f2.place(x=0 ,y=500)

photo1=PhotoImage(file='mm.png')
imo2=Label(ppro,image=photo1)
imo2.place(x=430,y=330, width=170,height=170)


lf2=Label(ppro,text='اسم المستخدم',font='bold 20',bg='#BDC3C7')
lf2.place(x=630,y=380,width=250,height=30)

en1=Entry(ppro,bg='#00FFFF',font='bold 15',width=250,justify='right')
en1.place(x=630,y=420, width=250 ,height=35)


en2=Entry(ppro,bg='#00FFFF',font='bold 15',show='*',justify='right')
en2.place(x=630,y=480, width=250 ,height=35)

lf2=Label(ppro,text='كلمه السر',font='bold 20',bg='#BDC3C7')
lf2.place(x=630,y=450,width=250,height=30)



bu1=Button(ppro,text='تسجيل دخول',
           activebackground='#FFFF00', font='bold 20',command=log)
bu1.place(x=630 ,y=530,width=250 ,height=40)


photo2=PhotoImage(file='mmr1.png')

lf3=Label(ppro,image=photo2)
lf3.place(x=200 ,y=500)








ppro.mainloop()