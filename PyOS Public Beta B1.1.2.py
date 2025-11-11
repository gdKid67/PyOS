import tkinter as tk
import hashlib
username = input('Enter your username: ')
password = input('Enter your password: ')
def New_Window():
    Window = tk.Toplevel()
    canvas = tk.Canvas()
    canvas.pack()
    print("Opened New profile with POS code 0S01")
def New_Console():
    Window = tk.Toplevel()
    canvas = tk.Canvas(Window)
    canvas.pack()
    print("Opened New Console Window with POS code 0S02")
print("Opened PyOS Public beta version 1")
root = tk.Tk()
root.title("New Profile")
root.minsize(298, 70)
root.resizable(False, False)
label1 = tk.Label(text= "Version PB1 (11-11-2025)")
label1.pack()
label2 = tk.Label(text= "By gdKid67")
label2.pack()
button = tk.Button(root, text="New Profile", bg='White', fg='Black', command=lambda: New_Window())
button.pack()
buttonC = tk.Button(root, text="Console", bg='Black', fg='White', command=lambda: New_Console())
buttonC.pack()
root.mainloop()

print("Ended Process on command (POS Code 0X01)")

