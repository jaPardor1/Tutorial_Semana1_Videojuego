

import json
import pygame
import esper
from src.create.prefab_creator import crear_cuadrado
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.systems.s_movement import  system_screen_movement
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.data.json_extract import extraer_datos_json
class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        data_window= extraer_datos_json('assets/cfg/window.json')
        window_width= data_window["window"].get('size').get('w')
        window_height= data_window["window"].get('size').get('h')
        window_title= data_window["window"].get('title')
        window_framerate= data_window["window"].get('framerate')
        self.r =data_window["window"].get('bg_color').get('r') 
        self.g =data_window["window"].get('bg_color').get('g') 
        self.b =data_window["window"].get('bg_color').get('b')




         

        
        
        self.screen = pygame.display.set_mode((window_width,window_height),pygame.SCALED)#visualizacion de la ventaqna para que se vea bien.
        pygame.display.set_caption(window_title)
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = window_framerate
        self.delta_time= 0
        
        self.ecs_world = esper.World()


    # implementacion mas sencilla de un game loop
    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):

        crear_cuadrado(self.ecs_world, pygame.Vector2(50,50),pygame.Vector2(150,100),pygame.Vector2(100,100),pygame.Color(255,255,199))
        

        



    

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time()/ 1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False


    def _update(self):
        system_screen_movement(self.ecs_world,self.delta_time)
        system_screen_bounce(self.ecs_world,self.screen)
        
    def _draw(self):
        self.screen.fill((self.r,self.g,self.b))
        system_rendering(self.ecs_world,self.screen)
        pygame.display.flip()

    def _clean(self):
        pygame.quit
