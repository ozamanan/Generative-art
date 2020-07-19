from PIL import Image
import cv2
import numpy as np
import glob
import os
import math
from random import shuffle, seed
import datetime

class Canvas():
    def __init__(self):
        super(Canvas, self).__init__()
        self.width = 1920
        self.height = 1080
        self.zoom = 1
        self.canvas = Image.new("RGB", (self.width, self.height), "white")
        self.pix = self.canvas.load()

def circle():
    print("Hello world!")