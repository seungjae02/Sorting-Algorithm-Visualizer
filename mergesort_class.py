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


    def draw_checkpoint(self, start, array):
        # Show checkpoints of sorted groups of data
        for index, datum in enumerate(array):
            pygame.draw.rect(self.app.screen, WHITE, ((2 + 8 * index + 8 * start), 70, 6, 730))
            pygame.draw.rect(self.app.screen, SPRINGGREEN,
                             ((2 + 8 * index + 8 * start), 800 - datum, 6, datum))
            pygame.display.update()

        for index, datum in enumerate(array):
            pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                             ((2 + 8 * index + 8 * start), 800 - datum, 6, datum))


    def mergesort(self, array, curr_start):
        if len(array) > 1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            left_start = curr_start
            right_start = curr_start + mid

            # Recursive call on each half
            self.mergesort(left, left_start)
            self.mergesort(right, right_start)

            # Iterators for traversing for the 2 halves of array
            i = 0
            j = 0

            # Iterator for the main list that I am sorting
            k = 0

            # Merging the arrays back together
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    # Highlight selected datum within array
                    self.draw_sub_update(i, left_start, left, TOMATO)
                    array[k] = left[i]
                    i += 1
                else:
                    # Highlight selected datum within array
                    self.draw_sub_update(j, right_start, right, ROYALBLUE)
                    array[k] = right[j]
                    j += 1
                k += 1

            # Code to catch all the remaining non-appended values in the array
            while i < len(left):
                # Highlight selected datum within array
                self.draw_sub_update(i, left_start, left, TOMATO)
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                # Highlight selected datum within array
                self.draw_sub_update(j, right_start, right, ROYALBLUE)
                array[k] = right[j]
                j += 1
                k += 1
            self.draw_checkpoint(curr_start, array)

