import random
import time
# Implementation of binary search algorithm!!

# We will prove that binary search is faster than naive search!

# naive search: snan entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1 



def naive_search(l, target):
    # example l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    # example l = [1, 3, 5, 10, 12]  # should return 3
    midpoint = (low + high) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoiint]
        #print(f"L={l},Targ= {target}, midpoint + 1= {midpoint + 1}, high= {high}")
        return binary_search(l, target, midpoint + 1, high)
    
if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))

    lenght = 70000
    # build a sorted list of length 1000
    list_sorted = set()
    while len(list_sorted) < lenght:
        list_sorted.add(random.randint(-3*lenght, 3*lenght))
    list_sorted = sorted(list(list_sorted))

    start = time.time()
    for target in list_sorted:
        naive_search(list_sorted, target)
    end = time.time()
    naiv_time = (end - start) / lenght
    print("Naive search time: ", naiv_time, "seconds" )
    print("Naive serch time: ", naiv_time * 60, "minutes")

    start = time.time()
    for target in list_sorted:
        binary_search(list_sorted, target)
    end = time.time()
    bin_time = (end - start) / lenght
    print("Binary search time: ", bin_time, "seconds")
    print("Binary serch time: ", bin_time * 60, "minutes")

    print()
    print(naiv_time > bin_time)
    print(f"Binary search time is : {naiv_time - bin_time} seconds faster")