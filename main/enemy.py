import random

import pygame
import math
from gobject import GameObject


class Enemy(GameObject):
    def __init__(self, xy=None, playground=None, sensitivity=1):
        GameObject.__init__(self, playground)
        if xy is None:
            self._y = -100
            self._x = random.randint(10, playground[0] - 100)
        else:
            self._x = xy[0]
            self._y = xy[1]

        self._objectBound = (10, self._playground[0] - 100, -100, self._playground[1])
        self._moveScale = 0.1 * sensitivity
        if random.random() > 0.5:
            self._slop = 0.5
        else:
            self._slop = -0.5
        self._moveScaleY = math.cos(self._slop * math.pi / 2) * self._moveScale
        self._moveScaleX = math.sin(self._slop * math.pi / 2) * self._moveScale
