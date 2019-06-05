import pygame
import math
import sys
from cube import *
from enum import Enum

class piece:

    def __init__ (self, type = 't',  initialCoords = (0, 0, 5)):
        self.x = initialCoords[0]
        self.y = initialCoords[1]
        self.z = initialCoords[2]
        cubeCoords = ( self.x, self.y, self.z), (self.x, self.y + 1, self.z),(self.x, self.y - 1, self.z), (self.x, self.y, self.z + 1)
        self.cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]
        self.counter = 0

    def moveX(self, distance):
        self.x += distance
        updateCoords()

    def moveY(self, distance):
        self.y += distance
        updateCoords()

    def moveZ(self, distance):
        self.z += distance
        updateCoords()

    def updateCoords(self):
        cubeCoords = ( self.x, self.y, self.z), (self.x, self.y + 1, self.z),(self.x, self.y - 1, self.z), (self.x, self.y, self.z + 1)
        self.cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]

    def update(self, dt, key):
        self.counter += 1

        if key[pygame.K_w]:
            self.z +=1

        if key[pygame.K_s]:
            self.z -=1

        if key[pygame.K_d]:
            self.x +=1

        if key[pygame.K_a]:
            self.x -=1

        if self.counter%20 == 0:
            self.y +=1

class t_piece:

    def __init__ (self, initialCoords = (0, 0, 5)):
        self.x = initialCoords[0]
        self.y = initialCoords[1]
        self.z = initialCoords[2]
        cubeCoords = ( self.x, self.y, self.z), (self.x, self.y + 1, self.z),(self.x, self.y - 1, self.z), (self.x, self.y, self.z + 1)
        self.cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]

    def moveX(self, distance):
        self.x += distance
        updateCoords()

    def moveY(self, distance):
        self.y += distance
        updateCoords()

    def moveZ(self, distance):
        self.z += distance
        updateCoords()

    def updateCoords(self):
        cubeCoords = ( self.x, self.y, self.z), (self.x, ++self.y, self.z),(self.x, --self.y, self.z), (self.x, self.y, ++self.z)
        self.cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]







