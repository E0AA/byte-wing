import pygame, random
from typing import Callable

class Celestial:
    def __init__(self, surface: pygame.Surface, image_file: str, draw_offset: Callable[[str], tuple], width: int = 128, height: int = 128, x: int = 0, y: int = 0) -> None:
        self.surface: pygame.Surface = surface
        
        self.draw_offset: Callable[[str], tuple] = draw_offset
        self.z_distance: int = 1
        
        self.position: dict = {
            "x": x,
            "y": y
        }
        
        self.size: dict = {
            "width": width,
            "height": height
        }
        
        self.image = pygame.Surface = pygame.transform.rotate(
            pygame.transform.scale(
                pygame.image.load(image_file),
                tuple(self.size.values())
            ),
            random.randint(-360, 360)
        )
    
    def draw(self) -> None:
        self.surface.blit(
            self.image,
            (
                self.position["x"] - (self.draw_offset()[0]/self.z_distance), 
                self.position["y"] - (self.draw_offset()[1]/self.z_distance)
            )
        )