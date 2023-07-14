import pygame
from typing import Callable

class Particle:
    def __init__(self, surface: pygame.Surface, position: dict, velocity: dict, draw_offset: Callable[[str], tuple]) -> None:
        self.surface: pygame.Surface = surface
        
        self.draw_offset: Callable[[str], tuple] = draw_offset
        
        self.position: dict = position
        self.velocity: dict = velocity
        
        self.radius: int = 2
        self.color: str = "#ff0000"
    
    def draw(self) -> None:
        pygame.draw.circle(
            self.surface, self.color,
            (
                self.position["x"] - self.draw_offset()[0], 
                self.position["y"] - self.draw_offset()[1]
            ),
            self.radius
        )
    
    def update(self) -> None:
        self.velocity["x"] /= 1.01
        self.velocity["y"] /= 1.01
        
        self.position["x"] += self.velocity["x"] 
        self.position["y"] += self.velocity["y"]
        
        self.draw()