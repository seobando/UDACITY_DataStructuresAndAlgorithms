def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    Returns:
       tuple: (min, max)
    """
    def quicksort(ints):

      if len(ints) <= 1:
          return ints
      
      pivot = ints[len(ints) // 2]
      left = [x for x in ints if x < pivot]
      middle = [x for x in ints if x == pivot]
      right = [x for x in ints if x > pivot]
      
      return quicksort(left) + middle + quicksort(right)

    sorted_ints = quicksort(ints)
    
    return (sorted_ints[0], sorted_ints[-1])
    

# Example Test Case of Ten Integers
import random
## Test Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
## Test Case 2
l = [i for i in range(-10, 0)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((-10, -1) == get_min_max(l)) else "Fail")
## Test Case 3
l = [i for i in range(3, 100)]  # a list containing 0 - 9
random.shuffle(l)

print("Pass" if ((3, 99) == get_min_max(l)) else "Fail")
