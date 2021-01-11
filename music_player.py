# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 04:33:38 2020

@author: girik
"""

import pygame

from playlist import *

from ask_song import *

queue=[]

pygame.mixer.init()

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
    


# def stop_music():
#     pygame.mixer.music.stop()
#     song_box.selection_clear(ACTIVE)
    
#     status_bar.config(text='')

def volume(num):
    
    pygame.mixer.music.set_volume(num)

def get_volume():
    return pygame.mixer.music.get_volume()    

def queue():
    pygame.mixer.music.queue(User_Played_queue) 

def next_song():
    
    current_song=song_box.curselection()
    next_one=current_song[0]+1
    song=song_box.get(next_one)
    song= f'Halsey_Music/{song}.mp3'
    
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    
    


