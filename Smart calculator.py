from tkinter import * #we are making GUI application so we need tkinter


#defining different operations for calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm(a,b):
    L=max(a,b)  #initializing L (Not as L=0 because time complexity will increase inside the loop)
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L  #if any multiple pof both a and b
        L=L+1
    return L #if no multiple of a and b then return max(a,b) or L

def hcf(a,b):
    H=min(a,b)
    while H<a*b:
        if H%a==0 and H%b==0:
            return H
        H=H-1
    return H

#now we will check the input from user as to what operations do they want
def extract_from_text(text):
    l=[]
    for t in text.split(" "):  #we are splitting the text from user
        try:       #we try to convert splited part to float. If that is converted to float form, that mean it is needed
            #as that is number
            float(t)
            l.append(float(t))  #we then append that float number as that will be needed for caclulations

        except ValueError:  #if not converted into float then pass
            pass

    return l  #returning l for further operations

def calculate():
    text=textin.get()  #getting text from textin using get method
    for word in text.split(" "): #we will check if the word is availaible in the operations dictionary
        if word.upper() in operations.keys(): #if word in dictionary eg:addition
            try:
                l=extract_from_text(text) #checking the numbers in extract_from_text
                r=operations[word.upper()](l[0],l[1]) #we are passing l0 and l1 inside the operation, eg:add(l0,l1)
                list.delete(0,END) #list is the output bar defined below, delete all elements of it
                list.insert(END,r)  #insert end and result calculated to display in list bar.

            except:  #if the word is not in the operations.keys
                list.delete(0,END)
                list.insert(END,"something went wrong, please re-enter the operation")

            finally:
                break
        else: #in any other case
            list.delete(0, END)
            list.insert(END, "something went wrong, please re-enter the operation")






#we have now defined all the operations, lets now define the dictionary which contain similar words for making our
#calculator smart
operations={"+":add, 'ADD':add, 'sum':add, 'Addition':add, 'plus':add,"-":sub, 'SUB':sub, 'subtraction':sub, "minus":sub
            , "difference":sub, "lcm":lcm, "LCM":lcm,"HCF":hcf, "hcf":hcf,"*":mul,"MULTIPLY":mul,"mul":mul,"product":mul
            , "div":div,"DIVIDE":div,"division":div,"modulus":mod,"mod":mod,"%":mod,"reminder":mod}



#making front end of the calculator
calc=Tk()  #making the window for our application
calc.geometry("500x300") #setting dimensions of cal
calc.title("Smart Calculaor")  #title of calc
calc.configure(background="Green") #background colour config. of calc


#front end label
l1=Label(calc,text="Welcome to Smart Calculator", font="Cambria 12 bold",width=25,padx=3)#using lalel method of tkinter
l1.place(x=150,y=10)

l2=Label(calc,text="You can operate many mathematical operations", font="Cambria 12 bold",width=45,padx=3)#using lalel method of tkinter
l2.place(x=50,y=40)

l3=Label(calc,text="Please enter the operation", font="Cambria 12 bold",width=25,padx=3)#using lalel method of tkinter
l3.place(x=150,y=100)

textin=StringVar()
e1= Entry(calc, width=25,textvariable=textin)  #creating entry bar
e1.place(x=180,y=150) #placing entry bar

b1= Button(calc, text="Calulate result", font="Cambria 12 bold", command=calculate)  #we have deifned the calculate above
b1.place(x=195,y=190)

#creating list box for displaying result
list= Listbox(calc, width=30, height=3)
list.place(x=160,y=240)



calc.mainloop()