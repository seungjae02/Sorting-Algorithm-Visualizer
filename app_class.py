import pygame
import sys
from settings import *
from buttons_class import *

pygame.init()

class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'main menu'
        self.sorting_state = ''
        self.load()

    # Define Buttons
        # Start Button
        self.start_button = Buttons(self, SPRINGGREEN, 300, 620, 200, 70, text='START')
        # Visualize Buttons
        self.bubble_sort_button = Buttons(self, PINK, 10, 10, 148, 50, text='Bubble Sort')
        self.selection_sort_button = Buttons(self, PINK, 168, 10, 148, 50, text='Selection Sort')
        self.merge_sort_button = Buttons(self, PINK, 326, 10, 148, 50, text='Merge Sort')
        self.quick_sort_button = Buttons(self, PINK, 484, 10, 148, 50, text='Quick Sort')
        self.radix_sort_button = Buttons(self, PINK, 642, 10, 148, 50, text='Radix Sort')

    def run(self):
        while self.running:
            if self.state == 'main menu':
                self.main_menu()
            if self.state == 'visualize':
                self.visualize_window()

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

    def visualize_buttons_graphics(self, pos, event):
        if self.bubble_sort_button.isOver(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sorting_state = 'bubble sort'
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
            self.quick_sort_button.colour, self.radix_sort_button.colour = PINK,PINK,PINK,PINK,PINK

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
            self.visualize_buttons_graphics(pos, event)

        self.visualize_button_selected()
        pygame.display.update()

    def execute_algorithms(self):
        pass
