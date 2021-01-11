# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 04:42:08 2021

@author: hp
"""

from PIL import Image

image1=Image.open('music.png')
image2=image1.resize((50,50))
image2.save("music2.png")