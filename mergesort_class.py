from settings import *
import pygame
import time
yeet = num_list.copy()

class MergeSort:
    def __init__(self, app):
        self.app = app
        self.sorted = False

    def draw_update(self, datum1, datum2, array):
        pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * datum1 + 6 * datum1), 70, 6, 730))
        pygame.draw.rect(self.app.screen, WHITE, ((2 + 2 * datum2 + 6 * datum2), 70, 6, 730))

        pygame.draw.rect(self.app.screen, SPRINGGREEN,
                         ((2 + 2 * datum1 + 6 * datum1), 800 - array[datum1], 6, array[datum1]))
        pygame.draw.rect(self.app.screen, SPRINGGREEN,
                         ((2 + 2 * datum2 + 6 * datum2), 800 - array[datum2], 6, array[datum2]))
        pygame.display.update()

        # Draw new organized/updated data
        pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                         ((2 + 2 * datum1 + 6 * datum1), 800 - array[datum1], 6, array[datum1]))
        pygame.draw.rect(self.app.screen, NOT_HIGHLIGHTED_DATA,
                         ((2 + 2 * datum2 + 6 * datum2), 800 - array[datum2], 6, array[datum2]))

    def mergesort(self, array):
        
        if len(array) > 1:
            mid = len(array)//2
            left = array[:mid]
            right = array[mid:]

            # Recursive call on each half
            self.mergesort(left)
            self.mergesort(right)

            # Iterators for traversing for the 2 halves of array
            i = 0
            j = 0

            # Iterator for the main list that I am sorting
            k = 0

            # Merging the arrays back together
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    self.draw_update(i, j, array)

                    i += 1
                else:
                    array[k] = right[j]
                    self.draw_update(i, j, array)

                    j += 1
                k += 1

                time.sleep(0.01)

            # Code to catch all the remaining not-appended values in the array
            while i < len(left):
                array[k] = left[i]
                self.draw_update(i, j, array)
                i += 1
                k += 1
                time.sleep(0.01)

            while j < len(right):
                array[k] = right[j]
                self.draw_update(i, j, array)
                j += 1
                k += 1
                time.sleep(0.01)

#print('before:', yeet)
#thing = MergeSort(None)
#thing.mergesort(yeet)
#print('after:', yeet)


[1,2,3,4,5,6]

