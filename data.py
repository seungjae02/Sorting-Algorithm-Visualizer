from settings import *
import pygame
import random

class Datum:
    def __init__(self, value):
        self.value = value
        self.colour = TAN

class Data:
    def __init__(self, app, nums):
        self.obj_array = []
        self.app = app
        self.nums = nums

    def generate_data(self):
        for i,v in enumerate(self.nums):
            datum = Datum(v)
            self.obj_array.append(datum)






