import pygame
import math

class Camera:
    def __init__(self, pos = (0,0,0), rot = (0,0)):
        self. pos = list(pos)
        self.rot = list(rot)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rot[0] += y
            self.rot[1] += x

    def update(self, dt, key):
        s = dt*10

        if(key[pygame.K_q]):
            self.pos[1] +=s
        if(key[pygame.K_e]):
            self.pos[1] -=s


        x, y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

        if key[pygame.K_w]:
           self.pos[0] += x
           self.pos[2] += y
        if key[pygame.K_s]:
            self.pos[0] -= x
            self.pos[2] -= y
        if key[pygame.K_d]:
            self.pos[0] -= y
            self.pos[2] += x
        if key[pygame.K_a]:
            self.pos[0] += y
            self.pos[2] -= x


        if(key[pygame.K_j]):
            self.rot[0] += s/3
        if(key[pygame.K_k]):
            self.rot[0] -= s/3
        if(key[pygame.K_l]):
            self.rot[1] +=s/3
        if(key[pygame.K_h]):
            self.rot[1] -=s/3
