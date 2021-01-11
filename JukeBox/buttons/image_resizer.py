# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 03:19:03 2020

@author: hp
"""

from PIL import Image

pause_btn_img=Image.open('buttons/pause.png')
pause_btn_img=pause_btn_img.resize((60,60))
pause_btn_img.save('pause.png')

play_btn_img=Image.open('buttons/play.png')
play_btn_img=play_btn_img.resize((60,60))
play_btn_img.save('buttons/play.png')

stop_btn_img=Image.open('buttons/stop.png')
stop_btn_img=stop_btn_img.resize((60,60))
stop_btn_img.save('stop.png')

next_btn_img=Image.open('buttons/next.png')
next_btn_img=next_btn_img.resize((60,60))
next_btn_img.save('buttons/next.png')

previous_btn_img=Image.open('buttons/previous.png')
previous_btn_img=previous_btn_img.resize((60,60))
previous_btn_img.save('previous.png')