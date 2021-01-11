# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 22:23:42 2020

@author: girik
"""

import os

def file():
    for folder, subfolder, file in os.walk('downloads'):
        return file


for i in file():
    os.rename(rf'downloads/{i}', rf'edited/{i[17:-25]}.mp3') 