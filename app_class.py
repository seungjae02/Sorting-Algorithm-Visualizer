import pygame
import sys
from settings import *
from buttons_class import *
from bubblesort_class import *
from selectionsort_class import *
from mergesort_class import *
from data import *


pygame.init()

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'main menu'
        self.sorting_state = ''
        self.load()

        self.data = num_list.copy()
        random.shuffle(self.data)

        self.data_generated = False

        # self.data = Data(self, self.nums)

    # Define Buttons
        # Start Button
        self.start_button = Buttons(self, SPRINGGREEN, 300, 620, 200, 70, text='START')
        # Visualize Buttons
        self.bubble_sort_button = Buttons(self, PINK, 20*1+110*0, 10, visual_button_length, visual_button_height, text='Bubble Sort')
        self.selection_sort_button = Buttons(self, PINK, 20*2+110*1, 10, visual_button_length, visual_button_height, text='Selection Sort')
        self.merge_sort_button = Buttons(self, PINK, 20*3+110*2, 10, visual_button_length, visual_button_height, text='Merge Sort')
        self.quick_sort_button = Buttons(self, PINK, 20*4+110*3, 10, visual_button_length, visual_button_height, text='Quick Sort')
        self.radix_sort_button = Buttons(self, PINK, 20*5+110*4, 10, visual_button_length, visual_button_height, text='Radix Sort')

        # Reset Button
        self.reset_sorting_button = Buttons(self, RED, 20*6+110*5, 10, visual_button_length, visual_button_height, text='Reset')

    def run(self):
        while self.running:
            if self.state == 'main menu':
                self.main_menu()
            if self.state == 'visualize':
                self.visualize_window()
            if self.state == 'execute':
                self.execute_algorithms()
            if self.state == 'sorted':
                self.sorted_window()

        pygame.quit()
        sys.exit()

#################### HELPER FUNCTIONS ####################
    def load(self):
        self.main_menu_background = pygame.image.load('SA_main_background.png')

    ##### Draw Text
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

    def sketch_main_menu(self):
        self.screen.blit(self.main_menu_background, (0, 0))

    def sketch_start_button(self):
        self.start_button.draw_button(SPRINGGREEN)

    def start_button_graphics(self, pos, event):
        if self.start_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'visualize'
            elif event.type == pygame.MOUSEMOTION:
                self.start_button.colour = ALICE
        else:
            self.start_button.colour = SPRINGGREEN

    def sketch_visualize_buttons(self):
        self.bubble_sort_button.draw_button(BLACK)
        self.selection_sort_button.draw_button(BLACK)
        self.merge_sort_button.draw_button(BLACK)
        self.quick_sort_button.draw_button(BLACK)
        self.radix_sort_button.draw_button(BLACK)

    def reset_button_graphics(self, pos, event):
        if self.reset_sorting_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = ''
                self.reset()
            elif event.type == pygame.MOUSEMOTION:
                self.reset_sorting_button.colour = WHITE
        else:
            self.reset_sorting_button.colour = RED

    def button_functions_graphics(self, pos, event):
        if self.bubble_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'bubble sort'
                self.state = 'execute'
            elif event.type == pygame.MOUSEMOTION:
                self.bubble_sort_button.colour = TOMATO

        elif self.selection_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'selection sort'
                self.state = 'execute'
            elif event.type == pygame.MOUSEMOTION:
                self.selection_sort_button.colour = TOMATO

        elif self.merge_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'merge sort'
                self.state = 'execute'
            elif event.type == pygame.MOUSEMOTION:
                self.merge_sort_button.colour = TOMATO

        elif self.quick_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'quick sort'
            elif event.type == pygame.MOUSEMOTION:
                self.quick_sort_button.colour = TOMATO

        elif self.radix_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'radix sort'
            elif event.type == pygame.MOUSEMOTION:
                self.radix_sort_button.colour = TOMATO

        else:
            self.bubble_sort_button.colour, self.selection_sort_button.colour, self.merge_sort_button.colour, \
            self.quick_sort_button.colour, self.radix_sort_button.colour = PINK, PINK, PINK, PINK, PINK

    def visualize_button_selected(self):
        if self.sorting_state == 'bubble sort':
            self.bubble_sort_button.colour = TOMATO
        elif self.sorting_state == 'selection sort':
            self.selection_sort_button.colour = TOMATO
        elif self.sorting_state == 'merge sort':
            self.merge_sort_button.colour = TOMATO
        elif self.sorting_state == 'quick sort':
            self.quick_sort_button.colour = TOMATO
        elif self.sorting_state == 'radix sort':
            self.radix_sort_button.colour = TOMATO

    def draw_data(self, array):
        # Go through randomized array and draw data according to each datum's value
        #print(array)
        for index, datum in enumerate(array):
            pygame.draw.rect(self.screen, NOT_HIGHLIGHTED_DATA, ((2 + 2 * index + 6 * index), 800 - datum, 6, datum))

    def final_data_showcase(self, obj_array):
        # Do the final sweep through the organized data for extra coolness
        for index, datum in enumerate(obj_array):
            pygame.draw.rect(self.screen, SPRINGGREEN, ((2 + 2 * index + 6 * index), 800 - datum, 6, datum))
            pygame.display.update()

    def reset(self):
        # Reset the whole data and introduce a new set of randomized data
        self.state = 'visualize'
        self.data = num_list.copy()
        random.shuffle(self.data)

    #################### EXECUTE FUNCTIONS ####################
    def main_menu(self):
        self.sketch_main_menu()
        self.sketch_start_button()
        self.draw_text('Made By: Seung Jae Yang', self.screen, [530, 750], 28, BLACK, FONT, centered=False)
        pygame.display.update()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.start_button_graphics(pos, event)

    def visualize_window(self):
        pygame.draw.rect(self.screen, WHITE, (0,0,800,800), 0)
        pygame.draw.rect(self.screen, ALICE, (0,0,800,70), 0)
        self.sketch_visualize_buttons()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.button_functions_graphics(pos, event)

        self.visualize_button_selected()

        self.draw_data(self.data)
        pygame.display.update()

    def execute_algorithms(self):
        pos = pygame.mouse.get_pos()
        self.sketch_visualize_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.button_functions_graphics(pos, event)

        if self.sorting_state == 'bubble sort':
            print('bubble')
            # make bubble sort object
            bubble_sort = BubbleSort(self)
            # sort using bubble sort
            bubble_sort.bubblesort(self.data)
            self.final_data_showcase(self.data)
            self.state = 'sorted'

        if self.sorting_state == 'selection sort':
            print('select')
            # make selection sort object
            selection_sort = SelectionSort(self)
            # sort using selection sort
            selection_sort.selectionsort(self.data)
            self.final_data_showcase(self.data)
            self.state = 'sorted'

        if self.sorting_state == 'merge sort':
            print('merge')
            # make merge sort object
            merge_sort = MergeSort(self)
            # sort using merge sort
            # Initialize previous mid actual as 0
            merge_sort.mergesort(self.data, 0)
            self.final_data_showcase(self.data)
            self.state = 'sorted'

    def sorted_window(self):
        # reveal reset button
        self.reset_sorting_button.draw_button(BLACK)
        pygame.display.update()

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.reset_button_graphics(pos, event)




