import random
import time

def selection_sort(alist):
    comparisons = 0
    for i in range(len(alist) - 1):
        max = 0
        for j in range(1, len(alist) - i):
            comparisons += 1
            if alist[max] <= alist[j]:
                max = j
        alist[len(alist) - 1 - i], alist[max] = alist[max], alist[len(alist) - 1 - i]
    return comparisons

def insertion_sort(alist):
    comparisons = 0
    for i in range(1, len(alist)):
        curr = alist[i]
        while i > 0 and curr < alist[i-1]:
            comparisons += 1
            alist[i] = alist[i-1]
            i -= 1
        if i > 0:
            comparisons += 1
        alist[i] = curr
    return comparisons


def main():

    for num in [100000]:
        random.seed(1234)
        randoms = random.sample(range(1000000), num)  # Generate num random numbers from 0 to 999,999
        start_time = time.time()
        comps = selection_sort(randoms)
        stop_time = time.time()
        print("n:", num, "- comps:", comps, "- time:", stop_time - start_time)

if __name__ == '__main__': 
    main()
