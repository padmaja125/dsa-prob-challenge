# Given an input string, return the number of times that the string "code" appears anywhere in the string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2
def count_code(strs):
    count = 0
    x = 0
    while x < len(strs):
        if strs[x] == 'c':
            if strs[x+1] == 'o':
                if strs[x+3] == 'e':
                    count +=1
                    x = x+3
        x += 1
    return count

print(count_code('cozexxcope'))
        
