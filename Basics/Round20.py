# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more. 
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values.

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

def round_sum(a,b,c):
    a = ( a // 10)*10 + 10 if a % 10 > 5 else (a // 10)*10   
        
    b =(b // 10)*10 + 10  if b %10 > 5 else (b // 10)*10 
    c = (c // 10 )*10+ 10 if c%10 > 5 else (c // 10 )*10 


       
    
    sum = a + b + c
    return sum

print(round_sum(12, 13, 14))