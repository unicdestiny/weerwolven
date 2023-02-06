import pygame
import pygame.locals
from game import GenerateMainWorld
class manualDisplay:
    def generateWindow(self):
        windowWidth,windowHeight=1000,650
        blackBackground=[0,0,0]
        color=[255,0,0]
        world=pygame.display.set_mode([windowWidth,windowHeight])
        pygame.display.set_caption("weerwolven")
        world.fill(blackBackground)
        world.set_alpha(200)
        running=True

        pygame.init()

        fontHeader = pygame.font.SysFont("Arial", 50)
        header = "manual:"
        font =pygame.font.SysFont("Arial",25)
        text=[
            " * Het spel heeft 5 personen die elk een huis hebben er zijn ook 5 moordwapens.",
            " * Elke nacht gebeurt een moord en u dient de moordenaar te zoeken dit zal dus 1 van de 5 geweest zijn.",
            " * Het is aan u om op het einde van het spel te raden wie de moordenaar is.",
            " * Je kan de moordenaar raden tijdens de nacht.",
            "exit manual"
        ]

        while running:
            self.changeView()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    running=False
            header_surface = fontHeader.render(header, True, (255, 255, 255))
            world.blit(header_surface, (20, 0))
            for i in range(3):
                list_surface=font.render(text[i],True,(255,255,255))
                world.blit(list_surface,(40,80+80*i))

            pygame.draw.rect(world, color, [windowWidth - 150, windowHeight - 50, 150, 50])
            text_surface=font.render(text[4],True,(255,255,255))
            world.blit(text_surface, (windowWidth - 170 + 50, windowHeight - 50))
            pygame.display.flip()


    def changeView(self):
        mousePositionX,mousePositionY=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if (mousePositionX>800) and (mousePositionX<1000) and (mousePositionY>450) and (mousePositionY<650):

                    game=GenerateMainWorld()
                    game.generateMainWindow()

manual=manualDisplay()
manual.generateWindow()