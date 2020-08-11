from settings import *
import pygame
import time

class MergeSort:
    def __init__(self, app):
        self.app = app

    def draw_sub_update(self, index, start, array, colour):
        pygame.draw.rect(self.app.screen, colour,
                         ((2 + 8 * index + 8 * start), 800 - array[index], 6, array[index]))

        pygame.display.update()

        # Draw new organized/updated data
        pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                         ((2 + 8 * index + 8 * start), 800 - array[index], 6, array[index]))
        time.sleep(2)


    def draw_checkpoint(self, start, array):
        # Show checkpoints of sorted groups of data
        for index, datum in enumerate(array):
            pygame.draw.rect(self.app.screen, WHITE,
                             ((2 + 8 * index + 8 * start), 800 - datum, 6, datum))

        for index, datum in enumerate(array):
            pygame.draw.rect(self.app.screen, SPRINGGREEN,
                             ((2 + 8 * index + 8 * start), 800 - datum, 6, datum))
            pygame.display.update()

        for index, datum in enumerate(array):
            pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                             ((2 + 8 * index + 8 * start), 800 - datum, 6, datum))


    def mergesort(self, array, previous_mid_actual, previous_start):
        if len(array) > 1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            if previous_start == 0 and previous_mid_actual == 0:
                left_start = 0
                right_start = 0
                left_ma = right_ma = mid
            else:
                left_ma = previous_mid_actual - mid
                right_ma = previous_mid_actual + mid
                left_start = left_ma - mid
                right_start = previous_mid_actual

            # Recursive call on each half
            self.mergesort(left, left_ma, left_start)
            self.mergesort(right, right_ma, right_start)

            # Iterators for traversing for the 2 halves of array
            i = 0
            j = 0

            # Iterator for the main list that I am sorting
            k = 0

            # Merging the arrays back together
            while i < len(left) and j < len(right):
                # [1] is added so the code reads the values
                if left[i] < right[j]:
                    array[k] = left[i]
                    self.draw_sub_update(i, left_start, left, TOMATO)
                    i += 1
                else:
                    array[k] = right[j]
                    self.draw_sub_update(j, right_start, right, ROYALBLUE)
                    j += 1
                k += 1

            # Code to catch all the remaining not-appended values in the array
            while i < len(left):
                array[k] = left[i]
                self.draw_sub_update(i, left_start, left, TOMATO)
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                self.draw_sub_update(j, right_start, right, ROYALBLUE)
                j += 1
                k += 1
            self.draw_checkpoint(previous_start, array)

#print('before:', yeet)
#thing = MergeSort(None)
#thing.mergesort(yeet)
#print('after:', yeet)

