from tkinter import ttk
import tkinter as os
import datetime as dt
OS = os.Tk()
Version = "Beta 4"
BGColour = "Gray"
TBColour = "White"
#for patch notes
FGColour = "White"
TBGColour = "Black"
OS.config(cursor="arrow")
current_time = dt.datetime.now()
UserSpace = os.Frame(master=OS, relief=os.RAISED, width=200, height=200, bg=BGColour,)
UserSpace.pack(fill=os.BOTH, expand=True)
PyOS = os.Label(master=UserSpace, text="PyOS", bg=BGColour, fg=FGColour, font=("Times", "100", "bold"))
PyOS.pack(side=os.TOP)
PyOS3 = os.Label(master=UserSpace, text=Version, bg=BGColour, fg=FGColour, font=("Times", "30", "bold"))
PyOS3.pack(side=os.TOP)
PyOS4 = os.Label(master=UserSpace, text="Release of PyOS", bg=BGColour, fg=FGColour, font=("Times", "30", "bold"))
PyOS4.pack(side=os.TOP)
TB = os.Frame(master=OS, height=90, bg=TBColour)
TB.pack(fill=os.X, side=os.BOTTOM)
Start = os.Button(master= TB, text="Start", fg= TBGColour, bg=TBColour)
Start.pack(fill=os.Y, side=os.LEFT)
LogOut = os.Button(master= TB, text="Log Out", fg= TBGColour, bg=TBColour, command= OS.quit)
LogOut.pack(fill=os.Y, side=os.LEFT)
Spacer2 = os.Frame(master=TB,width=5, bg=TBColour)
Spacer2.pack(side=os.RIGHT)
PatchNotes = os.Label(master=TB, text="Version BETA4", fg= TBGColour, bg=TBColour)
PatchNotes.pack(side=os.RIGHT)
DateTime = os.Label(master=TB, text=f"{current_time}", fg= TBGColour, bg=TBColour)
DateTime.pack(side=os.RIGHT)

###################################################################################

Window = os.Frame(master=UserSpace, width= 200, height= 150,)
Window.place(x=100, y=100)

Content = os.Frame(master=Window, width= 200, height= 130, bg='Black')
Content.pack(fill=os.X, side=os.BOTTOM)

Head = os.Frame(master=Window, width= 200, height= 20)
Head.pack(fill=os.X, side=os.BOTTOM)


def start_drag(event):
    Window.x = event.x
    Window.y = event.y

def do_drag(event):
    x = Window.winfo_x() + event.x - Window.x
    y = Window.winfo_y() + event.y - Window.y
    Window.place(x=x, y=y)


Head.bind("<Button-1>", start_drag)
Head.bind("<B1-Motion>", do_drag)

OS.attributes('-fullscreen',True)
OS.mainloop()
