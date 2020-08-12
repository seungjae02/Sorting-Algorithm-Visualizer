from settings import *
import pygame
import time

class QuickSort:
    def __init__(self, app):
        self.app = app

    def draw_highlight(self, index, array, colour):
        pygame.draw.rect(self.app.screen, colour,
                         ((2 + 8 * index), 800 - array[index], 6, array[index]))

        pygame.display.update()
        time.sleep(0.1)

        # Draw new organized/updated data
        pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                         ((2 + 8 * index), 800 - array[index], 6, array[index]))

    def draw_update(self, index, array, colour, piv=False):
        # For updating pivot points only
        if piv:
            pygame.draw.rect(self.app.screen, colour,
                             ((2 + 8 * index), 800 - array[index], 6, array[index]))

        # For updating non-pivot points
        if not piv:
            pygame.draw.rect(self.app.screen, WHITE, ((2 + 8 * index), 70, 6, 730))
            pygame.draw.rect(self.app.screen, colour,
                             ((2 + 8 * index), 800 - array[index], 6, array[index]))

            pygame.display.update()
            time.sleep(0.1)

            # Draw new organized/updated data
            pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                             ((2 + 8 * index), 800 - array[index], 6, array[index]))



    def partition(self, array, start, end):
        pivot = array[start]
        low = start + 1
        high = end
        self.draw_update(start, array, BLACK, piv=True)

        while True:
            # These two while loops exit when their indexes cross each other, or found the desired value
            while low <= high and array[low] <= pivot:
                self.draw_highlight(low, array, SPRINGGREEN)
                low += 1
            while high >= low and array[high] >= pivot:
                self.draw_highlight(high, array, SPRINGGREEN)
                high -= 1

            # In order to check that the two while actually found a value and not just because their indexes crossed
            # The if statement below is necessary
            if low <= high:
                array[low], array[high] = array[high], array[low]
                self.draw_update(low, array, TOMATO)
                self.draw_update(high, array, ROYALBLUE)

            # If there are no more values to be swapped, then exit the while loop
            else:
                break
        # Once exit out of while loop, switch the low/high number and the pivot number
        # As a result, the pivot number will end up where all the higher values are to the right, and all the lower values
        # are to the left
        array[start], array[high] = array[high], array[start]
        self.draw_update(start, array, TOMATO)
        self.draw_update(high, array, ROYALBLUE)

        return high

    def quicksort(self, array, start, end):
        if start >= end:
            return

        p = self.partition(array, start, end)
        self.quicksort(array, start, p - 1)
        self.quicksort(array, p + 1, end)









