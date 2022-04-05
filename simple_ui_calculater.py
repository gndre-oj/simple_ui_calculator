from tkinter import *

class Calculator(object):
    global YPOS
    global XPOS
    XPOS = 50
    YPOS = 15
    
    def __init__(self):

        self.window = Tk()
        self.window.title("Taschenrechner")
        self.window.resizable(False, False)
        self.window.geometry("+%d+%d" % (XPOS, YPOS))
        self.window.configure(bg="#3b3b3b")
        
        self.__build()
        self.__display()

    def __calc(self, value):
        self.output.config(state="normal")
        calc = self.output.get()
        calcLen = len(calc)
        calcOpt = ["+","*","/","."]
        if value == "C":
            self.output.delete(0, END)
        elif value == "DEL":
            if calc[-2:calcLen] == "**":
                self.output.delete(calcLen-2, END)
            elif calc[-4:calcLen] == "3.14":
                self.output.delete(calcLen-4, END)
            elif calc[-5:calcLen] == "**0.5":
                self.output.delete(calcLen-5, END)
            elif calc[-3:calcLen] == "---":
                self.output.delete(calcLen-1, END)
            else:
                self.output.delete(calcLen-1, END)
        elif value == "=":
            if calcLen > 0 and calc[-1] in calcOpt:
                calc = calc[:-1]
            if calcLen != 0:
                self.output.delete(0, END)
                self.output.insert(0, eval(calc))
        else:
            if calcLen > 0 and value in calcOpt and calc[-1] in calcOpt:
                self.output.delete(calcLen-1, END)
            else:
                self.output.insert(END, value)
        self.output.config(state="disabled")
    
    def __build(self):
        def onExtend():
            grid = [
                (0,0,"-","#333333","-"),
                (5,1,"^x","#3b3b3b","**"),(6,1,"Π","#3b3b3b","3.14"),
                (5,2,"√","#3b3b3b","**0.5"),(6,2,"","#3b3b3b",""),
                (5,3,"","#3b3b3b",""),(6,3,"","#3b3b3b",""),
                (5,4,"","#3b3b3b",""),(6,4,"","#3b3b3b","")
            ]
        grid = [
            (0,0,"-","#333333","-"),
            (0,1,"7","#262626","7"),(1,1,"8","#262626","8"),(2,1,"9","#262626","9"),(3,1,"×","#3b3b3b","*"),(4,1,"÷","#3b3b3b","/"),
            (0,2,"4","#262626","4"),(1,2,"5","#262626","5"),(2,2,"6","#262626","6"),(3,2,"+","#3b3b3b","+"),(4,2,"-","#3b3b3b","-"),
            (0,3,"1","#262626","1"),(1,3,"2","#262626","2"),(2,3,"3","#262626","3"),(3,3,"(","#3b3b3b","("),(4,3,")","#3b3b3b",")"),
            (0,4,"0","#262626","0"),(1,4,"C","#DC143C","C"),(2,4,"DEL","#DC143C","DEL"),(3,4,".","#3b3b3b","."),(4,4,"=","#3b3b3b","=")
        ]
        for (col,row,text,color,item) in grid:
            if col == 0 and row == 0:
                self.output = Entry(self.window, font="Arial", text=text, state="disabled", bd=4)
                self.output.grid(column=col, row=row, columnspan=5, ipady=5, sticky=E+W)
            else:
                button = Button(self.window, text=text, bg=color, fg="white", width=6, height=3, bd=2, command=lambda value=item: self.__calc(value))
                button.grid(column=col, row=row)
    
    def __display(self):
        self.window.mainloop()

Calculator()