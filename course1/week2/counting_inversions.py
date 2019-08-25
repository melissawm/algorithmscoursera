from math import ceil


def count_inversions(array):
    n = len(array)
    if n == 1:
        return 0, array
    else:
        half = ceil(n/2)
        left_inv, left_sorted = count_inversions(array[0:half])
        right_inv, right_sorted = count_inversions(array[half:])
        split_inv, split_sorted = count_split(left_sorted, right_sorted, n)
        return left_inv+right_inv+split_inv, split_sorted

def count_split(left, right, n):
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
    if total_inv == 2407905288:
        print("Ok!")
    else:
        print("Wrong!")
