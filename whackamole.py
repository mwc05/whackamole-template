import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        mole_x = 0
        mole_y = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (int(event.pos[0]/32), int(event.pos[1]/32)) == (int(mole_x/32), int(mole_y/32)):
                        mole_x = random.randrange(0, 20) * 32
                        mole_y = random.randrange(0, 16) * 32
            screen.fill("light green")
            for i in range(0, 640, 32):
                pygame.draw.line(screen, "black", (i, 0), (i, 512))
            for i in range(0, 512, 32):
                pygame.draw.line(screen, "black", (0, i), (640, i))
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
