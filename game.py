import pygame
import pygame.locals
from player import newPlayer

class GenerateMainWorld:
    def generateMainWindow(self):
        pygame.display.set_caption('weerwolven')
        # give size of world
        worldX = 1000
        worldY = 650
        world = pygame.display.set_mode([worldX, worldY])
        # generate day Background
        background_image_day = pygame.image.load("images/background_day.jpg")
        # generate night Background
        background_image_night= pygame.image.load("images/backgroundNight.jpg")
        background_colour = ('#4e5452')

        pygame.init()
        pygame.display.set_caption("weerwolven")
        world.fill(background_colour)
        pygame.init()

        self.drawWorld(world, background_image_day, background_image_night)
    def houses(self,world):
        houseImage = pygame.image.load('images/house1.png')
        positionHouses = [
            [360, 220],
            [100, 250], [600, 250],
            [100, 450], [700, 450]
        ]

        for i in positionHouses:
            for y in positionHouses:
                world.blit(houseImage, (i, y))

    def currentGuessCount(self,numberCount):
        return numberCount
    def drawWorld(self,world,background_day,background_night):
        main = True
        # generatePlayer

        currentPlayer = newPlayer()
        currentPlayer_list = pygame.sprite.Group()
        currentPlayer_list.add(currentPlayer)
        #generate a clock
        clock = pygame.time.Clock()
        #generate a delta time
        deltaTime=0
        timeElapsed=0

        while main:

            deltaTime=clock.tick()*.001
            timeElapsed+=deltaTime

            #time Elapsed is time given before change
            if timeElapsed<10:
                world.blit(background_day, (0, 0))
                self.houses(world)
                currentPlayer.move()
                currentPlayer.updatePosition()
                currentPlayer.changeView()
                currentPlayer_list.draw(world)
                pygame.display.flip()
            elif timeElapsed<20:

                world.blit(background_night, (0, 0))
                self.houses(world)

                font = pygame.font.SysFont('Arial', 32)
                text = " the sun is going under, time to guess: "
                weerwolvenNaam="Anna"
                guessed = []
                numberOfPeople = 5
                countOfGuesses = 0

                isSame = False
                running = True
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()

                        elif event.type == pygame.KEYDOWN:
                            if event.key == 13:
                                currentBet = text[text.find(':') + 1:len(text)]
                                currentBet = currentBet.strip()

                                if len(guessed) == 0:
                                    if currentBet == weerwolvenNaam:
                                        text = "you guessed it"
                                    else:
                                        text = "try again: "
                                        guessed.append(currentBet)

                                        countOfGuesses += 1
                                        self.currentGuessCount(countOfGuesses)
                                else:
                                    if currentBet == weerwolvenNaam:
                                        text = "you guessed it"
                                    elif countOfGuesses == numberOfPeople:
                                        text = "you are dead"
                                        main = False
                                    else:
                                        for guessedAnswers in guessed:
                                            if guessedAnswers == currentBet:
                                                isSame = True
                                        if isSame == True:
                                            text = "wrong value, try again: "
                                        else:
                                            text = "try again: "

                                            guessed.append(currentBet)
                                            countOfGuesses += 1
                                            self.currentGuessCount(countOfGuesses)

                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode
                            world.blit(background_night, (0, 0))
                            self.houses(world)

                        # puts text on screen
                        text_surface = font.render(text, True, (255, 255, 255))
                        world.blit(text_surface, (0, 0))

                        pygame.display.flip()
            else:
                timeElapsed=0
