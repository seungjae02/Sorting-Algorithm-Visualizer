from settings import *
import pygame

class BubbleSort:
    def __init__(self, app):
        self.sorted = False
        self.app = app

    def sort(self, array):
        while not self.sorted:
            swap_occurred = False
            for i in range(len(array)-1):
                if array[i].value > array[i+1].value:
                    temp = array[i]
                    array[i] = array[i+1]
                    array[i+1] = temp

                    # Keeps track if sorting action has ever occurred
                    swap_occurred = True

                    # Erase previous data at the position being checked
                pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * i + 6 * i), 70, 6, 730))
                pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * (i+1) + 6 * (i+1)), 70, 6, 730))

                pygame.draw.rect(self.app.screen, SPRINGGREEN, ((2 + 2 * i + 6 * i), 800 - array[i].value, 6, array[i].value))
                pygame.draw.rect(self.app.screen, SPRINGGREEN, ((2 + 2 * (i+1) + 6 * (i+1)), 800 - array[i+1].value, 6, array[i+1].value))
                pygame.display.update()

                pygame.draw.rect(self.app.screen, TAN,
                                 ((2 + 2 * i + 6 * i), 800 - array[i].value, 6, array[i].value))
                pygame.draw.rect(self.app.screen, TAN,
                                 ((2 + 2 * (i + 1) + 6 * (i + 1)), 800 - array[i + 1].value, 6, array[i + 1].value))


            if not swap_occurred:
                self.sorted = True

        pygame.display.update()




