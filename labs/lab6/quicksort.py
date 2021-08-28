import random

PIVOT_FIRST = False
total_count = 0

def quick_sort(alist):
   global total_count
   total_count = 0
   quick_sort_helper(alist,0,len(alist)-1)
   return total_count

def quick_sort_helper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)
       quick_sort_helper(alist,first,splitpoint-1)
       quick_sort_helper(alist,splitpoint+1,last)

def partition(alist,first,last):
   global total_count
   piv_index = first
   if not PIVOT_FIRST: # write code for selecting pivot based on median of 3 (first/mid/last)
      piv_index = median_three(first, last, alist)

   pivotvalue = alist[piv_index]
   alist[piv_index] = alist[first] # move pivot out of the way
   alist[first] = pivotvalue       # by swapping with first element

   leftmark = first+1              # left index
   rightmark = last                # right index

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           total_count += 1
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           total_count += 1
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   alist[first] = alist[rightmark]      # swap pivotvalue and element at rightmark
   alist[rightmark] = pivotvalue

   return rightmark                     # return splitpoint

def median_three(first, last, alist):
    """Returns the index of the median of the first middle and last values"""
    mid = (first + last) // 2
    median = 0
    a = alist[first]
    b = alist[mid]
    c = alist[last]
    if a > b:
        if a < c:
            return first
        elif b > c:
            return mid
        else:
            return last
    else:
        if a > c:
            return first
        elif b < c:
            return mid
        else:
            return last

if __name__ == '__main__':

    n = 800

    my_randoms = random.sample(range(100000), n)
    count = quick_sort(my_randoms)
    print ("n =", n, "Final:", my_randoms, "\n count =", count)

    my_list = list(range(n))
    quick_sort(my_list)
    print ("n =", n, "Final:", my_list, "\n count =", total_count)
