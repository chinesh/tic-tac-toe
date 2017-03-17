import Tkinter
from Tkinter import *
import tkMessageBox

i=0

class Game:
    def check(self):
        if(self.button1["text"]=="X" and self.button2["text"]=="X" and self.button3["text"]=="X" or
             self.button4["text"]=="X" and self.button5["text"]=="X" and self.button6["text"]=="X" or
             self.button7["text"]=="X" and self.button8["text"]=="X" and self.button9["text"]=="X" or
             self.button1["text"]=="X" and self.button4["text"]=="X" and self.button7["text"]=="X" or
             self.button2["text"]=="X" and self.button5["text"]=="X" and self.button8["text"]=="X" or
             self.button3["text"]=="X" and self.button6["text"]=="X" and self.button9["text"]=="X" or
             self.button1["text"]=="X" and self.button5["text"]=="X" and self.button9["text"]=="X" or
             self.button7["text"]=="X" and self.button5["text"]=="X" and self.button3["text"]=="X" ):
            tkMessageBox.showinfo("winner","x is the winner")

        elif(self.button1["text"]=="O" and self.button2["text"]=="O" and self.button3["text"]=="O" or
             self.button4["text"]=="O" and self.button5["text"]=="O" and self.button6["text"]=="O" or
             self.button7["text"]=="O" and self.button8["text"]=="O" and self.button9["text"]=="O" or
             self.button1["text"]=="O" and self.button4["text"]=="O" and self.button7["text"]=="O" or
             self.button2["text"]=="O" and self.button5["text"]=="O" and self.button8["text"]=="O" or
             self.button3["text"]=="O" and self.button6["text"]=="O" and self.button9["text"]=="O" or
             self.button1["text"]=="O" and self.button5["text"]=="O" and self.button9["text"]=="O" or
             self.button7["text"]=="O" and self.button5["text"]=="O" and self.button3["text"]=="O" ):
            tkMessageBox.showinfo("winner","O is the winner")

    def move(self,buttons):
        global i
        if(i%2==0 and buttons["text"]==" "):
            buttons["text"]= "X"
            i+=1
            self.check()

        elif(1%2!=0 and buttons["text"]==" "):
            buttons["text"]="O"
            i+=1
            self.check()



    def __init__(self,p1,p2):

        root = Tkinter.Tk()
        root.title("Tic Tac Toe")
        cv = Canvas(root,width=450,height=25,bg="gray")
        attrFrame = Frame(root)
        L1 = Label(root, text="O or X")
        L1.pack( side = TOP)
        E1 = Entry(root, bd =5)
        E1.pack(side = TOP)
        cv.pack()
        topFrame = Frame(root)

        self.button1=Tkinter.Button(topFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button1))
        self.button2=Tkinter.Button(topFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button2))
        self.button3=Tkinter.Button(topFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button3))
        for widget in self.button1,self.button2,self.button3:
            widget.pack(side=LEFT)
        topFrame.pack(side=TOP)
        centreFrame = Frame(root)
        self.button4=Tkinter.Button(centreFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button4))
        self.button5=Tkinter.Button(centreFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button5))
        self.button6=Tkinter.Button(centreFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button6))
        for widget in self.button4,self.button5,self.button6:
            widget.pack(side=LEFT)
        centreFrame.pack(side=TOP)
        bottomFrame = Frame(root)
        self.button7=Tkinter.Button(bottomFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button7))
        self.button8=Tkinter.Button(bottomFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button8))
        self.button9=Tkinter.Button(bottomFrame,height=10,width=15,activebackground="black",padx=15,text=" ",borderwidth=2,command=lambda:self.move(self.button9))
        for widget in self.button7,self.button8,self.button9:
            widget.pack(side=LEFT)
        bottomFrame.pack(side=TOP)
        root.mainloop()



if __name__=="__main__":
    Game(4,5)

