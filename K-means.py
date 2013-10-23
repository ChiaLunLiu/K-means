import tkinter
import random
import time
import types
import copy
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        self.group = -1
        self.objectid = -1
class Kmeans:
    def __init__(self):
        self.color = [] #'''color used by K points'''
        self.k = 0      #'''number of K'''
        self.p = []     #'''sample points'''
        self.gp = []    #'''points of K'''
        self.num = 0    #'''number of points'''
        self.cnt = 0    #'''number of round'''
        self.initGUI()
    def initGUI(self):
        self.top = tkinter.Tk()
        self.C = tkinter.Canvas(self.top, bg="white", height=400, width=600)
        self.var = tkinter.StringVar()
        self.var1 = tkinter.StringVar()
        self.topFrame = tkinter.Frame(self.top)
        self.labelNum = tkinter.Label(self.topFrame,text="Point")
        self.entryNum = tkinter.Entry(self.topFrame,bd=5)
        self.labelNum.pack(side=tkinter.LEFT)
        self.entryNum.pack(side=tkinter.LEFT)
        self.labelK = tkinter.Label(self.topFrame,text="K")
        self.entryK = tkinter.Entry(self.topFrame,bd=5)
        self.labelK.pack(side=tkinter.LEFT)
        self.entryK.pack(side=tkinter.LEFT)
        self.button_reset = tkinter.Button(self.topFrame, text ="reset", command = self.init2)
        self.button_reset.pack(side = tkinter.LEFT)
        self.button_step = tkinter.Button(self.topFrame, text ="step", command = self.update)
        self.button_step.pack(side=tkinter.LEFT)
        self.button_run = tkinter.Button(self.topFrame, text ="run", command = self.run)
        self.button_run.pack(side=tkinter.LEFT)
        self.label = tkinter.Label(self.top,textvariable=self.var)

        self.var.set(("run :%d" % (self.cnt)))
        self.label.pack()
        self.topFrame.pack()
        self.C.pack()
    def run(self):
        self.update()
        if( self.finished == 0):
            self.top.after(2000,self.run)
    def init2(self):
        k = int(self.entryK.get())
        n = int(self.entryNum.get())
        self.init(k,n)
        self.draw()
    def init(self,k,n):
        self.C.delete("all")
        self.finished = 0
        self.num = n
        self.k = k
        self.color=[]
        self.p=[]
        self.gp=[]
        for i in range(0,k):
            colorString = '#%02x%02x%02x' %(random.randint(0,256),random.randint(0,256),random.randint(0,256))
            self.color.append(colorString)
            t = Point()
            t.x = random.randint(5,590)
            t.y = random.randint(5,390)
            self.gp.append(t)
        for i in range(0,n):
            t = Point()
            t.x = random.randint(5,590)
            t.y = random.randint(5,390)
            self.p.append(t)
    def draw(self):
       # idx = self.C.create_oval(90,90,100,100, fill="blue")
       # idx = self.C.create_oval(150,150,160,160, fill="blue")
       # idx = self.C.create_oval(0,0,10,10, fill="blue")
        for i in range(0,self.num):
            pt = self.p[i]
            idx = self.C.create_oval(pt.x-5,pt.y-5,pt.x+5,pt.y+5, fill="green")
            pt.objectid = idx;
        for i in range(0,self.k):
            pt = self.gp[i]
            idx = self.C.create_oval(pt.x-5,pt.y-5,pt.x+5,pt.y+5, fill=self.color[i])
            pt.objectid = idx;
    def update(self):
        if( self.finished == 1):
            return
        self.cnt = self.cnt +1
        self.var.set(("run :%d" % (self.cnt)))
        new_gp = copy.deepcopy(self.gp)
        count = [1]* self.k
        for i in range(0,self.num):
            m = -1
            idx = -1
            for j in range(0,self.k):
                tx = self.p[i].x - self.gp[j].x
                ty = self.p[i].y - self.gp[j].y
                t = tx*tx + ty*ty
                if ( (m == -1) or (m > t)):
                    m = t
                    idx = j
            self.p[i].group = idx
            count[idx] = count[idx]+1;
            self.C.itemconfig(self.p[i].objectid,fill=self.color[idx])
            new_gp[ idx ].x += self.p[i].x
            new_gp[ idx ].y += self.p[i].y

        #''' compare the old gp and new gp'''
        changed = 0
        for i in range(0,self.k):
            new_gp[i].x = new_gp[i].x//count[i]
            new_gp[i].y = new_gp[i].y//count[i]
        for i in range(0,self.k):
            if( (self.gp[i].x != new_gp[i].x) or (self.gp[i].y != new_gp[i].y)):
                changed = 1

        if changed == 0:
            self.finished = 1
            self.var.set("done")
            return True
        ''' update gp'''
        for i in range(0,self.k):
           self.gp[i] = new_gp[i]
        for i in range(0,self.k):
            self.C.delete(self.gp[i].objectid)
            pt = self.gp[i]
            idx = self.C.create_oval(pt.x-5,pt.y-5,pt.x+5,pt.y+5, fill=self.color[i])
            self.gp[i].objectid = idx
        return False

    def print12(self):
        return self.num

k = Kmeans()
#k.init(5,300)

#k.draw()
#k.top.after(1000,k.update)

k.top.mainloop()


print("done")
