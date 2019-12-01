from config import tetris_shapes, bit_matrix
from utils import *
from random import randrange as rand
from random import choice
import sys
import copy
import time
from threading import Timer

class Tetris(object):
    def __init__(self):
        self.redraw = True
        self.score = 0
        self.start_time = time.time()
        self.led_matrix = []
        self.next_shape = choice(list(tetris_shapes))
        self.message = self.next_shape + ' ' * (7 - len(str(self.score))) + str(self.score)
        self.init_game()


    def new_stone(self):
        new_stone = tetris_shapes[self.next_shape]
        for _ in range(rand(4)):
            new_stone = rotate_clockwise(new_stone)
        self.next_shape = choice(list(tetris_shapes))
        self.stone = new_stone
        self.stone_x = int(config['cols'] / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0
        self.message = self.next_shape + ' ' * (7 - len(str(self.score))) + str(self.score)
        if check_collision(self.board,
                           self.stone,
                           (self.stone_x, self.stone_y)):
            self.gameover = True

    def init_game(self):
        self.board = new_board()
        self.new_stone()


    def move(self, delta_x):
        if not self.gameover and not self.paused:
            new_x = self.stone_x + delta_x
            if new_x < 0:
                new_x = 0
            if new_x > config['cols'] - len(self.stone[0]):
                new_x = config['cols'] - len(self.stone[0])
            if not check_collision(self.board,
                                   self.stone,
                                   (new_x, self.stone_y)):
                self.stone_x = new_x
        self.redraw = True

    def quit(self):
        self.timeframe.cancel()
        self.gameover = True
        self.led_matrix = []
        self.score = 0
        self.next_shape = choice(list(tetris_shapes))
        self.init_game()
        

    def drop(self):
        if not self.gameover and not self.paused:
            self.stone_y += 1
            if check_collision(self.board,
                               self.stone,
                               (self.stone_x, self.stone_y)):
                self.board = join_matrixes(
                    self.board,
                    self.stone,
                    (self.stone_x, self.stone_y))
                self.new_stone()
                while True:
                    for i, row in enumerate(self.board[:-1]):
                        if 0 not in row:
                            self.board = remove_row(self.board, i)
                            self.score += 100
                            self.message = self.next_shape + ' ' * (7  - len(str(self.score))) + str(self.score)
                            break
                    else:
                        break
        self.redraw = True
        self.timeframe.cancel()
        self.timeframe = Timer(0.75, self.next_frame)
        self.timeframe.start()
        #print(time.time() - self.start_time)
        #self.start_time = time.time()
        

    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board,
                                   new_stone,
                                   (self.stone_x, self.stone_y)):
                self.stone = new_stone
        self.redraw = True

    def toggle_pause(self):
        self.paused = not self.paused
            

    def next_frame(self):
        self.drop()

    def run(self):
        self.gameover = False
        self.paused = False
        self.timeframe = Timer(0.75, self.next_frame)
        self.timeframe.start()
        while not self.gameover:
            if self.redraw:
                self.led_matrix = copy.deepcopy(self.board)
                for i, row in enumerate(self.stone):
                    for j, pixel in enumerate(row):
                        self.led_matrix[self.stone_y+i][self.stone_x+j] = self.led_matrix[self.stone_y+i][self.stone_x+j] or pixel
                self.redraw = False


