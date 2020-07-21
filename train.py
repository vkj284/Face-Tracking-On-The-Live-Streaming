import tkinter as tk
from tkinter import Message ,Text
import cv2
import os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font

global window
window=tk.Tk()
def changeup():
    c=c26.get()
    d=e26.get()
    ulistf()
    asdf=userpass[klc]
    print(asdf)
    if(asdf==c):
       userdata[klc][1]=d
       ucsvf()
       hom()
       res="Successfully change a password"
       message.configure(text=res)
    else:
        res="password are incorrect"
        message.configure(text=res)
        
    

def hom():
    c2.delete(0, 'end')
    e2.delete(0, 'end')
    g2.delete(0, 'end')
    i2.delete(0, 'end')
    k2.delete(0, 'end')
    c22.delete(0, 'end')
    c23.delete(0, 'end')
    c24.delete(0, 'end')
    c25.delete(0, 'end')
    c26.delete(0, 'end')
    e26.delete(0, 'end')
    res=""
    message.configure(text=res)
    message2.configure(text=res)
    
def sid():
    p=(c24.get())
    listf()
    qw=[]
    for x in data:
        kl=x[0]
        qw.append(kl)
    sf=[]
    for k in range(0,len(data)):
        z=qw[k]   
        if(z==p):
            sf.append(data[k])
            res = pd.DataFrame(sf,columns=['Id','Name','EmailID','Mobileno','Mobileno'])
            message2.configure(text=res)
            res2="You are Search ID is "+p
            message.configure(text=res2)
            clear()
            break
        if(k==len(data)-1):
            res="You are Search ID is not found"
            message.configure(text=res)
            res2=""
            message2.configure(text=res2)
            
def sid2():
    p=(c25.get())
    ulistf()
    sf=[]
    for k in range(0,len(username)):
        z=username[k]
        if(z==p):
            sf.append(userdata[k])
            dataf = pd.DataFrame(sf,columns=['Username','Password','Name','Mobileno','EmailID'])
            message2.configure(text=dataf)
            res2="You are Search Username is "+p
            message.configure(text=res2)
            clear()
        if(z==len(userdata)-1):
            res="You are Search Username is not found"
            message.configure(text=res)
            res2=""
            message2.configure(text=res2)

def clear():
    c2.delete(0, 'end')
    e2.delete(0, 'end')
    g2.delete(0, 'end')
    i2.delete(0, 'end')
    k2.delete(0, 'end')
    c22.delete(0, 'end')
    c23.delete(0, 'end')
    c24.delete(0, 'end')
    c25.delete(0, 'end')
    
def ddata():
    listf()
    p=(c22.get())
    eru=[]
    asd=[]
    for x in data:
        eru.append(x[0])
    for x in data:
        asd.append(x[1])
    for k in range(0,len(data)):
        print(k)
        lk=str(eru[k])
        if(lk==p):
            del data[k]
            q=asd[k]
            csvf()
            mdy="TrainingImage/"
            for x in range(1,63):
                os.remove(mdy+q+"."+p+"."+str(x)+".jpg")
                continue
            clear()
            res = "successfully deleted"
            message.configure(text= res)
            break
        if(k==len(data)-1):
            res="Not found ID"
            message.configure(text=res)
            res2=""
            message2.configure(text=res2)

            
def duser():
    ulistf()
    p=(c23.get())
    eru=[]
    for x in userdata:
        eru.append(x[0])
    print(eru)
    for k in range(0,len(userdata)):
        lk=str(eru[k])
        if(lk==p):
            del userdata[k]
            res = "successfully deleted user account"
            print(res)
            message.configure(text= res)
            ucsvf()
            clear()
            break
        if(k==len(userdata)-1):
            res="Not found Account"
            message.configure(text=res)
            res2=""
            message2.configure(text=res2)
        
def listf():
    global data
    data=[]
    with open("Details\Details.csv") as csva:
        csvr=csv.reader(csva)
        for row in csvr:
            data.append(row)
            
def csvf():
    del data[0]
    dataf = pd.DataFrame(data,columns=["Id","Name","EmailID","PHONENO","address"])
    #print(dataf)
    dataf.to_csv("Details\Details.csv",index=False)
    c=pd.read_csv("Details\Details.csv")
    #print(c)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def TakeImages():        
    Id=(c2.get())
    name=(e2.get())
    email=(g2.get())
    mob=(i2.get())
    add=(k2.get())
    #global names,emails,mobs,adds
    #Ids=str(Id)
    names=str(name)
    emails=str(email)
    mobs=str(mob)
    adds=str(add)
    listf()
    qw=[]
    for x in data:
        kl=x[0]
        qw.append(kl)
        
    if Id in qw:
        res = "already register id try another id"
        message.configure(text= res)
        csvf()

    else:
        if(is_number(Id) and name.isalpha()):
            cam = cv2.VideoCapture(0)
            harcascadePath = "haarcascade_frontalface_default.xml"
            detector=cv2.CascadeClassifier(harcascadePath)
            sampleNum=0
            while(True):
                ret, img = cam.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = detector.detectMultiScale(gray, 1.3, 5)
                for (x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                    #incrementing sample number
                    sampleNum=sampleNum+1
                    #saving the captured face in the dataset folder TrainingImage
                    cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                    #display the frame
                    cv2.imshow('frame',img)
                    #wait for 100 miliseconds 
                    if sampleNum>60:
                        cam.release()
                        cv2.destroyAllWindows()
                        break
                        # break if the sample number is morethan 100
                    elif cv2.waitKey(100) & 0xFF == ord('q'):
                        cam.release()
                        cv2.destroyAllWindows()
                        break
                if sampleNum>60:
                    break
             
            row = [Id, names,emails,mobs,adds]
            '''with open('Details\Details.csv','a+') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(row)
            csvFile.close()'''
            data.append(row)
            csvf()
            clear()
            res = "successfully Registered"
            message.configure(text= res)
            clear()
            
        else:
            if(is_number(Id)):
                res = "Enter Alphabetical Name"
                message.configure(text= res)
            if(name.isalpha()):
                res = "Enter Numeric Id"
                message.configure(text= res)
    
def TrainImages():
    clear()
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Trained Data"#+",".join(str(f) for f in Id)
    message.configure(text= res)

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    clear()
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("Details\Details.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)
    res = "Live streaming"
    message.configure(text= res)
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Unknown'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("ImagesUnknown"))+1
                cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('Tracking',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Track\Track_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    #print(attendance)
    res=attendance
    #message2.configure(text= res)
    df = pd.read_csv(fileName)
    message2.configure(text= df)


def ulistf():
    global userdata
    userdata=[]
    with open ('Login\Login.csv') as csva:
        csvr=csv.reader(csva)
        for row in csvr:
            userdata.append(row)
    global username,userpass
    username=[]
    userpass=[]
    for x in userdata:
        username.append(x[0])
    for x in userdata:
        userpass.append(x[1])
            
def ucsvf():
    del userdata[0]
    dataf = pd.DataFrame(userdata,columns=['Username','Password','Name','Mobileno','EmailID','Address'])
    #print(dataf)
    dataf.to_csv("Login\Login.csv",index=False)
    c=pd.read_csv("Login\Login.csv")
    #print(c)
    
def che():
    c=c1.get()
    d=e1.get()
    #print(c1.get(),e1.get())
    a='admin'
    b='123'
    global alb4
    #print(a,b)
    global un
    un="ADMIN"
    if(c==a and d==b):
        des()
        main()
        a26.place_forget()
        b26.place_forget()
        c26.place_forget()
        d26.place_forget()
        e26.place_forget()
        f26.place_forget()
   
    else:
        res="Invalid Admin name and password"
        abc4.configure(text=res)
        
def che2():
    p=c12.get()
    q=e12.get()
    ulistf()
    global alb4
    for k in range(0,len(userdata)):
        print(k)
        global un
        un=str(username[k])
        up=str(userpass[k])
        if(un==p and up==q):
            global klc
            klc=k
            des()
            main()
            a2.place_forget()
            b2.place_forget()
            c2.place_forget()
            d2.place_forget()
            e2.place_forget()
            f2.place_forget()
            g2.place_forget()
            h2.place_forget()
            i2.place_forget()
            j2.place_forget()
            k2.place_forget()
            l2.place_forget()
            a22.place_forget()
            b22.place_forget()
            c22.place_forget()
            d22.place_forget()
            a23.place_forget()
            b23.place_forget()
            c23.place_forget()
            d23.place_forget()
            a25.place_forget()
            b25.place_forget()
            c25.place_forget()
            d25.place_forget()
            ul.place_forget()
            
        elif(un==p and not(up==q)):
            res="Invalid user name and password"
            abc4.configure(text=res)
           
    ucsvf()
    

def che3():
    global alb4
    rname=c13.get()
    rmobile=e13.get()
    remail=g13.get()
    ruser=i13.get()
    rpass=k13.get()
    raddr=n13.get()
    ulistf()
    if ruser in username:
        res="already register a username try another username"
        abc4.configure(text=res)
    else:
        row = [ruser,rpass,rname,rmobile,remail,raddr]
        userdata.append(row)
        res="Successfully create a account" 
        abc4.configure(text=res)
        c13.delete(0, 'end')
        e13.delete(0, 'end')
        g13.delete(0, 'end')
        i13.delete(0, 'end')
        k13.delete(0, 'end')
        n13.delete(0, 'end')
    ucsvf()

def des():
    a1.destroy()
    b1.destroy()
    c1.destroy()
    d1.destroy()
    e1.destroy()
    f1.destroy()
    a12.destroy()
    b12.destroy()
    c12.destroy()
    d12.destroy()
    e12.destroy()
    f12.destroy()
    a13.destroy()
    b13.destroy()
    c13.destroy()
    d13.destroy()
    e13.destroy()
    f13.destroy()
    g13.destroy()
    h13.destroy()
    i13.destroy()
    j13.destroy()
    k13.destroy()
    j13.destroy()
    k13.destroy()
    l13.destroy()
    m13.destroy()
    n13.destroy()
    abc4.destroy()
    

def des2():
    la2.destroy()
    la22.destroy()
    message.destroy()
    message2.destroy()
    trainImg.destroy()
    trackImg.destroy()
    ul.destroy()
    trl.destroy()
    account.destroy()
    a2.destroy()
    b2.destroy()
    c2.destroy()
    d2.destroy()
    e2.destroy()
    f2.destroy()
    g2.destroy()
    h2.destroy()
    i2.destroy()
    j2.destroy()
    k2.destroy()
    l2.destroy()
    a22.destroy()
    b22.destroy()
    c22.destroy()
    d22.destroy()
    a23.destroy()
    b23.destroy()
    c23.destroy()
    d23.destroy()
    a24.destroy()
    b24.destroy()
    c24.destroy()
    d24.destroy()
    a25.destroy()
    b25.destroy()
    c25.destroy()
    d25.destroy()
    a26.destroy()
    b26.destroy()
    c26.destroy()
    d26.destroy()
    e26.destroy()
    f26.destroy()
    home.destroy()
    logout.destroy()
    logout2.destroy()
    
def logoutt():
    des()
    des2()
    login()
    

def us():
    clear()
    rdata=pd.read_csv("Login\Login.csv")
    message2.configure(text=rdata)
    
def rs():
    clear()
    listf()
    del data[0]
    dataf = pd.DataFrame(data,columns=["Id","Name","EmailID","PHONENO","address"])
    message2.configure(text=dataf)
    
    
def main():
    global home,la2,la22,ul,trl,message,message2,trainImg,trackImg,account,logout,logout2,t1,a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2,a22,b22,c22,d22,a23,b23,c23,d23,a24,b24,c24,d24,a25,b25,c25,d25,a26,b26,c26,d26,e26,f26,sbb

    
    la2= tk.Label(window, text="Notification : ",width=20  ,fg="black"  ,height=2 ,font=('times', 15, ' bold underline ')) 
    la2.place(x=220, y=100)
    
    message= tk.Label(window, text="" ,bg="white"  ,fg="red"  ,width=40  ,height=2, activebackground = "yellow" ,font=('times', 15, ' bold ')) 
    message.place(x=275, y=150)

    
    la22 = tk.Label(window, text=" Message: ",width=20  ,fg="black"   ,height=2 ,font=('times', 15, ' bold  underline')) 
    la22.place(x=210, y=220)
    
    message2 = tk.Label(window, text="" ,fg="green"   ,bg="white",activeforeground = "green",width=51  ,height=6  ,font=('times', 15, ' bold ')) 
    message2.place(x=275, y=290)

    trainImg = tk.Button(window, text="Train Data" ,command=TrainImages ,fg="blue"  ,bg="white"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    trainImg.place(x=25, y=150)

    trackImg = tk.Button(window, text="Live streaming" ,command=TrackImages ,fg="blue"  ,bg="white"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    trackImg.place(x=25, y=200)

    home = tk.Button(window, text="Home" ,command=hom ,fg="blue"  ,bg="white"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    home.place(x=25, y=100)

    trl = tk.Button(window, text="Registered list" ,command=rs ,fg="blue"  ,bg="white"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    trl.place(x=25, y=250)

    ul = tk.Button(window, text="Userlist" ,command=us ,fg="blue"  ,bg="white"  ,width=15  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    ul.place(x=25, y=300)

    account= tk.Label(window, text=un,width=10  ,fg="Red"  ,height=1 ,font=('times', 15, ' bold')) 
    account.place(x=1100, y=25)

    logout= tk.Button(window, text="Logout",command=logoutt,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    logout.place(x=1225, y=5)
    logout2= tk.Button(window, text="Logout&quit",command=window.destroy,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    logout2.place(x=1225, y=50)
    
    t1 = tk.Label(window, text="Face Tracking On The Live Streaming"   ,fg="blue"  ,width=38  ,height=1,font=('times', 30, 'bold')) 
    t1.place(x=200, y=10)
    a2 = tk.Label(window, text="Register",fg="black",width=45 ,bg="white" ,height=2, font=( 'bold') )
    a2.place(x=925, y=100)

    b2= tk.Label(window, text="ID",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b2.place(x=900, y=150)

    c2 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c2.place(x=1100, y=160)

    d2 = tk.Label(window, text="Name",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    d2.place(x=900, y=190)
    
    e2= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    e2.place(x=1100, y=200)

    f2= tk.Label(window, text="Email ID",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    f2.place(x=900, y=230)

    g2 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    g2.place(x=1100, y=240)

    h2 = tk.Label(window, text="Mobile No",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    h2.place(x=900, y=270)
    
    i2= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    i2.place(x=1100, y=280)

    j2 = tk.Label(window, text="Address",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    j2.place(x=900, y=310)
    
    k2= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    k2.place(x=1100, y=320)
    
    l2 = tk.Button(window, text="Register",command=TakeImages,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    l2.place(x=1225, y=355)

    a22 = tk.Label(window, text="Delete",fg="black",width=45 ,bg="white" ,height=2, font=( 'bold') )
    a22.place(x=925, y=400)

    b22= tk.Label(window, text="ID",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b22.place(x=850, y=450)

    c22 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c22.place(x=1050, y=460)

    d22 = tk.Button(window, text="Delete",command=ddata,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    d22.place(x=1225, y=490)

    
    a23 = tk.Label(window, text="Delete User Account",fg="black",width=45 ,bg="white" ,height=2, font=( 'bold') )
    a23.place(x=925, y=540)

    b23= tk.Label(window, text="UserName",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b23.place(x=860, y=600)

    c23 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c23.place(x=1050, y=610)

    d23 = tk.Button(window, text="Delete",command=duser,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    d23.place(x=1225, y=640)

    a24 = tk.Label(window, text="search",fg="black",width=53 ,bg="white" ,height=2, font=( 'bold') )
    a24.place(x=275, y=450)

    b24= tk.Label(window, text="ID",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b24.place(x=215, y=505)

    c24 = tk.Entry(window,width=20 ,bg="white",fg="blue",font=('times', 15, ' bold '))
    c24.place(x=375, y=515)

    d24 = tk.Button(window, text="Search",fg="blue" ,command=sid ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    d24.place(x=600, y=508)

    a25 = tk.Label(window, text="track",fg="black",width=54 ,bg="white" ,height=2, font=( 'bold') )
    a25.place(x=275, y=560)

    b25= tk.Label(window, text="Username",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b25.place(x=205, y=610)

    c25 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c25.place(x=375, y=620)

    d25 = tk.Button(window, text="Search",command=sid2,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    d25.place(x=600, y=615)

    a26= tk.Label(window, text="Change Password",fg="black",width=45 ,bg="white" ,height=2, font=( 'bold') )
    a26.place(x=925, y=100)

    b26= tk.Label(window, text="OldPassword",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b26.place(x=900, y=150)

    c26= tk.Entry(window,width=20 ,show="*",bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c26.place(x=1100, y=160)

    d26= tk.Label(window, text="NewPassword",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    d26.place(x=900, y=190)
    
    e26= tk.Entry(window,width=20 ,show="*",bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    e26.place(x=1100, y=200)

    f26= tk.Button(window, text="change",command=changeup,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    f26.place(x=1225, y=240)

def login():
    global a1,b1,c1,d1,e1,f1,a12,b12,c12,d12,e12,f12,a13,b13,c13,d13,e13,f13,g13,h13,i13,j13,k13,l13,abc4,m13,n13
    window.title("Face tracking on the live streaming")
    t1 = tk.Label(window, text="Face Tracking On The Live Streaming"   ,fg="blue"  ,width=38  ,height=1,font=('times', 30, 'bold')) 
    t1.place(x=225, y=10)
    
    a1 = tk.Label(window, text="ADMIN LOGIN",fg="black",width=40 ,bg="white" ,height=3, font=( 'bold') )
    a1.place(x=120, y=100)
    
    b1 = tk.Label(window, text="Admin Name",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b1.place(x=50, y=190)
    
    c1 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c1.place(x=270, y=200)

    d1 = tk.Label(window, text="Admin Password",width=20  ,fg="black"      ,height=2 ,font=('times', 15, ' bold ')) 
    d1.place(x=50, y=260)
    
    e1 = tk.Entry(window,width=20,show="*"  ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    e1.place(x=270, y=270)

    f1 = tk.Button(window, text="login" ,command=che,fg="blue"  ,bg="white"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    f1.place(x=200, y=370)

    a12 = tk.Label(window, text="USER LOGIN",fg="black",width=40 ,bg="white" ,height=3, font=( 'bold') )
    a12.place(x=525, y=100)

    b12= tk.Label(window, text="UserName",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b12.place(x=475, y=190)
    
    c12 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c12.place(x=680, y=200)

    d12 = tk.Label(window, text="UserPassword",width=20  ,fg="black"      ,height=2 ,font=('times', 15, ' bold ')) 
    d12.place(x=475, y=260)
    
    e12= tk.Entry(window,width=20,show="*"  ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    e12.place(x=680, y=270)

    f12 = tk.Button(window, text="login",command=che2  ,fg="blue"  ,bg="white"  ,width=10  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
    f12.place(x=600, y=370)

    a13 = tk.Label(window, text="Register User Login",fg="black",width=45 ,bg="white" ,height=3, font=( 'bold') )
    a13.place(x=925, y=100)

    b13= tk.Label(window, text="Name",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    b13.place(x=875, y=190)

    c13 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    c13.place(x=1075, y=200)

    d13 = tk.Label(window, text="Mobile no",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    d13.place(x=875, y=260)
    
    e13= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    e13.place(x=1075, y=270)

    f13= tk.Label(window, text="Email ID",width=20  ,height=2  ,fg="black" ,font=('times', 15, ' bold ') ) 
    f13.place(x=875, y=320)

    g13 = tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold '))
    g13.place(x=1075, y=330)

    h13 = tk.Label(window, text="Username",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    h13.place(x=875, y=440)
    
    i13= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    i13.place(x=1075, y=450)

    j13 = tk.Label(window, text="Password",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    j13.place(x=875, y=500)
    
    k13= tk.Entry(window,show="*",width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    k13.place(x=1075, y=510)

    m13 = tk.Label(window, text="Address",width=20  ,fg="black"    ,height=2 ,font=('times', 15, ' bold ')) 
    m13.place(x=875, y=380)
    
    n13= tk.Entry(window,width=20 ,bg="white"  ,fg="blue",font=('times', 15, ' bold ')  )
    n13.place(x=1075, y=390)
    
    l13 = tk.Button(window, text="submit",command=che3 ,fg="blue"  ,bg="white"  ,width=10  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
    l13.place(x=1100, y=570)
    
    abc4 = tk.Label(window, text="" ,fg="red"    ,height=2 ,width=40) 
    abc4.place(x=550, y=450)

    alb5= tk.Label(window, text="FACE TRACKING ON THE LIVE STREAMING "  ,fg="blue"    ,height=2 ,width=40) 
    alb5.place(x=25, y=650)
    
    window.mainloop()
login()
