import pygame as pg
import sys, random, os

pg.init()

#controls the time of the game 
clock = pg.time.Clock()

#setting the dimensions of the main window 
screen_width = 1080
screen_height = 660

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Ping Pong')


#this variable controls the game loop
game_active = False

#OBJECT RECTANGLES

#ball rectangle
ball = pg.Rect(screen_width/2 - 15, screen_height/2 -15, 30, 30)

#player rectangle
player = pg.Rect(screen_width - 15, screen_height/2 - 65, 10, 130)

#opponent recatngle
opponent = pg.Rect(5, screen_height/2 - 65, 10, 130)

#colors for board 
#Put it in a list so that can be call anytime
#the elements are further listed so can be called by slicing 
colors = [[(69, 69, 69), (201, 118, 0)], [(33, 33, 33), (6, 175, 201)]]

#background color
bg_color = colors[1][0]

#color for players, opponent, center line, ball 
game_color = colors[1][1]

#color for start menu text, winner
winner_color = (76, 209, 21)

#game counter
number_of_games = 0

#speed variables

#movement variables for ball
ball_speed_x = 3 * random.choice((1, -1)) 
ball_speed_y = 3 * random.choice((1, -1))

#controls the level by default it should be 0, it increases in the function
ball_level = 0

#movement vairable for player 
player_speed = 0 #by default zero so that if no key is pressed it won't move

#moving opponent rectangle
opponent_speed = 10

#this variable changes the reflex of the oppenent's movement corresponding to the ball
#by changing this numer we change how powerful the opponent is 
opponent_reflexes = 3


#TEXT VARIABLES 
#score
player_score = 0
opponent_score = 0

#font
game_font = pg.font.Font('ping_pong/font.ttf', 32) #for printing everything
start_font = pg.font.Font('ping_pong/font.ttf', 50) #for printing all start screen variales 
main_menu_font = pg.font.Font('ping_pong/font.ttf',35)
#This variable is to check where the ball ends when the game is over
the_end_of_ball = None

#this func checks where the ball ended and prints the winner 
def winner_blitter(ball_locator):

    if ball_locator == 'left':
        win_text = start_font.render('You win!!', False, winner_color)
        screen.blit(win_text, (435, 300))
    
    if ball_locator == 'right':
        win_text = start_font.render('Opponent wins!!', False, colors[0][1])
        screen.blit(win_text, (350, 300))
    
    if ball_locator == None:
        pass
        
    #reseting the ball to the center 
def ball_reset():
    
    global ball_speed_x, ball_speed_y, game_active
    
    ball.center = (screen_width/2, screen_height/2)
    
    ball_speed_x *= random.choice((1, -1))
    ball_speed_y *= random.choice((1, -1))
    
    #changing ball directions if it touches boundries
def ball_movement():
    #calling scores
    global player_score, opponent_score
    
    #calling global variables 
    global ball_speed_y, ball_speed_x, ball_level, game_active, the_end_of_ball
    
    #moving the ball in the screen surface by adding speed variables
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    
    #gradually increases the speed of the ball as the game progresses
    ball_speed_x += ball_level
    ball_speed_y += ball_level
    
    #if ball touches top or bottom reverse its direction
    if (ball.top <= 0) or (ball.bottom >= screen_height):
        
        ball_speed_y *= -1
    
    #if ball touches left or right of the window, Finishes the game
    if (ball.left <= 0):        
        
        ball_reset() #resets the ball
        the_end_of_ball = 'left'
        game_active = False #ends the game
    
                
    if (ball.right >= screen_width):
    
        ball_reset() #resets the ball
        the_end_of_ball = 'right'        
        game_active = False #restarts the game 
        
    #checking if ball collides with the rectangle of the player or the opponent
    if ball.colliderect(player) and ball_speed_x > 0:
        
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1	
        
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        
        player_score += 1
    
    if ball.colliderect(opponent) and ball_speed_x < 0:
        
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1	
        
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
        
        opponent_score += 1
        
        #controls the amount of speed of the ball
        ball_level += 0.001
        
    
    #player movement
def player_movement():
    global player_speed
    #moving the player up and down
    player.y += player_speed
    
    #if player touches boundries we don't let it go out of the screen
    if (player.top <= 0):
        player.top = 1 #this means that the player will stay at top of screen
        player_speed = 0
            
    if (player.bottom >= screen_height): 
        player.bottom = screen_height #this means that the player will stay at bottom of screen
        player_speed = 0
    
    #opponent movement
def opponent_movement():
    
    global opponent_speed, opponent_reflexes, opponent_score
    
    #if opponent is below the ball, move it up
    if opponent.top < ball.y:
        opponent.top += (opponent_speed + opponent_reflexes)
    
    #if opponent is anove the ball, move it down
    if opponent.bottom > ball.y:
        opponent.bottom -= (opponent_speed - opponent_reflexes)
    
    #if opponent touches boundries we don't let it go out of the screen
    if (opponent.top <= 0):
        opponent.top = 0 #this means that the opponent will stay at top of screen
          
    if (opponent.bottom >= screen_height): 
        opponent.bottom = screen_height #this means that the oppopnent will stay at bottom of screen
    
    #increasing the power of the opponent as the ball speed also increass so that the opponent dosen't loses
    if opponent_score == 14:
        opponent_reflexes =  5
    
    
def restart_game(game, screen_placer):

    global ball_speed_y, ball_speed_x, player_score, opponent_score, ball_level, number_of_games
    
    #this loop checks if number of games is greater than one, then replaces the green color of start game to oragne color for restart game
    if number_of_games >= 1:
        color = colors[0][1]
    else:
        color = winner_color
    
    #prinitng restart on the game
    start_game_text = start_font.render(f'Click Mouse to {game} Game', False, color)
    screen.blit(start_game_text, (screen_placer, 370))
    
    main_menu_text = main_menu_font.render('Press M for main menu', False, (255,255,255))
    screen.blit(main_menu_text, (screen_placer+125, 450))
    
    #resetting the score
    player_score = 0
    opponent_score = 0
    
    #resetting the ball difficulty
    ball_level = 0
    
    #resetting the orignal ball speed
    ball_speed_x = 3 * random.choice((1, -1)) 
    ball_speed_y = 3 * random.choice((1, -1))


#MAIN GAME LOOP
while True:

#handling the user input
#this for loop checks all user interactions 
    for event in pg.event.get():
        
        #checking if the user preeses the cross above the screen
        if event.type == pg.QUIT:
            
            pg.quit()
            sys.exit()
        
        #to check if the user has clicked the mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            #on clciking the mouse button, it starts the game
            game_active = True
            
            #increasing the number of games played
            number_of_games += 1
                   
        
        #checking if the user presses a key
        if event.type == pg.KEYDOWN:
    
            if event.key == pg.K_DOWN:
                player_speed +=7
            
            
            if event.key == pg.K_UP:
                player_speed -=7
                
            if event.key == pg.K_m:
                    
                pg.quit()
                os.system('interface.py')
        
        #checking if the user unpresses a key
        if event.type == pg.KEYUP:
            
            if event.key == pg.K_DOWN:
                player_speed = 0
            
            if event.key == pg.K_UP:
                player_speed = 0   
               
            
    
    #VISUALS
    #filling the background with grey color
    screen.fill(bg_color)
    
    #drawing the player, opponent rectangles
    pg.draw.rect(screen, game_color, player)
    pg.draw.rect(screen, game_color, opponent)
    
    #drawing the ellipse ball
    pg.draw.ellipse(screen, game_color, ball)
    
    #center line 
    pg.draw.aaline(screen, game_color, (screen_width/2,0), (screen_width/2,screen_height))
    
    #printing the player score
    player_text = game_font.render(f'Score: {player_score}', False, game_color)
    screen.blit(player_text, (5, 5))
    
    #creating a variable for player and opponent text and placing it on the screen
    #player_text = game_font.render(f'{player_score}', False, game_color)
    #screen.blit(player_text, (550, 330))
    
    #opponent_text = game_font.render(f'{opponent_score}', False, game_color)
    #screen.blit(opponent_text, (500, 330))
    
    #activating the game
    if game_active:
        
        #if game is active the all, player and opponent will start moving
        ball_movement()
        
        player_movement()
        
        opponent_movement()

    else:
        
        #this will show the winner text, start/restart text 
        #ball, player and opponent will not be moving
        if not game_active:
            
            #if user restarts game after playing one more game it shows restart
            if number_of_games >= 1:
                restart_game('Restart', 210)
                winner_blitter(the_end_of_ball) #prints the winner 
                
            #to start game we need to click the mouse
            else:
                restart_game('Start', 220)
                                
    #updating the screen
    pg.display.flip()
    clock.tick(120) #controls the framerate of the screen
    
    

        