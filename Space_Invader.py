# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:50:10 2020

@author: hp
"""

# importing the necessities
import pygame
import time
import random
import os
import sys



# initialising pygame

pygame.init()
# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 8, buffer = 20148)
pygame.font.init()



# creating pygame window
HEIGHT,WIDTH=900,900
SCREEN=pygame.display.set_mode((HEIGHT,WIDTH),)
pygame.display.set_caption("Space Invader")



# loading all the graphics

# Enemy AI
EVIL_RED = pygame.image.load("Space/graphics/evil_red2.png")
EVIL_GREEN = pygame.image.load("Space/graphics/evil_green2.png")
EVIL_PURPLE = pygame.image.load("Space/graphics/evil_purple2.png")
EVIL_GOLD = pygame.image.load("Space/graphics/evil_special2.png")


# Lasers
RED_LASER = pygame.image.load("Space/graphics/red_laser.png")
GREEN_LASER = pygame.image.load(os.path.join("Space/graphics", "green_laser.png"))
PURPLE_LASER = pygame.image.load(os.path.join("Space/graphics", "purple_laser.png"))
GOLD_LASER = pygame.image.load(os.path.join("Space/graphics", "special_laser.png"))
MY_LASER = pygame.image.load(os.path.join("Space/graphics", "blue_laser.png"))


# Player Spaceplayer
MY_SPACESHIP = pygame.image.load(os.path.join("Space/graphics", "spaceship2.png"))


# Background and scaling (cool boy)
BG = pygame.transform.scale(pygame.image.load(os.path.join("Space/graphics", "background.png")),(HEIGHT,WIDTH))

# general laser class
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)



# general player class
class Ship:
    COOLDOWN = 30
    
    def __init__(self,x,y,health=100):
        
        self.x = x
        self.y = y
        self.health = health
        self.ship_image = None
        self.laser_image = None
        self.lasers = []
        self.cool_down_counter = 0
        

    def draw(self, window):
        window.blit(self.ship_image, (self.x,self.y))
        for laser in self.lasers:
            laser.draw(window)
        
        
        
    def get_width(self):
        return self.ship_image.get_width()
        
    def get_height(self):
        return self.ship_image.get_height()  
    
    
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter +=1
    
    
    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x+12, self.y+10, self.laser_image)
            self.lasers.append(laser)
            self.cool_down_counter = 1
    
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    

class Player(Ship):
    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_image = MY_SPACESHIP
        self.laser_image = MY_LASER
        self.mask= pygame.mask.from_surface(self.ship_image)
        self.max_health = health
        
    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
    
    def draw(self,window):
        super().draw(window)
        self.health_bar(window)
    
                            
    def health_bar(self, window):
         pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width(), 10))
         pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_image.get_height() + 10, self.ship_image.get_width() * (self.health/self.max_health), 10))

        

class Enemy(Ship):
    COLOR_MAP = {
                    "red":(EVIL_RED,RED_LASER),
                    "green":(EVIL_GREEN,GREEN_LASER),
                    "purple":(EVIL_PURPLE,PURPLE_LASER),
                    "gold":(EVIL_GOLD,GOLD_LASER)
        
                }
    
    
    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_image,self.laser_image = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_image)
    
    def move(self,vel):
        self.y +=vel



def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None



# Main Loop

def main():
    running = True
    FPS=60
    level = 0
    lives = 5
    main_font = pygame.font.SysFont("comicsans", 45)
    lost_font = pygame.font.Font('Space/game_over.ttf', 175)
    
    player= Player(415,750)
    
    enemies=[]
    wave_length = 5
    enemy_vel = 1
    laser_vel = -4
    player_vel = 5
    
    clock=pygame.time.Clock()
    
    lost = False
    lost_count = 0
    
    
     # draws every event on the display
     
    def redraw_window():
        SCREEN.blit(BG,(0,0))
        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        
        SCREEN.blit(lives_label, (10,10))
        SCREEN.blit(level_label, (WIDTH - level_label.get_width()-10,10))
        
        
        # draws enemies on the screen
        for enemy in enemies:
            enemy.draw(SCREEN)
       
        player.draw(SCREEN)
        
        # game over animation
        if lost:
            lost_label = lost_font.render("GAME OVER!", 1, (255,140,0))
            SCREEN.blit(lost_label,(WIDTH/2 - lost_label.get_width()/2, 350))
            
        pygame.display.update()
    

    while running:
        clock.tick(FPS)
        
        redraw_window()
        
        if lives <=0 or player.health <= 0:
            lost = True
            lost_count += 1
            
        if lost:
            if lost_count > FPS*3:
               running = False
            else:
               continue
        
        # checks for losing condition
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1300,-100), random.choice(["red","green","purple"]))
                enemies.append(enemy)
                
        # checks if the close button has been pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # Assigning keys
        keys = pygame.key.get_pressed()   
        
        # LEFT 
        if keys[pygame.K_a] and player.x - player_vel>0:
            player.x-=player_vel
        elif keys[pygame.K_LEFT] and player.x - player_vel>0:
            player.x-=player_vel
            
        # RIGHT
        if keys[pygame.K_d] and player.x + player_vel<WIDTH-83:
            player.x+=player_vel
        elif keys[pygame.K_RIGHT] and player.x + player_vel<WIDTH-83:
            player.x+=player_vel
            
        # UP
        if keys[pygame.K_w] and player.y - player_vel>0:
            player.y-=player_vel
        elif keys[pygame.K_UP] and player.y - player_vel>0:
            player.y-=player_vel
        
        # DOWN
        if keys[pygame.K_s] and player.y +  player_vel<HEIGHT-100:
            player.y+=player_vel
        elif keys[pygame.K_DOWN] and player.y + player_vel<HEIGHT -100:
            player.y+=player_vel    
            
        # shoot // SPACEBAR
        if keys[pygame.K_SPACE]:
            player.shoot()

            
        for enemy in enemies:
            enemy.move(enemy_vel)
            enemy.move_lasers(-laser_vel, player)
            
            if random.randrange(0,120) == 1:
                
                enemy.shoot()
            
            if collide(enemy, player):
              player.health -= 10
              enemies.remove(enemy)
              
            
            
            
            elif enemy.y + enemy.get_height() > HEIGHT:
               lives -= 1
               enemies.remove(enemy)
            
          
        
        player.move_lasers(laser_vel, enemies)

    
# main menu after losing 
def main_menu():
    info_font = pygame.font.Font("Space/prstart.ttf", 20)
    title_font = pygame.font.Font("Space/INVASION2000.ttf", 70)
    run = True
    while run:
        SCREEN.blit(BG, (0,0))
        title_label = title_font.render("Start Game", 1, (0,255,0))
        info_label = info_font.render("(Press Enter to begin)", 1, (255,255,255))
        menu_label = info_font.render("(Press M for main menu)", 1, (255,255,255))
        
        SCREEN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        SCREEN.blit(info_label, (WIDTH/2 - title_label.get_width()/2 + 10, 450))
        SCREEN.blit(menu_label, (WIDTH/2 - title_label.get_width()/2 + 8, 520))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    
                    pygame.quit()
                    os.system('the_arcade.py')
                    
            
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    main()
    pygame.quit()
   
# main_menu()
    
  
    
  
