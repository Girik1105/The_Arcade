# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:43:33 2021

@author: hp
"""

#coding with sayed

#import tkinter



import pygame as pygame
import flappy
import Space_Invader
import os
import random
from playsound import playsound

pygame.init()
pygame.display.set_caption("The Arcade")
icon = pygame.image.load('arcade_assets/arcade_bg.png')
pygame.display.set_icon(icon)
pygame.mixer.music.load('crazzy.mp3')
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(-1 )

screen = pygame.display.set_mode((900, 900))
# bg = pygame.image.load("arcade_assets/arcade_bg.png")
BG = pygame.transform.scale(pygame.image.load("arcade_assets/arcade_bg_fin_2.png"),((900,900)))

FONT = pygame.font.SysFont('Comic Sans MS', 32)
# Default button images/pygame.Surfaces.
IMAGE_NORMAL = pygame.Surface((100, 32))
IMAGE_NORMAL.fill(pygame.Color('SlateGray'))
IMAGE_HOVER = pygame.Surface((100, 32))
IMAGE_HOVER.fill(pygame.Color('lightskyblue'))
IMAGE_DOWN = pygame.Surface((100, 32))
IMAGE_DOWN.fill(pygame.Color('aquamarine1'))
play_image = pygame.transform.scale(pygame.image.load("arcade_assets/music2.png"),((50,50)))
stop_image = pygame.transform.scale(pygame.image.load("arcade_assets/no_music2.png"),((50,50)))

IMAGE_SPACE = pygame.Surface((100, 32))
IMAGE_SPACE.fill(pygame.Color(33, 47, 61))


IMAGE_FLAPPY = pygame.Surface((100, 32))
IMAGE_FLAPPY.fill(pygame.Color(34,139,34))

IMAGE_HOVER_FLAPPY = pygame.transform.scale(pygame.image.load("Flappy/Graphics/background_transparent.png"),((90,220)))

IMAGE_HOVER_SPACE = pygame.transform.scale(pygame.image.load("Space/graphics/background.jpg"),((90,220)))

# Button is a sprite subclass, that means it can be added to a sprite group.
# You can draw and update all sprites in a group by
# calling `group.update()` and `group.draw(screen)`.
def run_interface():
    class Button(pygame
                 .sprite.Sprite):
    
        def __init__(self, x, y, width, height, callback,
                     font=FONT, text='', text_color=(0, 0, 0),
                     image_normal=IMAGE_NORMAL, image_hover=IMAGE_HOVER,
                     image_down=IMAGE_DOWN):
            super().__init__()
            # Scale the images to the desired size (doesn't modify the originals).
            self.image_normal = pygame.transform.scale(image_normal, (width, height))
            self.image_hover = pygame.transform.scale(image_hover, (width, height))
            self.image_down = pygame.transform.scale(image_down, (width, height))
    
            self.image = self.image_normal  # The currently active image.
            self.rect = self.image.get_rect(topleft=(x, y))
            # To center the text rect.
            image_center = self.image.get_rect().center
            text_surf = font.render(text, True, text_color)
            text_rect = text_surf.get_rect(center=image_center)
            # Blit the text onto the images.
            for image in (self.image_normal, self.image_hover, self.image_down):
                image.blit(text_surf, text_rect)
    
            # This function will be called when the button gets pressed.
            self.callback = callback
            self.button_down = False
    
        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.image = self.image_down
                    self.button_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                # If the rect collides with the mouse pos.
                if self.rect.collidepoint(event.pos) and self.button_down:
                    self.callback()  # Call the function.
                    self.image = self.image_hover
                self.button_down = False
            elif event.type == pygame.MOUSEMOTION:
                collided = self.rect.collidepoint(event.pos)
                if collided and not self.button_down:
                    self.image = self.image_hover
                elif not collided:
                    self.image = self.image_normal
    
    
    class Game:
    
        def __init__(self, screen):
            self.done = False
            self.clock = pygame.time.Clock()
            self.screen = screen
            # Contains all sprites. Also put the button sprites into a
            # separate group in your own game.
            self.all_sprites = pygame.sprite.Group()
            self.number = 0
            # Create the button instances. You can pass your own images here.
            
            
            # sound on and sound off
            self.pause_button = Button(
                800, 200, 50, 50, self.pause,
                FONT, '', (255, 255, 255),
                stop_image,stop_image,stop_image)
            
            self.play_button = Button(
                800, 125, 50, 50, self.play,
                FONT, '', (255, 255, 255),
                play_image,play_image,play_image)
            
            
            
            
            # games
            
            self.flappy_button = Button(
                40, 200, 220, 90, self.run_flappy,
                FONT, 'Flappy Penguin', (255, 255, 255),
                IMAGE_FLAPPY, IMAGE_HOVER_FLAPPY, IMAGE_HOVER_FLAPPY)
            
            self.space_button = Button(
                40, 350, 220, 90, self.run_space,
                FONT, 'Space Invader', (255, 255, 255),
                IMAGE_SPACE, IMAGE_HOVER_SPACE, IMAGE_HOVER_SPACE)
            
            
            
            self.pong_button = Button(
                40, 500, 220, 90, self.ping_pong,
                FONT, 'Ping Pong', (255, 255, 255),
                )
            
            
            # jukebox
            self.juke_button = Button(
                40, 650, 220, 90, self.juke_box,
                FONT, 'Juke Box', (255, 255, 255),
                )
            
            
            
            
            
            # If you don't pass images, the default images will be used.
            self.quit_button = Button(
                320, 240, 170, 65, self.quit_game,
                FONT, 'Quit', (255, 255, 255))
            # Add the button sprites to the sprite group.
            self.all_sprites.add(self.flappy_button,self.space_button,self.pause_button,self.play_button,self.pong_button,self.juke_button)
            
        
        def pause(self):
                        
                pygame.mixer.music.pause()
                
        def play(self):
                pygame.mixer.music.play()
           
        def ping_pong(self):
            pygame.quit()
            os.system('ping_pong.py')
            
            
        def juke_box(self):
           
            pygame.quit()
            os.system('juke_box.py')        
            
            
            
        
        def run_space(self):
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Space/space_music.mp3')
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play(-1)
            Space_Invader.main_menu()
            pygame.mixer.music.stop()
    
        def quit_game(self):
            """Callback method to quit the game."""
            self.done = True
    
        def run_flappy(self):
            pygame.mixer.music.stop()
            flappy.main_game()
    
        def run(self):
            while not self.done:
                self.dt = self.clock.tick(30) / 1000
                self.handle_events()
                self.run_logic()
                self.draw()
    
        def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                for button in self.all_sprites:
                    button.handle_event(event)
    
        def run_logic(self):
            self.all_sprites.update(self.dt)
    
        def draw(self):
            self.screen.fill((30, 30, 30))
            screen.blit(BG,(0,0)) 
            
            
            my_font = pygame.font.Font("Space/INVASION2000.ttf", 57)

            info_label = my_font.render("Welcome  To  The  Arcade" ,True, (255,255,255))
            
            copy_right_font= pygame.font.Font("Space/Bitter-Bold.otf",15)
            copy_right_label =  copy_right_font.render("© 2020 Armaan And Girik" ,True, (255,255,255))
          
            screen.blit(info_label, (40,50))
            screen.blit(copy_right_label,(350,860))
            
            
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
 
    
    if __name__ == '__main__':
        pygame.init()
        Game(screen).run()
        pygame.quit()
        


run_interface()





