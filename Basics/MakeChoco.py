# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
# Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# make_chocolate(4, 1, 9) → 4
# make_chocolate(4, 1, 10) → -1
# make_chocolate(4, 1, 7) → 2

def make_chocolate(a,b,c):
    small = a;
    big = b * 5
    difference = c - big
    if difference <= small:
        if small - difference == 0:
            return small
        else:
            return small - difference
    else:
        return -1

print( make_chocolate(4, 1, 7))
