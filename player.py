import pygame
import pygame.locals

from houses import houseDesign

class newPlayer(pygame.sprite.Sprite):
    # spawn player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 60
        self.images = []

        img = pygame.image.load("images/hero2.png")
        self.images.append(img)
        self.image = self.images[0]

        self.rect = self.image.get_rect()


        self.defaultPos()
        self.changeView()

    def defaultPos(self):
        self.rect.x = 430
        self.rect.y = 450
    def updatePosition(self):
        self.rect.x=self.rect.x
        self.rect.y=self.rect.y
    def move(self):
        currentY = 0
        currentX = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        # print("key left")
                        currentX -= 35
                        self.update(currentX,currentY)

                    case pygame.K_RIGHT:
                        # print("key right")
                        currentX += 35
                        self.update(currentX, currentY)
                    case pygame.K_UP:
                        # print("key up")
                        currentY -= 35
                        self.update(currentX, currentY)
                    case pygame.K_DOWN:
                        # print("key down")
                        currentY += 35
                        self.update(currentX,currentY)
            elif event.type==pygame.QUIT:
                pygame.quit()


    def update(self, currentX, currentY):
        if (self.rect.y + currentY > 300) and (self.rect.y + currentY < 580) and (currentX == 0) and (currentY != 0):
            self.rect.y = self.rect.y + currentY


        elif (self.rect.x + currentX > 0) and (self.rect.x + currentX < 880) and (currentY == 0) and (currentX != 0):
            self.rect.x = self.rect.x + currentX

        else:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y
    def changeView(self):
        xPos = int(self.rect.x)
        yPos = int(self.rect.y)
        positionDoorHouses=[
            [430, 345],
            [150, 380],
            [675, 380],
            [745, 555],
            [150, 555]
        ]
        for i in range(5):
            if positionDoorHouses[i][0] == xPos and positionDoorHouses[i][1] == yPos:
                pygame.quit()
                insideHome=houseDesign()
                insideHome.set_houseNumber(i)
                insideHome.generateWindow()
