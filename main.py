import pygame
import math
import sys

from cube import *
from camera import *

def rotate2d(pos, rad):
    x, y = pos
    s, c = math.sin(rad), math.cos(rad)
    return x*c - y*s, y*c + x*s

if __name__ == "__main__":

    pygame.init()
    pygame.event.get()
    pygame.mouse.get_rel()
    pygame.mouse.set_visible(0);
    pygame.event.set_grab(1)

    WIDTH, HEIGHT = 400, 600
    cx, cy = WIDTH// 2, HEIGHT // 2

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    camera = Camera((12.500703, -13.84000, -4.54922), (0.136667, -0.950000))


    cubeCoords = (0, 0, 0), (2, 2, 2), (2, 2, -2), (2, -2, -2), (-2, 2, -2), (2, -2, 2), (-2, -2, 2), (-2, -2, -2), (-2, 2, 2)

    cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]

    while True:

        dt = clock.tick()/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill((0,0,0))
        '''
        for edge in edges:

            points = []
            for x, y, z in  (verts[edge[0]], verts[edge[1]]):

                x -= camera.pos[0]
                y -= camera.pos[1]
                z -= camera.pos[2]

                x,z = rotate2d((x,z), camera.rot[1])
                y,z = rotate2d((y,z), camera.rot[0])


                z += 5
                f = 200/z
                x, y = x*f, y*f
                points += [(cx + int(x), cy +int(y))]
            pygame.draw.line(screen, (0,0,0), points[0], points[1], 1)
        '''

        faceList = []
        faceColor = []
        depth = []

        for obj in cubes:

            vert_list = []
            screen_coords = []
            for x,y,z in obj.verts:

                x -= camera.pos[0]
                y -= camera.pos[1]
                z -= camera.pos[2]

                x,z = rotate2d((x,z), camera.rot[1])
                y,z = rotate2d((y,z), camera.rot[0])
                vert_list += [(x,y,z)]

                f = 200/z
                x, y = x*f, y*f
                screen_coords += [(cx + int(x), cy + int(y))]

            for f in range(len(obj.faces)):
                face = obj.faces[f]

                on_screen = False
                for i in face:
                    x, y = screen_coords[i]
                    if vert_list[i][2] > 0 and x > 0 and x < WIDTH and y > 0 and y < HEIGHT:
                        on_screen = True
                        break

                if on_screen:
                    coords = [screen_coords[i] for i in face]
                    faceList += [coords]
                    faceColor += [obj.colors[f]]

                    depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

        order = sorted(range(len(faceList)), key =lambda i: depth[i], reverse = 1)

        for i in order:
            try:
                pygame.draw.polygon(screen, faceColor[i], faceList[i])
            except:
                pass

        pygame.display.flip()

        key =pygame.key.get_pressed()
        camera.update(dt, key)

