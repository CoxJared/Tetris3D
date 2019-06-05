import pygame
import math

class Camera:
    def __init__(self, position = (0,0,0), rotation = (0,0)):
        self. position = list(position)
        self.rotation = list(rotation)

    def events(self, event):
        if event.type == pygame.MOUSEMOTION:
            x, y = event.rel
            x /= 200
            y /= 200
            self.rotation[0] += y
            self.rotation[1] += x

    def update(self, dt, key):
        s = dt * 10

        if(key[pygame.K_q]):
            self.position[1] +=s

        if(key[pygame.K_e]):
            self.position[1] -=s

        x, y = s * math.sin(self.rotation[1]), s * math.cos(self.rotation[1])

        #if key[pygame.K_w]:
        #   self.position[0] += x
        #   self.position[2] += y

        #if key[pygame.K_s]:
        #    self.position[0] -= x
        #    self.position[2] -= y

        #if key[pygame.K_d]:
        #    self.position[0] -= y
        #    self.position[2] += x

        #if key[pygame.K_a]:
        #    self.position[0] += y
        #    self.position[2] -= x


        if(key[pygame.K_j]):
            self.rotation[0] += s/3
        if(key[pygame.K_k]):
            self.rotation[0] -= s/3
        if(key[pygame.K_l]):
            self.rotation[1] +=s/3
        if(key[pygame.K_h]):
            self.rotation[1] -=s/3
