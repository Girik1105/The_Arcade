# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 20:44:52 2020

@author: girik
"""

from playlist import list_of_songs

def ask_song(path):
    while True:
        try:
            user = input('Enter the name of the song you want to play:')
        except:
            print('Wrong input, please try again!')
        else:
            if user in list_of_songs(path):
                return f'{user}.mp3'
                break
            else:
                print('Please enter a song from the available choices')  
                
def queue_song(path):
    while True:
        try:
            user = input('Add to queue:')
        except:
            print('Wrong input, please try again!')
        else:
            if user in list_of_songs(path):
                return f'{user}.mp3'
                break
            else:
                print('Please enter a song from the available choices')  
                