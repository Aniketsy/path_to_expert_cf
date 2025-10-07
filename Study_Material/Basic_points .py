###   How to find freq of numbers
freq = {}
for num in nums:
   freq[num] = freq.get(num, 0) + 1

###   How to retrive required value from dict
for key, value in freq.items():
    if value == 1:
        return key


###############
from collections import Counter
freq = Counter(nums)   # Count all numbers efficiently
for num, count in freq.items():
    if count == 1:
         return num
