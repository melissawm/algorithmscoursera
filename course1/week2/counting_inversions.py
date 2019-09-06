from math import ceil


# Recursive algorithm that counts the total number of inversions in an array
# INPUT: array containing integers in some order
# OUTPUT: number of pairs (i,j) with i<j and array[i]>array[j]

def count_inversions(array):
    n = len(array)
    if n == 1:
        # Base case
        return 0, array
    else:
        # Recursive calls
        half = ceil(n/2)
        left_inv, left_sorted = count_inversions(array[0:half])
        right_inv, right_sorted = count_inversions(array[half:])
        # count_split is a special routine. see below
        split_inv, split_sorted = count_split(left_sorted, right_sorted, n)
        return left_inv+right_inv+split_inv, split_sorted

def count_split(left, right, n):
    # This routine counts the number of split inversions, that is, inversions
    # for which one element is on the left side of the original (upper recursive level)
    # array, and one element is on the right side.
    split = 0
    merged = []
    i = 0
    j = 0
    for k in range(0,n):
        if i == len(left):
            merged = merged+sorted(right[j:])
            j = len(right)
        elif j == len(right):
            merged = merged+sorted(left[i:])
            i = len(left)
        else:
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            elif left[i] > right[j]:
                # We have found a split inversion! This means that
                # all elements in the left array that have not yet
                # been processed are inversions, since they are all
                # larger than the elements on the right array.
                split += len(left)-i
                merged.append(right[j])
                j += 1
    return split, merged

if __name__ == "__main__":
    #with open("smallintegerarray.txt", "r") as infile:
    with open("IntegerArray.txt", "r") as infile:
        numbers = infile.readlines()
        numbers = [int(item.rstrip(" \n")) for item in numbers]

    total_inv, numbers_sorted = count_inversions(numbers)
    print("Total number of inversions: {}".format(total_inv))
