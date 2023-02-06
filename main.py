import pygame,time
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode([800, 800])

font=pygame.font.SysFont('Arial',32)
text="try a guess: "


weerwolven=[
    "peter",
    "jan",
    "jos",
    "Aaliyah"
]
weerwolvenNaam=weerwolven[random.randrange(0,len(weerwolven))]
print(weerwolvenNaam)
guessed=[]

numberOfPeople=len(weerwolven)
countOfGuesses=0
isSame=False
running=True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()

        elif event.type ==pygame.KEYDOWN:
            if event.key==13:
                currentBet=text[text.find(':')+1:len(text)]
                currentBet=currentBet.strip()
                if len(guessed)==0:
                    if currentBet==weerwolvenNaam:
                        text="you guessed it"
                    else:
                        text="try again: "
                        guessed.append(currentBet)
                        countOfGuesses+=1
                else:
                    if currentBet==weerwolvenNaam:
                       text="you guessed it"
                    elif countOfGuesses==numberOfPeople:
                        text="you are dead"
                    else:
                        for guessedAnswers in guessed:
                            if guessedAnswers==currentBet:
                                isSame=True
                        if isSame==True:
                            text="wrong value, try again: "
                        else:
                            text="try again: "
                            guessed.append(currentBet)
                        countOfGuesses += 1
            elif event.key==pygame.K_BACKSPACE:
                text=text[:-1]
            else:
                text+=event.unicode

        screen.fill((0, 0, 0))
        #puts text on screen
        text_surface=font.render(text,True,(255,255,255))
        screen.blit(text_surface,(0,0))

        pygame.display.flip()
        clock.tick(60)

#extra code
clock=pygame.time.Clock()
deltaTime = 0
timeElapsed = 0
running=True
while running:
    deltaTime = clock.tick(60)
    timeElapsed+=deltaTime/1000

    print(timeElapsed)