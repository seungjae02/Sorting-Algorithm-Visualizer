import pygame
import sys
from settings import *
from buttons_class import *
from bubblesort_class import *
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

        self.nums = num_list.copy()
        random.shuffle(self.nums)

        self.data_generated = False

        self.data = Data(self, self.nums)

    # Define Buttons
        # Start Button
        self.start_button = Buttons(self, SPRINGGREEN, 300, 620, 200, 70, text='START')
        # Visualize Buttons
        self.bubble_sort_button = Buttons(self, PINK, 20*1+110*0, 10, visual_button_length, visual_button_height, text='Bubble Sort')
        self.selection_sort_button = Buttons(self, PINK, 20*2+110*1, 10, visual_button_length, visual_button_height, text='Selection Sort')
        self.merge_sort_button = Buttons(self, PINK, 20*3+110*2, 10, visual_button_length, visual_button_height, text='Merge Sort')
        self.quick_sort_button = Buttons(self, PINK, 20*4+110*3, 10, visual_button_length, visual_button_height, text='Quick Sort')
        self.radix_sort_button = Buttons(self, PINK, 20*5+110*4, 10, visual_button_length, visual_button_height, text='Radix Sort')
        self.reset_sorting_button = Buttons(self, RED, 20*6+110*5, 10, visual_button_length, visual_button_height, text='RESET')

    def run(self):
        while self.running:
            if self.state == 'main menu':
                self.main_menu()
            if self.state == 'visualize':
                self.visualize_window()
            if self.state == 'execute':
                self.execute_algorithms()
            if self.state == 'sorted':
                pass

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

    def button_functions_graphics(self, pos, event):
        if self.state != 'sorted':
            if self.bubble_sort_button.isOver(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sorting_state = 'bubble sort'
                    self.state = 'execute'
                elif event.type == pygame.MOUSEMOTION:
                    self.bubble_sort_button.colour = TOMATO

            elif self.selection_sort_button.isOver(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sorting_state = 'selection sort'
                elif event.type == pygame.MOUSEMOTION:
                    self.selection_sort_button.colour = TOMATO

            elif self.merge_sort_button.isOver(pos):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.sorting_state = 'merge sort'
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
                self.quick_sort_button.colour, self.radix_sort_button.colour, self.reset_sorting_button = PINK, PINK, PINK, PINK, PINK, RED

        elif self.reset_sorting_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = ''
                self.reset()
            elif event.type == pygame.MOUSEMOTION:
                self.reset_sorting_button = TOMATO

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

    def draw_data(self, obj_array):
        for index, datum in enumerate(obj_array):
            pygame.draw.rect(self.screen, datum.colour, ((2 + 2 * index + 6 * index), 800 - datum.value, 6, datum.value))
        pygame.display.update()

    def final_data_showcase(self, obj_array):
        for index, datum in enumerate(obj_array):
            pygame.draw.rect(self.screen, SPRINGGREEN, ((2 + 2 * index + 6 * index), 800 - datum.value, 6, datum.value))
            pygame.display.update()

    def reset(self):
        self.state = 'visualize'
        self.nums = num_list.copy()
        random.shuffle(self.nums)

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

        if not self.data_generated:
            self.data.generate_data()
            self.data_generated = True

        self.draw_data(self.data.obj_array)

    def execute_algorithms(self):
        pos = pygame.mouse.get_pos()
        self.sketch_visualize_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.button_functions_graphics(pos, event)

        if self.sorting_state == 'bubble sort':
            bubble_sort = BubbleSort(self)
            bubble_sort.sort(self.data.obj_array)
            self.final_data_showcase(self.data.obj_array)
            if bubble_sort.sorted:
                self.state = 'sorted'

    def sorted_window(self):
        pos = pygame.mouse.get_pos()
        self.sketch_visualize_buttons()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.button_functions_graphics(pos, event)



