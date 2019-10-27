#!/usr/bin/python
# -*- coding:utf-8 -*-
from ctypes import *
import time
import RPi.GPIO as GPIO

class MAX7219:
    def __init__(self):
        self.hspi = CDLL('./dev_hardware_SPI.so')
        self.hspi.DEV_HARDWARE_SPI_begin("/dev/spidev0.0")
        self.hspi.DEV_HARDWARE_SPI_ChipSelect(3)
        self.cs_pin = 8
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.cs_pin, GPIO.OUT)
        
    def WriteByte(self, Reg):
        GPIO.output(self.cs_pin, 0)
        self.hspi.DEV_SPI_WriteByte(Reg)
        
    def Write(self, address1, dat1, address2, dat2):
        GPIO.output(self.cs_pin, 0)
        self.WriteByte(address1)
        self.WriteByte(dat1)
        self.WriteByte(address2)
        self.WriteByte(dat2)
        GPIO.output(self.cs_pin, 1)
        
    def WriteMap(self, matrix):
        map1 = [[x[i] for x in matrix[:8][::-1]] for i in range(8)]
        map2 = [[x[i] for x in matrix[8:][::-1]] for i in range(8)]
        for i in range(8):
            out1 = 0
            out2 = 0
            for bit in map1[i]:
                out1 = (out1 << 1) | bit
            for bit in map2[i]:
                out2 = (out2 << 1) | bit
            self.Write(i+1, out1, i+1, out2)
        
    def Init(self):
        self.Write(0x09,0x00,0x09,0x00)
        self.Write(0x0a,0x03,0x0a,0x03)
        self.Write(0x0b,0x07,0x0b,0x07)
        self.Write(0x0c,0x01,0x0c,0x01)
        self.Write(0x0f,0x00,0x0f,0x00)

