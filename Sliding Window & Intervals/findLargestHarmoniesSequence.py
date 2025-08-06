# Consider a scenario where a harmonious sequence is defined as a sequence extracted from a given array of integers, 'nums', where the highest value minus the lowest value equals exactly 1.
# Your task is to find the length of the longest such harmonious subsequence within 'nums'.
# Remember, a subsequence can be formed by eliminating zero or more elements from 'nums' without altering the order of the remaining elements.
 
# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3], which has a length of 5.
 
# Example 2:
# Input: nums = [1,2,3,4]
# Output: 2
 
# Example 3:
# Input: nums = [1,1,1,1]
# Output: 0
 
# Constraints:
# - The length of array 'nums' is at least 1 and at most 20,000.
# - The values of elements in 'nums' range between -1,000,000,000 and 1,000,000,000.

def findLargestHarmoniousSubsequence(nums):
    # create empty dict 
    c = {}
    for num in nums:
        # c[num] will through error as keyerror if key not present
        c[num] = c.get(num, 0) + 1
    # now try to find max value
    
    max_value = 0
    for key in c:
        if (key + 1) in c:
            max_value = max(max_value, c[key] + c[key + 1])
    return max_value


print(findLargestHarmoniousSubsequence([1, 3, 2, 2, 5, 2, 3, 7]))