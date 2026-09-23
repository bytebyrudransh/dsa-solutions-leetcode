def reverse_x(x):
    res = 0
    while(x):
        res = res * 10 + x % 10
        x //= 10
    return res


ans = []
for i in range(1, 10 ** 5):
    rev = reverse_x(i)

    e = i * (pow(10, len(str(i)) )) + rev #for even length just adding rev value
    if e <= 10 ** 9:
        ans.append(e)
    
    rev = reverse_x(i // 10) #removing last digit(in half it becomes the middle one) and passing to get reverse
    o = i * (pow(10, len(str(i)) - 1 )) + rev 

    if o <= pow(10, 9):
        ans.append(o)

w = sorted(ans)

even = []
odd = []
for i in w:
    if i & 1 == 0:
        even.append(i) #even ± 2 = even so even val in nums compare with this
    else:
        odd.append(i) #odd ± 2 = odd so odd val in nums compare with this

import bisect
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res =  0
        
        for i in nums:
            if i & 1 == 0:
                idx = bisect.bisect_right(even, i) #idx of first even palindrome greater than i
                
                if 1 <= idx < len(even): #idx in range so both left and right exist, take min
                    x, y = i - even[idx - 1], even[idx] - i
                    res += min(x // 2, y // 2)
                
                elif idx == 0: #idx at start so no left, only right exists
                    res += (even[idx] - i) // 2
                
                elif idx == len(even): #idx at end so no right, only left exists
                    res += (i - even[idx - 1]) // 2
                
            else:
                idx1 = bisect.bisect_right(odd, i) #idx of first odd palindrome greater than i
                
                if 1 <= idx1 < len(odd): #idx in range so both left and right exist, take min
                    x, y = i - odd[idx1 - 1], odd[idx1] - i
                    res += min(x // 2, y // 2)

                elif idx1 == 0: #idx at start so no left, only right exists
                    res += (odd[idx1] - i) // 2

                elif idx1 == len(odd): #idx at end so no right, only left exists
                    res += (i - odd[idx1 - 1]) // 2

        return res