# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:13:04 2021

@author: hp
"""

from tkinter import *
from Space_Invader import main_menu

root = Tk()
root.geometry("900x900")





btn = Button(root,text="click",command = main_menu)
btn.pack()




root.mainloop()