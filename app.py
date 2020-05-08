'''by @anactualhuman_
Calculator which outputs your input
#### https://ihumanbeing.github.io ####
'''

from tkinter import *

result = input("Enter result: ")

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
def btnClearDisplay():
    global operator
    operator=""
    text_input.set("")
    
def btnEqualsInput():
    global result
    text_input.set(result)
    
cal = Tk()
cal.title("Calculator")
cal.resizable(0,0)
cal.iconbitmap('icon.ico')
operator=""
text_input = StringVar()

txtDisplay = Entry(cal, font=("arial", 20, "bold"), textvariable = text_input, bg="powder blue", justify= "right").grid(columnspan=4)

#== row 1 ========================================================================================================================
btn7=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="7", command=lambda:btnClick(7)).grid(row=1, column=0)
btn8=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
btn9=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
Addition=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="+", command=lambda:btnClick("+")).grid(row=1, column=3)
#== row 2 ========================================================================================================================
btn4=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
btn5=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
btn6=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
Subtraction=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="-", command=lambda:btnClick("-")).grid(row=2, column=3)
#== row 3 ========================================================================================================================
btn1=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="1", command=lambda:btnClick(1)).grid(row=3, column=0)
btn2=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
btn3=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="3", command=lambda:btnClick(3)).grid(row=3, column=2)
Multiply=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="*", command=lambda:btnClick("*")).grid(row=3, column=3)
#== row 4 ========================================================================================================================
btn0=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="0", command=lambda:btnClick(0)).grid(row=4, column=0)
btinClear=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="C", command=btnClearDisplay).grid(row=4, column=1)
btnEquals=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="=", command=btnEqualsInput).grid(row=4, column=2)
Divide=Button(cal, padx=16, pady=16, bd = 0, fg="black", font=("arial", 20, "bold"), text="/", command=lambda:btnClick("/")).grid(row=4, column=3)

cal.mainloop()
