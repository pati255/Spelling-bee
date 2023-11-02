import pygame
import random
from pygame import mixer  #handles music/anything with sounds or musics
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
pygame.init()
#importing sounds
#global text
global text
dry = pygame.mixer.Sound('dry.wav')
citizen = pygame.mixer.Sound('citizen.wav')
ample = pygame.mixer.Sound('ample.wav')
wrap = pygame.mixer.Sound('wrap.wav')
ghostwriter = pygame.mixer.Sound('ghostwriter.wav')
operation = pygame.mixer.Sound('operation.wav')
pull = pygame.mixer.Sound('pull.wav')
guitar = pygame.mixer.Sound('guitar.wav')
hammer = pygame.mixer.Sound('hammer.wav')
approach = pygame.mixer.Sound('approach.wav')
thanks = pygame.mixer.Sound('thanks.wav')
lot = pygame.mixer.Sound('lot.wav')
ignorant = pygame.mixer.Sound('ignorant.wav')


#puts the words in a list
audio = [dry,citizen,ample,wrap,ghostwriter,operation,pull,guitar,hammer,approach,thanks,lot,ignorant]
#provides a font variable to be used
font= pygame.font.SysFont("Arial",60)
#provides a black colour to be called by the name instead of (0,0,0)
black = (0,0,0)
#variables holding a string this draws a text on a new surface with colours
#these variables are used for the validation of the game
right =  font.render("You are right",1,(255,16,41))
wrong =  font.render("You are wrong",1,(255,16,41))
#another style variable this is for the title of the game
title = font.render("Spelling Bee",1,(225,0,225))
#randomises the list available in a function ready to be called at any time
def playRandom():
        random.choice(audio).play()
        #another function being called to validate if the text written from input box matches the words in the list
        #if thats the case it will print on the surface variable right with dimensions of 100,300
def validate(b,text):
        if b == True:
         if text in words:
          window.blit(right,(100,300))        
         elif text not in words:
          window.blit(wrong,(100,300))
          
        
        
#creates a list
#used a random word generator
words = ["dry" , "citizen","growth","ample","wrap","ghostwriter","operation","pull","guitar","hammer","approach","thanks","lot","ignorant"]
#window for the game this is the resolution that the player sees the game
window = pygame.display.set_mode((500, 400))    
#uploading a little image to make it more user friendly
#https://www.dreamstime.com/cute-honey-bees-border-your-kawaii-design-image138419830
#link above shows the source of where this image was taken from, i do not own any rights to this image
background=pygame.image.load('bees.JPG')

#this provides a title for the menu 
gameTitle=font.render("Spelling Bee",1,(225,0,225))
#this creates a clock for the pygame which helps track time
clock = pygame.time.Clock()
#this creates a rectanble box with these dimensions below which will act as an input box to put in characters
input_box = pygame.Rect(100, 200, 140, 100)
#a function which will focus on the navigation of the main menu
def menu():
        #font and style of the main menu
        fontMenu = pygame.font.SysFont("Arial",16)
        #initalize all the pygame modules
        pygame.init()
        #while loop this will continously loop
        while True:
                #this is the  event queue and this code will get messages and remove them from queue
                for event in pygame.event.get():
                        #quits pygame
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pygame.quit()
                        if event.key == pygame.K_RETURN:
                            main()
                        else:
                                pygame.quit()
                
                         #if user presses space it quits pygame
                             #if user presses enter then they will be sent into main game      

                               
                 #fills window with a pink colour of this inensity red,blue,green           
                window.fill((255, 192, 203))
                #this provides the bee image for the background to make it more user friendly
                window.blit(background,(120,60))
                #variable that draws out a rectangle box filled with colour in these dimensions
                start = pygame.draw.rect(window,((255,255,255)),(260,250,120,30))
                #variable that draws out a rectangle box filled with colour in these dimensions
                ext = pygame.draw.rect(window,((200,0,100)),(80,250,120,30))
                #variable which has string ready to be displayed on the surface with colours
                enter =  fontMenu.render("Press enter to start",1,(20,0,0))
                #another variable that has a string with colours, these are for making it user friendly and practical guidance for the user
                esc =  fontMenu.render("press Space to quit",1,(255,255,255))
                #shows the string on top of the button on surface
                window.blit(enter,(260,250))
                #shows the string on top of the button on sufrace
                window.blit(esc,(80,250))
                #shows the gametitle on the menu screen for the user to know what game it is
                window.blit(gameTitle,(125,0))
                #updates the display of pygame
                pygame.display.update()
                #updates contents of entire display
                pygame.display.flip()
                #gets time in miliseconds
                clock.tick(60)

                
        
        
                 

#another function this is the main structure of the code and project
def main():
        #plays a random audio for the user
        playRandom()
        #empty variable used for storing what the user has inputted into the input box
        text = ''
        #variable which holds a False value
        f=False
        #initalizes pygame moudules
        pygame.init()
        #another loop this time for the main game which will nagivate using keys
        while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.KEYDOWN:
                            #shows the code created for deleting characters written in the input box
                        if event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                                #code showing if press enter the validation occurs to see if the user is right or wrong and if their text matches what they audio said
                        if event.key == pygame.K_RETURN:
                            f = True
                            #repeats whole loop with a new random audio so the user can start another one or if they struggle they can skip and do a new one
                        if event.key == pygame.K_DOWN:
                            main()
                        else:#this is the text that is written and works with the keys and events
                                text += event.unicode
       #this loop has been taken and sourced from https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame/46390412#46390412                         
                #fills display with the same pink colour
                window.fill((255, 192, 203))
                #puts the background picture into the project
                window.blit(background,(120,60))
                #calls for validation on the text that has been entered in the input box 
                validate(f,text)
                # creates a new surface for this variable
                txt_surface = font.render(text, True, (0,0,0))
                 # able to resize the box to the programmers desire
                width = max(300, txt_surface.get_width()+50)
                input_box.w = width
                # puts the variable above on the surface to be seen by user
                window.blit(txt_surface, (input_box.x+10, input_box.y+10))
                # draws a rectangle on the surface where the user can see this is the input box seen on the project when it runs
                pygame.draw.rect(window, (255,255,255), input_box, 2)
                #draws the title variable which has been seen before on the surface display for the user so they know what game they are playing
                window.blit(title,(100,0))
                #updates display
                pygame.display.update()
                #updates display
                pygame.display.flip()
                #gets time in miliseconds
                clock.tick(60)
#calls back on the menu function to show the menu when program starts
menu()



