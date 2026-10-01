class Solution:
    def kthDigit(self, k: int) -> int:
        
        d = 1
        while True:
            tmp = (10**(d-1)) * 9 * d
            if tmp >= k:
                break
            k = k - tmp
            d += 1
        # At this point k is between 2 powers of 10
        for i in range(9):
            tmp = (10**(d-1)) * d
            if tmp >= k:
                break
            k = k - tmp
        # At this point k is between 2 multiples of that integer size
        div = math.floor((k-1)/d)
        rem = k%d
        # Find kth digit
        tmp = (10**(d-1))*(i+1) + div
        # To reverse it or not to reverse it
        rev = (tmp//10)%2
        last = abs((tmp%10) - 9) if rev else tmp%10
        tmp = str(tmp)[:-1] + str(last)
        return int(tmp[rem-1])

