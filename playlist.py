# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 04:58:18 2020

@author: girik
"""

import os

#This func gives a list of songs with entire names in folder
#This will be used for loading the music in the player using file path
def song_names_in_path(path):
    #Main list of songs but WITH .mp3 extension in file name
    All_Music_With_mp3 = []
    
    #Folder name of songs (by changing names you change list of songs)
    path = path # 'Halsey_Music' 'Eminem_Music' 
    
    #Loop to iterate through file to get all the music 
    for folder, subfolder, files in os.walk(path):
        
        for f in files:
            
            All_Music_With_mp3.append(f)
    
    return All_Music_With_mp3

#This func gives a list of songs with names of songs
#This will be used for displaying the music names for the user
def list_of_songs(path):
    
    #Just a temporary str which corresponds to All_Music_Without_mp3
    For_Removing_mp3 = ''
    
    #Main list of songs but WITHOUT .mp3 extension in file name
    Final_Music_Without_mp3 = []
    
    for i in song_names_in_path(path):
    
        For_Removing_mp3 = i[:-4]
        Final_Music_Without_mp3.append(For_Removing_mp3)

    return Final_Music_Without_mp3
    
             
        

