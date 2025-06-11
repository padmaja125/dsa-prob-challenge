# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(arr):
    newArr = []
    for i in arr:
        x = i *2
        if x%10 == 2:
            continue
        else:
            newArr.append(x)
    return newArr

## [i * 2 for i in arr if (i * 2) % 10 != 2]

print(two2([1, 2, 3]))