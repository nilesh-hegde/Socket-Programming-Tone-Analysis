import socket
import time
from tkinter import *
import tone_analysis_api
class application:
        def __init__(self,master):
                self.flag=0
                self.msg=""
                self.f=Frame(master)
                self.f.grid()
                self.cr()
        def cr(self):
                self.l=Label(self.f,text="Enter Message to be sent")
                self.l.grid(row=0,column=2)
                self.l3=Label(self.f,text=" ")
                self.l3.grid(row=1,column=2)
                self.t=Text(self.f,height=5,width=30,wrap=WORD)
                self.t.grid(row=1,column=2)
                self.l1=Label(self.f,text=" ")
                self.l1.grid()
                self.b=Button(self.f,text="Send")
                self.b.grid(row=3,column=2)
                self.l2=Label(self.f,text=" ")
                self.l2.grid()
                self.b["command"]=self.ad
        def ad(self):
                if self.flag==0:
                        self.l["text"]="Enter message to be sent"
                self.msg=""
                self.msg=self.t.get(0.0,END)
                host = '192.168.43.145'
                port = 5000

                mySocket = socket.socket()
                mySocket.connect((host,port))

                x=tone_analysis_api.cl_ana(self.msg)
                if x==0 or self.flag==1:
                        self.flag=0
                        mySocket.send(self.msg.encode())
                        self.l["text"]="Message sent"
                        time.sleep(2)
                        self.l["text"]="Enter message to be sent"
                        mySocket.close()
                else:
                        self.flag=1
                        self.l["text"]="Message agrresive in nature. Re-type to send"
                        self.t.delete(0.0,END)
                        mySocket.close()



root=Tk()
root.title("Client")
root.geometry("270x170")

app=application(root)

root.mainloop()
