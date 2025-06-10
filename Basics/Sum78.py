# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(val):
    sum = 0
    boolv = False
    for x in val:
        if(x == 7 ):
            boolv = True
            continue 
        if(boolv == True and x == 8):
            boolv = False
            continue
        if(boolv == False and x != 7):
            sum += x
    return sum


print(sum78([1,1,7,8,2]))