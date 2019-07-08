from tkinter import *
import os
root = Tk()
def openProgram():
	try:
		os.system("python3 C:\Program.py")
	except:
		os.system("py C:\Program.py")
	except:
		os.system("python3 \Program.py")
	except:
		os.system("py \Program.py")
myBtn = Button(root, bd = 5, text = "Open the program", command = openProgram)
