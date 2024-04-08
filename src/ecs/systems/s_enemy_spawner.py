
import esper
import pygame
from src.create.prefab_creator import crear_cuadrado
from src.data.json_extract import extraer_datos_json
from src.ecs.components.c_enemy_spawner import CEnemySpawner


def system_enemy_spawner(ecs_world:esper.World,level,enemies_info):
    enemy_spawner_entity = ecs_world.create_entity()
    ecs_world.add_component(enemy_spawner_entity,CEnemySpawner(level=level))
    components = ecs_world.get_components(CEnemySpawner)
    c_e:CEnemySpawner
    
    for entity ,(c_e) in components:
        #print(c_e[0].level_info)
        for i in c_e[0].level_info['enemy_spawn_events']:
            enemy_posx=i.get("position").get("x")
            enemy_posy=i.get("position").get("y")
            enemy_type= i.get("enemy_type")
            enemy=enemies_info.get(enemy_type)
            enemy_size_x=enemy.get("size").get("x")
            enemy_size_y=enemy.get("size").get("y")
            enemy_color_r=enemy.get("color").get("r")
            enemy_color_g=enemy.get("color").get("g")
            enemy_color_b=enemy.get("color").get("b")
            enemy_min_velocity= enemy.get("velocity_min")
            enemy_max_velocity= enemy.get("velocity_max")

            crear_cuadrado(ecs_world, pygame.Vector2(enemy_size_x,enemy_size_y),
                           pygame.Vector2(enemy_posx,enemy_posy),
                           pygame.Vector2(enemy_min_velocity,enemy_max_velocity),
                           pygame.Color(enemy_color_r,enemy_color_g,enemy_color_b))
