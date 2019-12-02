from socket import socket
from tkinter import *
import tone_analysis_api
class application:
    def __init__(self,master):
        self.data=""
        self.flag=0
        self.f=(master)
        self.f.grid()
        self.host=''
        self.port=5000
        self.mySocket = socket()
        self.mySocket.bind((self.host,self.port))
        self.mySocket.listen(1)
        self.cr()

    def cr(self):
        self.l=Label(self.f,text="  ")
        self.l.grid();
        self.t=Text(self.f,height=5,width=30,wrap=WORD)
        self.t.grid(columnspan=2,row=5,column=4)
        self.l1=Label(self.f,text="  ")
        self.l1.grid();
        self.b1=Button(self.f,text="Read")
        self.b1.grid(row=9,column=4)
        self.b2=Button(self.f,text="Un-wrap")
        self.b2.grid(row=9,column=5)
        self.b1["command"]=self.read_data
        self.b2["command"]=self.unwrap_data
        self.l2=Label(self.f,text="  ")
        self.l2.grid();

    def read_data(self):
        self.data=""
        conn,addr = self.mySocket.accept()
        self.data = conn.recv(1024).decode()
        x=tone_analysis_api.cl_ana(self.data)
        if x==0 :
            self.t.delete(0.0,END)
            self.t.insert(0.0,self.data)
            conn.close()
        else:
            self.flag=1
            self.t.delete(0.0,END)
            self.t.insert(0.0,"Agressive Message.Press Un-wrap to check content")
            conn.close()
    def unwrap_data(self):
        if self.flag==0:
            self.t.delete(0.0,END)
            self.t.insert(0.0,"No data to un-wrap")
        else:
            self.flag=0
            self.t.delete(0.0,END)
            self.t.insert(0.0,self.data)


root=Tk()
root.geometry("270x180")
root.title("Server")
app=application(root)
root.mainloop()
