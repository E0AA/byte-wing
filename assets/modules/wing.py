import pygame, math
from random import randint as rint
from assets.modules.particles import Particle

from typing import Callable

class Wing:
    def __init__(self, surface: pygame.Surface, draw_offset: Callable[[str], tuple], image_file: str = "./assets/images/wing.png") -> None:
        self.surface: pygame.Surface = surface
        
        self.draw_offset: Callable[[str], tuple] = draw_offset
        
        self.exhaust_particles: int = 5
        self.exhaust_spread: int = 10
        self.rotation_step_size: int = 5
        self.velocity_drag: float = 1.03
        
        self.position: dict = {
            "x": 512,
            "y": 256
        }
        self.velocity: dict = {
            "x": 0,
            "y": 0
        }
        self.size: dict = {
            "width": 64,
            "height": 64
        }
        self.rotation: float = 0.0
        self.acceleration: float = 0.0
        
        self.image: pygame.Surface = pygame.transform.scale(
            pygame.image.load(image_file),
            tuple(self.size.values())
        )
        
        self.particles: list[Particle] = []
    
    def coord_circle(self, angle, radius) -> tuple[int]:
        theta: float = math.pi * angle / 180
        x: int = radius * math.cos(theta)
        y: int = radius * math.sin(theta)

        return x, y

    def launch_particle(self) -> None:
        self.particles.append(
            Particle(
                self.surface,
                self.position.copy(),
                { # This part is not important
                    "x": -((self.coord_circle(self.rotation, self.acceleration)[0]+(rint(-self.exhaust_spread, self.exhaust_spread)/100))*rint(7, 25)),
                    "y": -((self.coord_circle(self.rotation, self.acceleration)[1]+(rint(-self.exhaust_spread, self.exhaust_spread)/100))*rint(7, 25)),
                },
                self.draw_offset
            )
        )

    def get_input(self) -> None:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotation -= self.rotation_step_size
        if keys[pygame.K_d]:
            self.rotation += self.rotation_step_size
        
        if keys[pygame.K_w]:
            self.acceleration += 0.01
            for _ in range(5):
                self.launch_particle()
        if keys[pygame.K_s]:
            self.velocity["x"] /= 1.1
            self.velocity["y"] /= 1.1
    
    def draw(self) -> None:
        self.rotated_image = pygame.transform.rotate(self.image, self.rotation)
        self.rect = self.rotated_image.get_rect(center=self.image.get_rect().center)
        self.rect.center = (512, 256)
        
        self.surface.blit(
            pygame.transform.rotate(self.image, -self.rotation),
            self.rect
        )
    
    def update(self) -> None:
        self.velocity["x"] += self.coord_circle(self.rotation, self.acceleration)[0]
        self.velocity["y"] += self.coord_circle(self.rotation, self.acceleration)[1]
        
        self.velocity["x"] /= self.velocity_drag
        self.velocity["y"] /= self.velocity_drag
        self.acceleration /= self.velocity_drag
        
        self.position["x"] += self.velocity["x"] 
        self.position["y"] += self.velocity["y"]
        
        self.rotation %= 360
        
        for particle in self.particles:
            if abs(sum(particle.velocity.values())) < 0.5:
                self.particles.remove(particle)
            else:
                particle.update()
        
        self.get_input()
        self.draw()