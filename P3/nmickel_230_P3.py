# ------------------------------------------------------------------------------
# Name: Nathaniel Mickel
# Project 3
# Due Date: 6/10/2019
# -----------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
# -----------------------------------------------------------------------------
# Refernces: Project 3 Guidelines
# -----------------------------------------------------------------------------
# Comments: N/A
# -----------------------------------------------------------------------------
# NOTE: width of the source code should be <= 80 characters readable on-screen.
# 23456789012345678901234567890123456789012345678901234567890123456789012345678
# 		10		  20		30		  40		50		  60		70		 80
# -----------------------------------------------------------------------------
def how_odd(n):
    count = 0
    while n % 2 == 1:
        count += 1
        n = int(n / 2)
    return count

def vibrate(n):
    count = 0
    while n != 1:
        if n % 2 == 1:
            n = int(n / 3)
        else:
            n = int(n * 4 / 3) + 1
        count += 1
    return count

def biggest_combustible(names, sizes, combustibles):
    biggest_size = None
    biggest_item = None
    for combustible in combustibles:
        if combustible in names:
            index = names.index(combustible)
            if biggest_size is None:
                biggest_size = sizes[index]
                biggest_item = combustible
            elif sizes[index] > biggest_size:
                biggest_item = combustible
                biggest_size = sizes[index]
    return biggest_item

def is_combustible(name, combustibles):
    for combustible in combustibles:
        if name == combustible:
            return True
    return False

def any_oversized(sizes, maximum):
    for num in sizes:
        if num > maximum:
            return True
    return False

def any_adjacent_combustibles(names, combustibles):
    for i in range(len(names) - 1):
        # Check if two consecutive names are in the combustible list
        if names[i] in combustibles and names[i + 1] in combustibles:
            return True
    return False

def get_combustibles(names, combustibles):
    clist = []
    for name in names:
        # if the name is in the combustibles list, append the name in list
        if name in combustibles:
            clist.append(name)
    return clist

def cheap_products(names, prices, limit):
    plist = []
    idx = 0
    for price in prices:
        # check if price at index is within the limit
        if prices[idx] <= limit:
            # append the name if within limit
            plist.append(names[idx])
            # increment the index
            idx = idx + 1
    return plist
def box_sort(names, sizes):