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

################## Formula for pythogores theorem, if we have given n that is a
Case 1: n is odd
if n % 2 == 1:
    b = (n * n - 1) // 2
    c = (n * n + 1) // 2

Case 2: n is even
else:
    k = n // 2
    b = k * k - 1
    c = k * k + 1
