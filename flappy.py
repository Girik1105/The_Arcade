# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:57:16 2020

@author: girik
"""

import pygame, sys, os, random


def main_game():
    
    pygame.init()
    
    
    #font for the game
    game_font = pygame.font.Font('Flappy/font/04B_19.TTF', 20)
    
    
    #screen size
    screen = pygame.display.set_mode((470, 650), )
    pygame.display.set_caption("Flappy Penguin")
    
    #clock for framerate
    clock = pygame.time.Clock()
    
    #importing background
    backgrounds = ['Flappy/Graphics/backgrounds/1.png', 'Flappy/Graphics/backgrounds/2.png', 'Flappy/Graphics/backgrounds/3.png', 'Flappy/Graphics/backgrounds/4.png']
    background_display = random.choice(backgrounds)
    
    background = pygame.image.load(background_display).convert()
    background = pygame.transform.scale(background, (470,650))
    
    #importing base
    base = pygame.image.load('Flappy/Graphics/base.png').convert()
    base = pygame.transform.scale(base, (470,150))
    
    
    #Creting bird with rectangle in pygame
    bird = pygame.image.load('Flappy/Graphics/pen.png')
    bird = pygame.transform.scale(bird, (43, 37))
    bird_rect = bird.get_rect(center = (100, 250))
    
    
    #bird rotator
    def rotate_bird(bird_rotate):
        new_bird = pygame.transform.rotozoom(bird_rotate, 180.0, 1.0)
        return new_bird
    
    #pipes
    
    pipe_surface = pygame.image.load('Flappy/Graphics/pole_lower.png')
    pipe_surface = pygame.transform.scale(pipe_surface, (150, 277))
    
    
    pipe_list = []
    
    PIPE_SPAWNER = pygame.USEREVENT
    pygame.time.set_timer(PIPE_SPAWNER, 1500) #controls the time for spawning pipes
    
    
    pipe_height = [270, 325, 425]
    
    def pipe_creator():
        random_pipe_position = random.choice(pipe_height)
        bottom_new_pipe = pipe_surface.get_rect(midtop = (470, random_pipe_position))
        top_pipe = pipe_surface.get_rect(midtop = (470, random_pipe_position - 500))
        return bottom_new_pipe, top_pipe
    
    def pipe_spacer(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
    
        return pipes
    
    def draw_pipes(pipes):
        for pipe in pipes:
            if pipe.bottom >= 470:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)
    
    
    #COLLISION CHECKER
    def check_collision(pipes):

        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                pygame.mixer.music.load('Flappy/hit.mp3')
                pygame.mixer.music.play()
                

                return False
    
        if bird_rect.top <= -50 or bird_rect.bottom >= 520:
            pygame.mixer.music.load('Flappy/hit.mp3')
            pygame.mixer.music.play()
            
    
            return False
    
        return True
    
    def falling_bird(gravity, bird_movement):
        gravity = 0.0001 # controls how much the bird will fall
        bird_movement = 0
        
        
        return gravity, bird_movement

    def game_over():
        press_spacebar = game_font.render('Press spacebar to start', True, (255,255,255))
        press_spacebar_rect = press_spacebar.get_rect(center = (225, 315))
        screen.blit(press_spacebar, press_spacebar_rect)
        
        press_m = game_font.render('Press M for Main menu', True, (255,255,255))
        press_m_rect = press_m.get_rect(center = (225, 345))
        screen.blit(press_m, press_m_rect)
    
    
    
    #GAME VARIABLES
    gravity = 0.20 # controls how much the bird will fall
    bird_movement = 0
    
    game_active = False
    
    score = 0
    
    number_of_games = 0
    
    file = open('Flappy/score.txt', 'r')
    
    high_score = int(file.read())
    
    file.close()
    
    
    #draws the base
    def draw_base():
        screen.blit(base,(base_position, 520))
        screen.blit(base,(base_position + 470, 520))
    
    
    base_position = 0
    
    
    
    #font for the score
    def score_surface(game_state):
    
        if game_state == 'main_game':
    
            score_surface = game_font.render('score: '+str(int(score)), True, (255,255,255))
            score_rect = score_surface.get_rect(center = (60, 30))
            screen.blit(score_surface, score_rect)
            
            
    
        if game_state == 'game_over':
    
            score_surface = game_font.render('score: '+str(int(score)), True, (255,255,255))
            score_rect = score_surface.get_rect(center = (60, 30))
            screen.blit(score_surface, score_rect)
    
            high_score_surface = game_font.render('Highscore: '+str(int(high_score)), True, (255,255,255))
            high_score_rect = score_surface.get_rect(center = (60, 65))
            screen.blit(high_score_surface, high_score_rect)
    
    
    def update_score(score, high_score):
        if score > high_score:
            high_score = score
        return high_score
    
    
    
    game_over_surface = pygame.image.load('Flappy/Graphics/start_game.png')
    game_over_surface = pygame.transform.scale(game_over_surface, (450, 125))
    game_over_surface_rect= game_over_surface.get_rect(center = (235, 225))
    
    
    
    
    #main game loop
    while True:
    
        for event in pygame.event.get():
    
            #quits game
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            if event.type == pygame.KEYDOWN: #checks if any of the button is pressed
    
                if event.key == pygame.K_SPACE and game_active == True:
                    pygame.mixer.music.load('Flappy/wing.mp3')
                    pygame.mixer.music.set_volume(0.1)
                    pygame.mixer.music.play()
                    bird_movement = 0
                    bird_movement -= 7 #gives bird jump (change to lower or increase the senstivity)
    
    
                if event.key == pygame.K_SPACE and game_active == False:
    
                    game_active = True
    
                    pipe_list.clear()
                    bird_rect.center = (100, 150)
                    bird_movement = 0
    
                    score = 0
                
                if event.key == pygame.K_m:
                    pygame.quit()
                    # sys.exit()
                    os.system('the_arcade.py 1')
                    
                    
    
            #pipe spawner
            if event.type == PIPE_SPAWNER:
                pipe_list.extend(pipe_creator())
                
    
        #background
        screen.blit(background,(0,0))
    
    
        #bird movement
        bird_movement += gravity
    
        rotate_bird(bird)
    
        bird_rect.centery += bird_movement
    
        if game_active:
    
            #bird
            screen.blit(bird, bird_rect)
    
            #collision checker
            game_active = check_collision(pipe_list)

            if not check_collision(pipe_list) :
                number_of_games += 1
                
                
                
    
            #pipes
            pipe_list = pipe_spacer(pipe_list)
            draw_pipes(pipe_list)
    
            score_surface('main_game')
            score += 0.006
            
    
        else:
            
            
            if number_of_games >= 1:
    
                falling_bird(gravity, bird_movement)
                screen.blit(bird, bird_rect)
            
            game_over()
    
            #game over image
            screen.blit(game_over_surface, game_over_surface_rect)



            #highscore
            high_score = update_score(score, high_score)
    
            #score
            score_surface('game_over')
    
    
        #floor
        base_position -= 1
    
        #base
        draw_base()
    
        #resets base so that it looks like a continues animation
        if base_position <= -470:
            base_position = 0
    
    
        pygame.display.update()
    
        clock.tick(120)  #Controls Framerate
    
        file = open('Flappy/score.txt', 'w')
        file.write(str(int(high_score)))
        file.close()

