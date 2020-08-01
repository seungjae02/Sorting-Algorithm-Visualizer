from settings import *
import pygame
import time

class SelectionSort:
    def __init__(self, app):
        self.app = app
        self.sorted = False

# Summary of Selection Sort: Sweep through data, select smallest values found and start making a stack of data going from smallest to biggest (left to right)
    def selectionsort(self, array):
        for i in range(len(array)):
            min_index = i
            for j in range(i+1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

            # Erase previous data at the position being checked
            pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * min_index + 6 * min_index), 70, 6, 730))
            pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * i + 6 * i), 70, 6, 730))

            # Draw new organized/updated data
            pygame.draw.rect(self.app.screen, SPRINGGREEN, ((2 + 2 * min_index + 6 * min_index), 800 - array[min_index], 6, array[min_index]))
            pygame.draw.rect(self.app.screen, SPRINGGREEN,
                             ((2 + 2 * i + 6 * i), 800 - array[i], 6, array[i]))
            pygame.display.update()

            pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA, ((2 + 2 * min_index + 6 * min_index), 800 - array[min_index], 6, array[min_index]))
            pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                             ((2 + 2 * i + 6 * i), 800 - array[i], 6, array[i]))

            time.sleep(0.1)


