def entry():
    r=[]
    e=[0]*(9)
    a1,b1=10,19
    r.append(randint(1,9))
    for i in range(1,8):
        x=randint(a1,b1)
        r.append(x)
        a1+=10
        b1+=10
    r.append(randint(80,90))    
    
    while len(r)!=15:
        y1=randint(1,90)
        j1=int(y1/10)
        if y1==90:
            j1=8
        if e[j1]<2:
            if y1 not in r:
                e[j1]+=1
                r.append(y1)      
    r.sort()
    #print(r)
    return r

from tkinter import *
from random import randint

root=Tk()
root.title("HOUSIE")
root.geometry("800x350+50+30")
root.configure(bg="#f9f0af")

top,mid,btm=[],[],[]
f=[0]*(4)
line=[0,0,0]
#c=[[0]*(100)]*(4)
c=[0]*(100)
l=[0]*(100)
#l=[[0]*(100)]*(4)

def display(k=0):
    t=[0]*(91)
    temp=top+mid+btm
    for i in temp:
        t[i]=l[i].get()
    str=""
    c=0
    if t[top[0]]==1 and t[top[1]]==1 and t[top[2]]==1 and t[top[3]]==1 and t[top[4]]==1 and set(top).issubset(set(done)):
        str+="  Top Row  "
        c+=1
    
    if t[mid[0]]==1 and t[mid[1]]==1 and t[mid[2]]==1 and t[mid[3]]==1 and t[mid[4]]==1 and set(mid).issubset(set(done)):
        str+="  Middle Row  "
        c+=1
    if t[btm[0]]==1 and t[btm[1]]==1 and t[btm[2]]==1 and t[btm[3]]==1 and t[btm[4]]==1 and set(btm).issubset(set(done)):
        str+="  Bottom Row  "
        c+=1
    if c==3:
        str="FULL HOUSIE!!!"
    if str=="":
        str="SORRY NO PRIZE YET !!"
    lb1=Label(root,text=str,bg="#cc3333",fg='gold',font=('Helvetica',10,'bold'))
    lb1.place(x=140,y=145,width=250,height=40)


#Generating Ticket
b=50
for k in range(1):
    f[k]=Frame(root,bg="#f0a979",width=350,height=130) 
    #f[k].grid(row=k+1,column=0,columnspan = 4)
    f[k].place(x=50,y=b)
    b+=130
    #f[k].propagate(0)
    
    r=entry()
    for i in r:
        l[i]=IntVar()
    
    for i in r:
        #c[i]=Checkbutton(f[k],text=i,variable=l[i],bg="blue",command=display)
        c[i]=Checkbutton(f[k],text=i,variable=l[i],bg="#cc3333",font=('Helvetica',9,'bold'))#"#996633")
    
    i=0
    rw=1
    col=0
    while i<15:
        col=int(r[i]/10)
        if r[i]==90:
            col=8
        if line[rw]<5:
            c[r[i]].grid(row=rw,column=col)
            line[rw]+=1
            if rw==0:
                top.append(r[i])
            elif rw==1:
                mid.append(r[i])
            elif rw==2:
                btm.append(r[i])
            i+=1
        rw=int((rw+1)%3)
    bb1=Button(root,text="Claim",command=lambda:display(0))
    bb1.place(x=60,y=145,width=60,height=40) 
    #bb2=Button(root,text="Claim2",command=lambda:display(1))
    #bb2.place(x=60,y=200,width=60,height=40)
    print(line)
    
def newno(n):
    done.append(n)
    s=str(n)+"\n\nNo.s Completed: "+str(len(done))
    l1=Label(f1,text=s,fg="gold",bg='#cc3333',font=('Arabic',10,'bold'))
    l1.place(x=30,y=70,width=150,height=50)
def generated():
    done.sort()
    print(done)
    
#Generating Token no.'s  
s=""
num=[]
done=[]
for i in range(1,91):
    num.append(i)
f1=Frame(root,bg="#cc3333",width=200,height=200)
f1.place(x=500,y=25)
b=Button(f1,text="NEXT NUMBER",command=lambda:newno(num.pop(randint(0,len(num)-1))))
b.place(x=60,y=15,width=85,height=40)
b1=Button(f1,text="GENERATED\nNUMBERS",command=generated)
b1.place(x=60,y=140,width=85,height=40)    

root.mainloop()