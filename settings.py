import random

##### Screen Settings #####
WIDTH = 800
HEIGHT = 800

##### Button Settings #####
visual_button_length = 110
visual_button_height = 50

##### Font Settings #####
FONT = 'Arial Black'

##### Colour Settings #####
WHITE = (255,255,255)
AQUAMARINE = (127,255,212)
BLACK = (0,0,0)
ALICE = (240,248,255)
STEELBLUE = (110,123,139)
MINT = (189,252,201)
SPRINGGREEN = (0,255,127)
TOMATO = (255,99,71)
ROYALBLUE = (72,118,255)
TAN = (255,165,79)
RED = (255,0,0)
PINK = (255,192,203)

NOT_HIGHLIGHTED_DATA = TAN

##### Numbers List
num_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175,
            182, 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329,
            336, 343, 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483,
            490, 497, 504, 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637,
            644, 651, 658, 665, 672, 679, 686, 693, 700]

random.shuffle(num_list)
print(num_list)

