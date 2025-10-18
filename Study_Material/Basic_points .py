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

################## Formula for pythogores theorem
Case 1: n is odd
if n % 2 == 1:
    b = (n * n - 1) // 2
    c = (n * n + 1) // 2


When n is odd, a Pythagorean triple formula is:

(
𝑎
,
𝑏
,
𝑐
)
=
(
𝑛
,
𝑛
2
−
1
2
,
𝑛
2
+
1
2
)
(a,b,c)=(n,
2
n
2
−1
	​

,
2
n
2
+1
	​

)

Case 2: n is even
else:
    k = n // 2
    b = k * k - 1
    c = k * k + 1


When n is even, define k = n / 2. Then the formula is:

(
𝑎
,
𝑏
,
𝑐
)
=
(
𝑛
,
𝑘
2
−
1
,
𝑘
2
+
1
)
(a,b,c)=(n,k
2
−1,k
2
+1)
