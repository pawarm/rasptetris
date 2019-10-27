from config import tetris_shapes, bit_matrix
from utils import *
from random import randrange as rand
from MAX7219 import MAX7219
import sys
import copy
import keyboard
import time
from threading import Timer

class Tetris(object):
    def __init__(self):
        self.led = MAX7219()
        self.led.Init()
        self.init_game()
        self.timeframe = Timer(0.75, self.next_frame)

    def new_stone(self):
        self.stone = tetris_shapes[rand(len(tetris_shapes))]
        self.stone_x = int(config['cols'] / 2 - len(self.stone[0]) / 2)
        self.stone_y = 0

        if check_collision(self.board,
                           self.stone,
                           (self.stone_x, self.stone_y)):
            self.gameover = True

    def init_game(self):
        self.board = new_board()
        self.new_stone()

    def center_msg(self):
        pass


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

    def quit(self):
        self.center_msg()
        sys.exit()

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
                            self.board = remove_row(
                                self.board, i)
                            break
                    else:
                        break

    def rotate_stone(self):
        if not self.gameover and not self.paused:
            new_stone = rotate_clockwise(self.stone)
            if not check_collision(self.board,
                                   new_stone,
                                   (self.stone_x, self.stone_y)):
                self.stone = new_stone

    def toggle_pause(self):
        self.paused = not self.paused

    def start_game(self):
        if self.gameover:
            self.init_game()
            self.gameover = False
            
    def press(self, event):
        if event.name == 'left':
            self.move(-1)
        elif event.name == 'right':
            self.move(+1)
        elif event.name == 'down':
            self.drop()
        elif event.name == 'up':
            self.rotate_stone()
        elif event.name == 'p':
            self.toggle_pause()
        elif event.name == 'space':
            self.start_game()
        elif event.name == '\x1b':
            self.quit()

    def next_frame(self):
        self.drop()
        self.timeframe = Timer(0.75, self.next_frame)
        self.timeframe.start()

    def run(self):

        self.gameover = False
        self.paused = False

        self.timeframe.start()
        while 1:
            if self.gameover:
                self.center_msg()
            else:
                if self.paused:
                    self.center_msg()
            led_matrix = copy.deepcopy(self.board)
            for i, row in enumerate(self.stone):
                for j, pixel in enumerate(row):
                    led_matrix[self.stone_y+i][self.stone_x+j] = led_matrix[self.stone_y+i][self.stone_x+j] or pixel
            self.led.WriteMap(led_matrix)


if __name__ == '__main__':
    App = Tetris()
    keyboard.on_press(App.press)
    App.run()
