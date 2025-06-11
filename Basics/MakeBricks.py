# We want to make a row of bricks that is goal inches long. 
# We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Return True if it is possible to make the goal by choosing from the given bricks. 

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True


def make_bricks(a,b,c):
    small = a 
    big = b * 5
    target = c
    return target <= small + big


print(make_bricks(3, 1, 9))