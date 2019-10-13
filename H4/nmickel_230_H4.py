# ------------------------------------------------------------------------------
# Name: Nathaniel Mickel
# Homework 4
# Due Date: /9/2019
# -----------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# -----------------------------------------------------------------------------
# Refernces: Homework 4 Guidelines
# -----------------------------------------------------------------------------
# Comments: N/A
# -----------------------------------------------------------------------------
# NOTE: width of the source code should be <= 80 characters readable on-screen.
# 23456789012345678901234567890123456789012345678901234567890123456789012345678
#     10      20    30      40    50      60    70     80
# -----------------------------------------------------------------------------


def deep_copy(some_2d_list):
    result = []
    # start with a fresh list
    for lst in some_2d_list:
        one = []
        # new list to be sorted
        for element in lst:
            one.append(element)
            # add element to one
        result.append(one)
        # add one to result
    return result


def transform(data, num_rows, num_cols):
    check = num_rows * num_cols
    l_len = len(data)
    final = []
    if check == l_len:
        k = 0
        for e in range(num_rows):
            sub = []
            for j in range(num_cols):
                sub.append(data[k])
                k = k + 1
            final.append(sub)
    elif l_len > check:
        final = []
    else:
        for i in range(l_len, check):
            data.append(0)
        k = 0
        for i in range(num_rows):
            sub = []
            for j in range(num_cols):
                sub.append(data[k])
                k = k + 1
            final.append(sub)
    return final


def gravitate(nums, direction):
    if direction == "right":
        for enum in range(len(nums)):
            for j in range(len(nums[enum])-1):
                nums[enum][j+1] = nums[enum][j+1]+nums[enum][j]
                # Adds the value of current element to the element on the right
                # and stores it in right
                nums[enum][j] = 0
                # Assigns 0 to the current element
    else:
        for enum in range(len(nums)):
            for j in range(len(nums[enum])-1, 0, -1):
                nums[enum][j-1] = nums[enum][j-1]+nums[enum][j]
                # Adds the value of current element to the element on the left
                # and stores it in left
                nums[enum][j] = 0
    return nums


def word_search(puzzle, words):
    final = []
    # Initialisation of final result array
    for search in range(len(words)):
        # We will check for every word in words
        # if there exists a jumbled word containing that word
        sort_one = sorted(words[search])
        # s is an array of characters in words[i] which is sorted
        signal = 0
        # signal corresponds whether a word existing
        while signal == 0:
            # this while loop runs until the correct word is found
            # or until all the words in jumbled are covered
            for jumbled in puzzle:
                # Check for every jumbled word in puzzle array
                sort_two = sorted(jumbled)
                # s1 is array of characters in jumbled, which is sorted
                if all(x in sort_two for x in sort_one):
                    # Checks if s1 contains all elements of s
                    signal = 1
                    # Signal is set to 1 if check condition returns true
                    final.append(words[search])
                    # Add the word to final list to be returned
                    break
            break
    return final
