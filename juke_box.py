# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 03:37:14 2020

@author: hp
"""

# import everything thats necessary
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from music_player import *
from playlist import list_of_songs
import time
from mutagen.mp3 import MP3
import os
import threading


# ==========================================================================
# ==========================================================================

def go_back():
    os.system('the_arcade.py')


def play_time():
    current_time= pygame.mixer.music.get_pos()/1000

    converted_current_time=time.strftime('%M:%S',time.gmtime(current_time))



    song=song_box.get(ACTIVE)
    song= f'JukeBox/Eminem_Music/{song}.mp3'

    # mutagen

    song_mut=MP3(song)
    song_length=song_mut.info.length
    converted_song_length=time.strftime('%M:%S',time.gmtime(song_length))



    status_bar.config(text=f'Time Elapsed: {converted_current_time}  of  {converted_song_length}',font=5)


    status_bar.after(1000,play_time)



def change_volume(val):

    song =  None


    volume = int(val)/100
    pygame.mixer.music.set_volume(volume)


    song_box.insert(END, song)

# ========================================================================================================
def add_from_pc():
    songs = filedialog.askopenfilenames(initialdir='C:\\users',title="Choose the folder",filetypes=(("mp3 files","*.mp3"),))

    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = song.replace("","")

            song = song.replace(".mp3","")

            song_box.insert(END, song)

def add_eminem():
    songs = list_of_songs('JukeBox/Eminem_Music')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'JukeBox/Eminem_Music/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)

def side_b():
    songs = list_of_songs('JukeBox/Eminem_Music/Side b')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Side b/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Kamikaze():
    songs = list_of_songs('JukeBox/Eminem_Music/Kamikaze')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Kamikaze/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Revival():
    songs = list_of_songs('JukeBox/Eminem_Music/Revival')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Revival/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def MMLP2():
    songs = list_of_songs('JukeBox/Eminem_Music/MMPL2')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'MMLP2/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Recovery():
    songs = list_of_songs('JukeBox/Eminem_Music/Recovery(deluxe)')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Recovery(deluxe)/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)



def Relapse():
    songs = list_of_songs('JukeBox/Eminem_Music/Relapse')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Relapse/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Just_Lose_it():
    songs = list_of_songs('JukeBox/Eminem_Music/Just Lose It')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Just Lose It/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Encore():
    songs = list_of_songs('JukeBox/Eminem_Music/Encore')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Encore/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def The_Eminem_show():
    songs = list_of_songs('JukeBox/Eminem_Music/The Eminem Show')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'The Eminem Show/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def MMLP():
    songs = list_of_songs('JukeBox/Eminem_Music/MMLP')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'MMLP/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)


def Slim_Shady_LP():
    songs = list_of_songs('JukeBox/Eminem_Music/Slim Shady LP')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Slim Shady LP/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)



def MTBMB():
    songs = list_of_songs('JukeBox/Eminem_Music/Music To Be Murdered By')
    for song in songs:
        # for subdirs, dirs, files in walk('Eminem_Music/'):
            song = f'Music To Be Murdered By/{song}'

            song = song.replace(".mp3","")

            song_box.insert(END, song)




def next_song():

    current_song=song_box.curselection()

    next_one=current_song[0]+1

    song=song_box.get(next_one)
    song= f'JukeBox/Eminem_Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0,END)

    song_box.activate(next_one)
    song_box.selection_set(next_one,last=None)


def previous_song():

    current_song=song_box.curselection()
    previous_one=current_song[0]-1
    song=song_box.get(previous_one)

    song= f'JukeBox/Eminem_Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    song_box.selection_clear(0,END)

    song_box.activate(previous_one)
    song_box.selection_set(next_one,last=None)


def stop_music():
    pygame.mixer.music.stop()
    status_bar.config(text="")
    song_box.selection_clear(song_box.curselection())




global paused
paused=False

def pause_music(is_paused):
    global paused

    paused= is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused=False
    else:
        pygame.mixer.music.pause()
        paused=True


def delete_song():
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()

def delete_all_songs():
    song_box.delete(0,END)
    pygame.mixer.music.stop()



def play_music():
    song=song_box.get(ACTIVE)
    song= f'JukeBox/Eminem_Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()
    song_box.curselection()


root=Tk()
root.geometry('650x600')
root.iconbitmap('JukeBox/icons/eminem_icon.ico')
root.title("JUKE BOX")



# creating a control frame
controls_frame=Frame(root)
controls_frame.pack()


# create Playlist Box
song_box= Listbox(root, bg="black", fg="green",font=8,height=15, width=65,selectbackground="green", selectforeground="black")
song_box.pack(anchor="n",pady=20)

# creating name label
name_label=Label(controls_frame,text="JUKE BOX")
name_label.config(font=('Arial',25))
name_label.grid(row=0,column=2,pady=5,sticky=N)

# creating previous button
previous_btn_label = Label(root)
previous_btn_img = PhotoImage(file='JukeBox/buttons/previous.png')
previous_btn_label.config(image=previous_btn_img)
previous_btn = Button(controls_frame,image=previous_btn_img,bd=0,command=lambda:previous_song())
previous_btn.grid(row=1,column=0,padx=10)



# creating next button
next_btn_label = Label(root)
next_btn_img = PhotoImage(file='JukeBox/buttons/next.png')
next_btn_label.config(image=next_btn_img)
next_btn = Button(controls_frame,image=next_btn_img,bd=0,command=lambda:next_song())
next_btn.grid(row=1,column=1,padx=10)


# creating pause button
pause_btn_label = Label(root)
pause_btn_img = PhotoImage(file='JukeBox/buttons/pause.png')
pause_btn_label.config(image=pause_btn_img)
pause_btn = Button(controls_frame,image=pause_btn_img,bd=0,command=lambda:pause_music(paused))
pause_btn.grid(row=1,column=2,padx=10)



# creating play button
play_btn_label = Label(root)
play_btn_img = PhotoImage(file='JukeBox/buttons/play.png')
play_btn_label.config(image=play_btn_img)
play_btn = Button(controls_frame,image=play_btn_img,bd=0,command=lambda:play_music())
play_btn.grid(row=1,column=3,padx=10)



# creating stop button
stop_btn_label = Label(root)
stop_btn_img = PhotoImage(file='JukeBox/buttons/stop.png')
stop_btn_label.config(image=stop_btn_img)
stop_btn = Button(controls_frame,image=stop_btn_img,bd=0,command=lambda:stop_music())
stop_btn.grid(row=1,column=4,padx=10)


gobacklabel = Label(root)
# stop_btn_img = PhotoImage(file='JukeBox/buttons/stop.png')
# stop_btn_label.config(image=stop_btn_img)
back_btn = Button(root,text='go back',command=threading.Thread(target = go_back).start())



# creating volume slider
controls_frame2=Frame(root)
controls_frame2.pack()

VolumeSliderLabel=Label(controls_frame2,text="Volume  ",font="Arial 15")
VolumeSliderLabel.grid(row=0,column=0,sticky=S)

VolumeSlider=Scale(controls_frame2,from_=0, to=100,orient=HORIZONTAL,length=135,command=change_volume)
pygame.mixer.music.set_volume(0.6)
VolumeSlider.set(60)
VolumeSlider.grid(row=0,column=1,padx=5)


#main menu
my_menu =  Menu(root)
root.config(menu=my_menu)

#sub menu
addsong_menu = Menu(my_menu,tearoff = False)
my_menu.add_cascade(label='Add Music', menu=addsong_menu)

#sub menu of sub menu
add_eminem_songs = Menu(addsong_menu,tearoff = False)

addsong_menu.add_cascade(label='Add Eminem Albums', menu=add_eminem_songs)

add_eminem_songs.add_command(label = 'MTBMB Side b (deluxe)', command=side_b)
add_eminem_songs.add_separator()

add_eminem_songs.add_command(label = 'Music to be murdered By', command=MTBMB)
add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Kamikaze', command=Kamikaze)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Revival', command=Revival)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Marshal Mathers LP 2', command=MMLP2)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Rcovery(Deluxe)', command=Recovery)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Relapse', command=Relapse)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Just Lose It', command=Just_Lose_it)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Encore', command=Encore)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'The Eminem Show', command=The_Eminem_show)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'Marshal Mathers LP', command=MMLP)
# add_eminem_songs.add_separator()

# add_eminem_songs.add_command(label = 'The Slim Shady LP', command=Slim_Shady_LP)
# add_eminem_songs.add_separator()

#sub menu
#for pc music
#addsong_menu.add_command(label="Add songs from your computer",command=add_from_pc)

delete_song_menu = Menu(my_menu, tearoff = False)
my_menu.add_cascade(label="Remove Songs",menu=delete_song_menu)
delete_song_menu.add_command(label="Delete the selected song from playlist",command=lambda: delete_song())
delete_song_menu.add_command(label="Delete playlist",command= lambda:delete_all_songs())



# crreating status bar
status_bar= Label(root,text='',bd=1,relief=GROOVE,anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=2)

copy_right=Label(root,text='Copyright @2020 "Armaan And Girik"',anchor=S)
copy_right.pack(fill=X,side=BOTTOM)

root.mainloop()
