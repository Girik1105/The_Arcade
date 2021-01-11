# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:50:35 2020

@author: girik
"""


from tkinter import *

root=Tk()
root.geometry=("1000x1000")
root.title("Music Marathon")


#main menu
my_menu =  Menu(root)
root.config(menu=my_menu)

#sub menu
addsong_menu = Menu(my_menu)
my_menu.add_cascade(label='Add Music', menu=addsong_menu)

#sub menu of sub menu
add_eminem = Menu(addsong_menu)
addsong_menu.add_cascade(label='Add Eminem Playlists', menu=add_eminem)
add_eminem.add_command(label = 'Side b', command = add_eminem)

#sub menu of sub menu
add_Halsey = Menu(addsong_menu)
addsong_menu.add_cascade(label='Add Halsey Playlists', menu=add_Halsey)
add_Halsey.add_command(label = '2015', command = add_Halsey)
add_Halsey.add_command(label = '2015', command = add_Halsey)



root.mainloop()