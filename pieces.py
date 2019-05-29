
from cube import *
from enum import Enum

class piece:

    def __init__ (self,type = 't',  initialCoords = (0, 0, 5)):
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
        cubeCoords = ( self.x, self.y, self.z), (self.x, self.y + 1, self.z),(self.x, self.y - 1, self.z), (self.x, self.y, self.z + 1)
        self.cubes = [Cube((x, y, z)) for x, y, z in cubeCoords]

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







