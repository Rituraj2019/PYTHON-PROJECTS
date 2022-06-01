from tkinter import*  #import* meaning you import all the objects present in that module
from tkcalendar import*
root=Tk()  #making an object of Tk class to make a window
root.title("Calender")  #using title method of Tk class for giving title
root.geometry("600x400") #using geometry method of Tk class for assigning geometry

cal=Calendar(root, year=2022, month=4, day=16) #making an object of calendar class
cal.pack(pady=20) #using pack method of calendar class for assigning pad Y axis.
root.mainloop() #running main loop

