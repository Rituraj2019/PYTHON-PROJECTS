
#importing necessary modules
from tkinter import*
from time import strftime
clock=Tk()   #making the clock window using Tk class
clock.title("Digital clock")  #Giving name to that window
lbl=Label(clock,font="arial 160 bold", bg="black",fg="white") #labeling the clock
lbl.pack(anchor="center",fill="both",expand="yes")  #packing the label in the window.

def time():
    string=strftime("%H:%M:%S%p") # %p for AM/PM
    lbl.config(text=string)
    lbl.after(1000,time) #after 1000 means, change in time window after every 1000 millisecond. we can change this
time()
mainloop()  #we can call mail loop method in between code to know working of different methods.
# Main loop method is an infinite loop use to run an apllication, it waits for an event to occur and process the event
#as long as the window is open