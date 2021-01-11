# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:40:58 2021

@author: hp
"""

#audio_player.py
import os
import tkinter as tk
import pygame
import tkinter.filedialog as filedialog
import os
import pygame

def play_all():


    directory = str(filedialog.askopenfile())
    print("Loding files from directory:", directory)
    os.chdir(directory)
    pygame.mixer.init()
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            print("Playing file:", file)
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
            # Wait for the music to play before exiting 
            while pygame.mixer.music.get_busy():   
                pygame.time.Clock().tick(5)

    
def songs_list():
    files = [file for file in os.listdir('side b')]
    List = []
    for file in files:
        List.append(str(file))
        #print(file)
    #print(List)
    return List

def play(song_name):

    song_name_label['text'] = "Now Playing: " + song_name
    pygame.mixer.init()
    pygame.mixer.music.load("./side b/" + song_name)
    print("Playing:", song_name)
    pygame.mixer.music.play()

window = tk.Tk()
window .title("Any Name")
Height = 720
Width = 1080

# define size of window
canvas = tk.Canvas(window, bg='#3cd1fa',  height=Height, width=Width)
canvas.pack()

# play button **************************************************
play_button_frame = tk.Frame(window)
play_button_frame.place(relx=0.40, rely=0.88, relheight=0.1, relwidth=0.10)

play_button = tk.Button(play_button_frame, text="Play", font=25, fg='#d1d1d1', bg='black',
                        command=lambda: play(listbox.get(listbox.curselection()))  )
play_button.place(relx=0.01, rely=0.005, relheight=0.98, relwidth=0.49)


play_all_button = tk.Button(window, text = "play_all",command= lambda:play_all())
play_all_button.pack()


#list box (playlist) *************************************************
listbox_frame = tk.Frame(window, bg='green')
listbox_frame.place(relx=0.7, rely=0.2, relheight=0.6, relwidth=0.29)

listbox = tk.Listbox(listbox_frame, bg="white", selectmode='ACTIVE')
listbox.place(relx=0.01, rely=0.01, relheight=0.98, relwidth=0.98)

# song name *****************************************************************
song_name_frame = tk.Frame(window, bg='white')
song_name_frame.place(relx=0.20, rely=0.1, relheight=0.05, relwidth=0.60)
song_name_label = tk.Label(song_name_frame,font=("times now roman", 10))
song_name_label.place(relx=0.0, rely=0, relheight=1, relwidth=1)

# PLaylist, to display song in the list
playlist = songs_list()
for item in playlist:
    listbox.insert(tk.END, item)
# auto selecting 1st element of list box
listbox.selection_set( first = 0 )

window.mainloop()