import pygame
import pygame.locals
class houseDesign:
    def set_houseNumber(self, houseNumber):
        self.houseNumber = houseNumber

    def get_houseNumber(self):
        return self.houseNumber

    def generateWindow(self):
        pygame.display.set_caption('weerwolven')

        numberOfHouse = self.get_houseNumber()
        worldX = 1200
        worldY = 600
        color = (0, 0, 0)
        colorText = (255, 255, 255)

        newWorld = pygame.display.set_mode([worldX, worldY])

        background_color = ('#072AD9')
        houseBackgroundArray = [
            ["images/insideHouse/minimalist.jpg"],
            ["images/insideHouse/cozy.jpg"],
            ["images/insideHouse/modern.jpg"],
            ["images/insideHouse/plants.jpg"],
            ["images/insideHouse/special.jpg"]
        ]

        #print(str(numberOfHouse))
        for i in range(5):
            if i == numberOfHouse:
                background_image = ''.join(houseBackgroundArray[i])
                houseBackground = pygame.image.load(background_image)
        pygame.init()

        running = True
        smallfont = pygame.font.SysFont('Arial', 35)

        text = smallfont.render('quit', True, colorText)

        while running:

            newWorld.fill(background_color)
            newWorld.blit(houseBackground, (0, 0))
            # draw rectangle
            pygame.draw.rect(newWorld, color, [worldX - 150, worldY - 50, 150, 50])
            # draw text
            newWorld.blit(text, (worldX - 150 + 50, worldY - 50))

            self.generateCrimeScene(newWorld, numberOfHouse)
            pygame.display.flip()
            pygame.display.update()
            self.changeViewGameMode()

            self.endgame()

    def changeViewGameMode(self):
        # to prevent circulary import
        from game import GenerateMainWorld
        mousePositionX, mousePositionY = pygame.mouse.get_pos()
        #print(str(mousePositionX)+" "+ str(mousePositionY))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (mousePositionX > 1000) and (mousePositionX < 1200) and (mousePositionY > 560) and (mousePositionY < 600):
                    game = GenerateMainWorld()
                    game.generateMainWindow()

    def generateCrimeScene(self, currentSurface, houseNumber):
        second_surface=pygame.Surface([1200,50])
        second_surface.set_alpha(0)

        font=pygame.font.SysFont("Arial",32)
        text=""
        #grep the position of mouse to reveal items first X than Y
        mousePositionX,mousePostionY=pygame.mouse.get_pos()
        pressed_keys=pygame.mouse.get_pressed()

        if houseNumber == 0:
            text += "welcome in the house of Anna, search by clicking in the room."
        elif houseNumber == 1:
            text += "welcome in the house of Jef, search by clicking in the room"
        elif houseNumber == 2:
            text += "welcome in the house of Bob, search by clicking in the room"
        elif houseNumber == 3:
            text += "welcome in the house of Jasmien, search by clicking in the room"
        elif houseNumber == 4:
            text += "welcome in the house of Fran, search by clicking in the room"

        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
        if(pressed_keys[0]):
                match houseNumber:
                    case 0:
                        #print("house number 0")
                        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
                        if (mousePositionX>200) and (mousePositionX<300) and (mousePostionY>300) and (mousePostionY<410):
                            blood=pygame.image.load("images/crimeSceneProps/blood.png")

                            currentSurface.blit(blood, (230,340))

                        elif(mousePositionX>580) and (mousePositionX<680) and (mousePostionY>240)  and (mousePostionY<340):
                            candle=pygame.image.load("images/crimeSceneProps/candle.png")
                            currentSurface.blit(candle,(600,300))
                        '''
                        # x=880-900 y=460-480
                        elif(mousePositionX>800)and (mousePositionX<900) and (mousePostionY>380) and (mousePostionY<480):
                            knife=pygame.image.load("images/crimeSceneProps/knife.png")
                            currentSurface.blit(knife,(780,360))
                        
                        '''

                    case 1:
                        #print("house number is 1")
                        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
                        if (mousePositionX > 170) and (mousePositionX < 270) and (mousePostionY > 320) and (mousePostionY < 420):
                            blood = pygame.image.load("images/crimeSceneProps/blood.png")
                            # x,y
                            currentSurface.blit(blood, (230, 390))
                            # x=650-680 y=320-340
                        elif (mousePositionX > 470) and (mousePositionX < 570) and (mousePostionY > 400) and (mousePostionY < 500):
                            pipe = pygame.image.load("images/crimeSceneProps/pipe.png")
                            currentSurface.blit(pipe, (550, 480))
                        # x=880-900 y=460-480
                        elif (mousePositionX > 360) and (mousePositionX < 460) and (mousePostionY > 320) and (mousePostionY < 420):
                            candle = pygame.image.load("images/crimeSceneProps/candle.png")
                            currentSurface.blit(candle, (440, 400))

                    case 2:
                        #print("house number 2")
                        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
                        if (mousePositionX > 440) and (mousePositionX < 540) and (mousePostionY > 310) and (mousePostionY < 410):
                            blood = pygame.image.load("images/crimeSceneProps/blood.png")
                            # x,y
                            currentSurface.blit(blood, (520, 390))
                            # x=650-680 y=320-340
                        elif (mousePositionX > 500) and (mousePositionX < 600) and (mousePostionY > 140) and (mousePostionY < 240):
                            knife = pygame.image.load("images/crimeSceneProps/knife.png")
                            currentSurface.blit(knife, (580, 220))
                        elif (mousePositionX>40) and (mousePositionX<140) and (mousePostionY>270) and (mousePostionY<400):
                            candle = pygame.image.load("images/crimeSceneProps/candle.png")
                            currentSurface.blit(candle, (600, 300))

                    case 3:
                        #print("house number 3")
                        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
                        if (mousePositionX > 740) and (mousePositionX < 840) and (mousePostionY > 270) and (mousePostionY < 370):
                            blood = pygame.image.load("images/crimeSceneProps/blood.png")
                            # x,y
                            currentSurface.blit(blood, (820, 350))
                            # x=650-680 y=320-340
                        elif (mousePositionX > 180) and (mousePositionX < 280) and (mousePostionY > 210) and (mousePostionY < 310):
                            rope = pygame.image.load("images/crimeSceneProps/rope.png")
                            currentSurface.blit(rope, (260, 290))
                            # x=880-900 y=460-480
                        elif (mousePositionX > 870) and (mousePositionX < 970) and (mousePostionY > 270) and (mousePostionY < 370):
                            candle = pygame.image.load("images/crimeSceneProps/candle.png")
                            currentSurface.blit(candle, (950, 350))

                    case 4:
                        #print("house number 2")
                        #print("mouse positie x: " + str(mousePositionX) + " mouse positie y: " + str(mousePostionY))
                        if (mousePositionX > 780) and (mousePositionX < 880) and (mousePostionY > 310) and (mousePostionY < 410):
                            blood = pygame.image.load("images/crimeSceneProps/blood.png")
                            # x,y
                            currentSurface.blit(blood, (860, 390))
                            # x=650-680 y=320-340
                        elif (mousePositionX > 110) and (mousePositionX < 210) and (mousePostionY > 450) and (mousePostionY < 550):
                            gun = pygame.image.load("images/crimeSceneProps/pistol.png")
                            currentSurface.blit(gun, (190, 530))
                            # x=880-900 y=460-480
                        elif (mousePositionX > 0) and (mousePositionX < 70) and (mousePostionY > 110) and (mousePostionY < 210):
                            candle = pygame.image.load("images/crimeSceneProps/candle.png")
                            currentSurface.blit(candle, (550, 190))

        text_surface = font.render(text, True, (0, 0, 255))
        currentSurface.blit(text_surface, (10, 0))
        currentSurface.blit(second_surface, (0, 0))
    def endgame(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()