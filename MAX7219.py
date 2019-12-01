#!/usr/bin/python3
# -*- coding:utf-8 -*-
import time
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import Image
from luma.led_matrix.device import max7219

class MAX7219:
    def __init__(self):
        serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(serial, cascaded=2, block_orientation=90)
        
    def WriteMap(self, matrix):
        tuple_list = []
        for i, row in enumerate(matrix):
            for j, col in enumerate(row):
                if col:
                    tuple_list.append((i,j))
        with canvas(self.device) as draw:
            draw.point(tuple_list, 1)


