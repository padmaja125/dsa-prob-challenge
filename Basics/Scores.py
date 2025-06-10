# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true

def scoresClump(lis):
    x = 0
    while(x+2 < len(lis)):
        if((lis[x]-lis[x+1]) == (lis[x+1] - lis[x+2])):
            x = x+2
        else:
            return False
    return True
        
print(scoresClump([3, 4, 6]))

