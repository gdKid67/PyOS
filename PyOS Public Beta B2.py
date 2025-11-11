import tkinter as os
OS = os.Tk()

UserSpace = os.Frame(master=OS, relief=os.RAISED, width=200, height=200, bg='Gray')
UserSpace.pack(fill=os.BOTH, expand=True)

TB = os.Frame(master=OS, height=50, bg="Black")
TB.pack(fill=os.X)

Start = os.Button(master= TB, text="Start")
Start.pack(fill=os.Y, side=os.LEFT)

LogOut = os.Button(master= TB, text="Log Out", command= OS.quit)
LogOut.pack(fill=os.Y, side=os.LEFT)

OS.attributes('-fullscreen',True)
OS.mainloop()
