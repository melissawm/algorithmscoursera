# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The
# integer in the ith row of the file gives you the ith entry of an input array.

#Your task is to compute the total number of comparisons used to sort the given input file by QuickSort. As you know,
# the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different
# pivoting rules.

#You should not count comparisons one-by-one. Rather, when there is a recursive call on a subarray of length m, you
# should simply add m−1 to your running total of comparisons. (This is because the pivot element is compared to each
# of the other m−1 elements in the subarray in this recursive call.)

#WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can
# give you differing numbers of comparisons. For this problem, you should implement the Partition subroutine exactly
# as it is described in the video lectures (otherwise you might get the wrong answer).

#DIRECTIONS FOR THIS PROBLEM:

#For the first part of the programming assignment, you should always use the first element of the array as the pivot
# element.

from math import floor

def call_quicksort(array, total_comparisons, pivot_choice='first'):
    n = len(array)
    if n <= 1:
        pass
    else:
        if pivot_choice=='first':
            # First case: choose always the first element
            pass
        elif pivot_choice=='last':
            # Second case: choose always the last element
            array[0], array[n-1] = array[n-1], array[0]
        elif pivot_choice=='median':
            # Third case: choose the median of [0], [n] and [n/2]
            choices = [array[0], array[-1], array[floor((n-1)/2)]]
            p = array.index(sorted(choices)[1])
            array[0], array[p] = array[p], array[0]
        pivot = 0
        # Partition the array around p
        i = 1
        for j in range(1,n):
            if array[j] < array[pivot]:
                array[j], array[i] = array[i], array[j]
                i += 1
            elif array[j] > array[pivot]:
                pass
        # Don't forget to move pivot to its rightful position
        array[i-1], array[pivot] = array[pivot], array[i-1]
        total_comparisons = n-1
        # Recursively sort left part
        left_comparisons, array[0:i-1] = call_quicksort(array[0:i-1], 0, pivot_choice)
        total_comparisons += left_comparisons
        # Recursively sort right
        right_comparisons, array[i:] = call_quicksort(array[i:], 0, pivot_choice)
        total_comparisons += right_comparisons

    return total_comparisons, array

if __name__ == "__main__":
    with open("QuickSort.txt", "r") as infile:
        numbers = infile.readlines()
        numbers = [int(item.rstrip(" \n")) for item in numbers]

    total_comparisons, numbers_sorted = call_quicksort(numbers, 0, pivot_choice='median')

    print("Total comparisons = {}".format(total_comparisons))

