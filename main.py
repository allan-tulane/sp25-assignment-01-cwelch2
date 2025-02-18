"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
        return x
    else:
        ra = foo(x-1)
        rb = foo(x-2)
        return ra + rb
def longest_run(mylist, key):
    # counts to keep track of overall longest run and the current run
    longestCount = 0
    currentCount = 0
    for n in mylist: # iterate through each element in the list
        if n != key:                            # if the current element is not the key
            if currentCount > longestCount:     # check if the current count is longer than the longest count
                longestCount = currentCount     # if it is, the longest count is now the current count
            currentCount = 0                    # reset current count back to 0 before continuing

        elif n == key:                          # if the current element is equal to the key
            currentCount += 1                   # increment current count by 1

        if currentCount > longestCount:         # final check to check if last sequence is the longest
            longestCount = currentCount

    return longestCount                         # return result


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    

def to_value(v):
    """
    if it is a Result object, return longest_size.
    else return v
    """
    if type(v) == Result:
        return v.longest_size
    else:
        return int(v)

def longest_run_recursive(mylist, key):
    # base case 1: if the list is empty, return a Result with all zeros and false
    if not mylist:
        return Result(0, 0, 0, False)
    # base case 2: if the list has one element, check if it matches the key
    if len(mylist) == 1:
        if mylist[0] == key:
            return Result(1, 1, 1, True)
        else:
            return Result(0, 0, 0, False)

    # split list into two halves for next recursive calls
    midpoint = len(mylist) // 2
    left_result = longest_run_recursive(mylist[:midpoint], key)
    right_result = longest_run_recursive(mylist[midpoint:], key)

    # combine results from both halves to form final result
    # and check if a run of the key spans the boundary between them
    if left_result.is_entire_range and right_result.is_entire_range: # if both halves are entirely the key, the whole list matches the key
        is_entire_range = True
        left_size = len(mylist)     # the left half is part of the key's run
        right_size = len(mylist)    # the right half is part of the key's run
        longest_size = len(mylist)  # the entire list is the longest run
    else:
        is_entire_range = False

        # calculate left_size and right_size for the combined result
        left_size = left_result.left_size
        if left_result.is_entire_range:             # if left half was entirely the key
            left_size += right_result.left_size     # add right half's key run to the left

        right_size = right_result.right_size
        if right_result.is_entire_range:            # if right half was entirely the key
            right_size += left_result.right_size    # add left half's key run to the right

        # Calculate the longest size, including a run that spans the middle
        longest_size = max(left_result.longest_size, right_result.longest_size, left_result.right_size + right_result.left_size)

    # Combine the results into a new Result object and return result
    return Result(left_size, right_size, longest_size, is_entire_range)


