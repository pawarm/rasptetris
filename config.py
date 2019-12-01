config = {
    'cols': 8,
    'rows': 16,
    'delay': 750,
    'maxfps': 30
}

text_display = {
    "PLAY":['p', 'l', 'a', 'y', ' ', ' ', ' ', ' '],
    "QUIT":['q', 'u', 'i', 't', ' ', ' ', ' ', ' '],
    "EXIT":[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
}

tetris_shapes = {
    'T':[[1, 1, 1],
     [0, 1, 0]],

    'S':[[0, 1, 1],
     [1, 1, 0]],

    'Z':[[1, 1, 0],
     [0, 1, 1]],

    'J':[[1, 0, 0],
     [1, 1, 1]],

    'L':[[0, 0, 1],
     [1, 1, 1]],

    'I':[[1, 1, 1, 1]],

    'O':[[1, 1],
     [1, 1]]
}

bit_matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
    ]

#  8
# 3 7
#  2
# 4 6
#  51 

digits = {
    '0':0b11000000,
    '1':0b11111001, 
    '2':0b10100100, 
    '3':0b10110000, 
    '4':0b10011001, 
    '5':0b10010010, 
    '6':0b10000010, 
    '7':0b11111000, 
    '8':0b10000000, 
    '9':0b10010000, 
    ' ':0b11111111,
    'a':0b10001000,
    'b':0b10000011,
    'c':0b11000110,
    'd':0b10100001,
    'e':0b10000110,
    'f':0b10001110,
    'g':0b11000010,
    'h':0b10001001,
    'i':0b11001111,
    'j':0b11100001,
    'l':0b11000111,
    'n':0b10101011,
    'o':0b11000000,
    'p':0b10001100,
    'q':0b10011000,
    'r':0b10101111,
    's':0b10010010,
    't':0b10000111,
    'u':0b11000001,
    'y':0b10010001,
    'T':0b10001111,
    'S':0b10011011,
    'Z':0b10101101,
    'J':0b11110001,
    'L':0b11000111,
    'I':0b11001111,
    'O':0b10100011
    }
