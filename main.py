import pygame
import math
import sys

from cube import *
from camera import *
from pieces import *

def rotate2d(position, radians):
    x, y = position
    sinAngle, cosAngle = math.sin(radians), math.cos(radians)
    return x * cosAngle - y * sinAngle, y * cosAngle + x * sinAngle

def setup():
    pygame.init()
    pygame.mouse.set_visible(0);
    pygame.event.set_grab(1)


if __name__ == "__main__":
    setup()

    WIDTH, HEIGHT = 500, 500
    cx, cy = WIDTH// 2, HEIGHT // 2

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    camera = Camera((-1.9, -14.77, -11.05), (0.14, -5.65))

    firstPiece = piece('t', (0, -20, 0))
    base = base()
    staticCubes = base.cubes

    while True:

        cubes = firstPiece.cubes + staticCubes
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

        faceList = []
        faceColor = []
        depth = []

        for obj in cubes:
            vertList = []
            screenCoordinates = []

            for x,y,z in obj.verts:
                x -= camera.position[0]
                y -= camera.position[1]
                z -= camera.position[2]

                x,z = rotate2d((x,z), camera.rotation[1])
                y,z = rotate2d((y,z), camera.rotation[0])
                vertList += [(x,y,z)]

                f = 200/z
                x, y = x*f, y*f
                screenCoordinates += [(cx + int(x), cy + int(y))]

            for faceIndex in range(len(obj.faces)):
                face = obj.faces[faceIndex]

                on_screen = False
                for i in face:
                    x, y = screenCoordinates[i]
                    if vertList[i][2] > 0 and x > 0 and x < WIDTH and y > 0 and y < HEIGHT:
                        on_screen = True
                        break

                if on_screen:
                    coords = [screenCoordinates[i] for i in face]
                    faceList += [coords]
                    depth += [sum(sum(vertList[j][i] for j in face)**2 for i in range(3))]
            #check if cube hit the bottom
            if(obj.)

        order = sorted(range(len(faceList)), key =lambda i: depth[i], reverse = 1)

        #drawing to screen
        for i in order:
            try:
                pygame.draw.polygon(screen, faceColor[i], faceList[i])
            except:
                pass

        pygame.display.flip()
        key = pygame.key.get_pressed()
        camera.update(dt, key)
        firstPiece.update(dt, key)
        firstPiece.updateCoords()

        #for debugging
        print("x: %f\ny: %f\nz: %f\n0: %f\n1: %f" % (camera.position[0], camera.position[1], camera.position[2], camera.rotation[0], camera.rotation[1]))
