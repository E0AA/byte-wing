import pygame, random
from random import randint as rint
from assets.modules.wing import Wing
from assets.modules.celestial import Celestial
import settings as sets

def main() -> None:
    RUN: bool = True
    
    draw_offset: tuple = [0, 0]
    
    screen: pygame.Surface = pygame.display.set_mode(
        (sets.WIDTH, sets.HEIGHT),
        pygame.RESIZABLE
    )
    clock: pygame.Clock = pygame.time.Clock()
    
    wing: Wing = Wing(screen, lambda: draw_offset)
    objects: list[Celestial] = []
    
    for _ in range(100):
        size = rint(16, 512)
        image = random.choice(
            [
                "./assets/images/asteroid-1.png",
                "./assets/images/asteroid-2.png",
                "./assets/images/asteroid-3.png",
                "./assets/images/asteroid-4.png"
            ]
        )
        
        objects.append(
            Celestial(
                screen, image, 
                lambda: draw_offset, 
                width = size, height = size, 
                x = rint(-2048, 2048), y = rint(-2048, 2048),
            )
        )
        
        objects[-1].z_distance = rint(1, 10)
    
    objects.sort(key=lambda obj: obj.z_distance, reverse=True)
    
    while RUN:
        clock.tick(sets.FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
        
        screen.fill((0, 0, 0))

        for planet in objects:
            planet.draw()
        
        wing.update()
        
        draw_offset = (wing.position["x"]-512, wing.position["y"]-256)

        pygame.display.update()
    
    pygame.display.quit()

if __name__ == "__main__":
    main()