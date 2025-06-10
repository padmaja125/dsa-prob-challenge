# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# cat_dog('catdog') → True
# cat_dog('catcat') → False
# cat_dog('1cat1cadodog') → True

def cat_dog(strs):
    catCount = 0
    dogCount = 0
    x = 0
    while x < len(strs):
        if strs[x] == 'c':
            if strs[x+1] == 'a':
                if strs[x+2] == 't':
                    x = x+2
                    catCount += 1
        if strs[x] == 'd':
            if strs[x+1] == 'o':
                if strs[x+2] == 'g':
                    x = x+2
                    dogCount += 1
        x += 1
    return catCount == dogCount

print(cat_dog('1cat1cadodog'))



