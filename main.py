import pygame
import sys
import random
import time
pygame.font.init()

# Target-> find pink donut

# GAME CONSTANTS
HEIGHT,WIDTH=600,1000

# FONT
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.SysFont("comicsans",19)
font2 = pygame.font.SysFont("comicsans",17)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# GAME VARIABLES
run=True

score=0


start_time = time.time()
# setting up  screen

s=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SingleDonut")

# setting up game instructions
def instructions(screen):
    instruction_text = font2.render(f'Only Click on the PINK Donut (SPACE to PAUSE)', True, "red")
    instruction_textRect = instruction_text.get_rect()
    instruction_textRect.center = (600, 40)

    credit_text = font2.render(f'by Souhardya Saha', True, "purple")
    credit_textRect = credit_text.get_rect()
    credit_textRect.center = (100, 10)
    screen.blit(credit_text, credit_textRect)
    screen.blit(instruction_text, instruction_textRect)




    pass

# MAKIGN DONUTS

# importing donut pics
donut_pics=[]
for i in range(1,7):
    p=pygame.transform.scale(pygame.image.load(f"d{i}.png"),(45,45))
    donut_pics.append(p)
print(len(donut_pics))

donuts=[]
def make_donuts_location():
    global donuts
    for i in range(15):
        
        if i==7:
            x=random.randrange(30,980,25)
            y=random.randrange(30,580,25)
            colour_num=5
        else:
            x=random.randrange(30,980,25)
            y=random.randrange(30,580,25)
            colour_num=random.randint(0,4)

        donuts.append((pygame.Rect(x,y,40,40),colour_num))
make_donuts_location()
print(donuts)
print(donut_pics)


# MAIN GAME LOOP
while(run):
    s.fill("pink")
    instructions(s)
  
    # score setup
    score_text = font1.render(f'SCORE: {int(score)}', True, "brown")
    score_textRect = score_text.get_rect()
    score_textRect.center = (50, 40)
    s.blit(score_text, score_textRect)

    # time ahead
    end_time = time.time()
    elapsed_time = end_time - start_time
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        # GAME PAUSING CODE
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                paused=True
                
                while(paused):
                    # what to display when game is paused
                    text = font.render('Game Paused !', True, green)
                    textRect = text.get_rect()
                    textRect.center = (WIDTH // 2, HEIGHT // 2)
                    s.blit(text, textRect)
                    
                    for event in pygame.event.get():
                        if event.type==pygame.KEYDOWN:
                            if event.key==pygame.K_SPACE:
                                paused=False
                    pygame.display.flip()
                    continue

    if (pygame.mouse.get_pressed()[0]):
      
        for i in donuts:
            donut=i[0]
            if donut.left<pygame.mouse.get_pos()[0]<donut.right and donut.top<pygame.mouse.get_pos()[1]<donut.bottom and i[1]==5:# last condition is to check pink colour
                print("CAUGHT")
                score+=0.03
                
            # game ending condition
            if donut.left<pygame.mouse.get_pos()[0]<donut.right and donut.top<pygame.mouse.get_pos()[1]<donut.bottom and i[1]!=5: 
                run=False
                continue
            
    if int(elapsed_time)%2==0:
        donuts.clear()
        
        make_donuts_location()
    print(int(score))
    for i in donuts:
        s.blit(donut_pics[i[1]],i[0])
  
    pygame.display.update()

# game over text and quitting
text1 = font.render('Game Over !! ', True, 'black')
textRect1 = text1.get_rect()
textRect1.center = (WIDTH // 2, HEIGHT // 2)
s.blit(text1,textRect1)

pygame.display.flip()
pygame.time.delay(2500)
sys.exit()