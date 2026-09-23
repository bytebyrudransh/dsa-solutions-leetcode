class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
#------------------------------------------------------------------------------------------------------------------------
        n= len(costs)

        i, j = 0, n-1

        pq1 = [] #from left pointer      #MINHEAP BY DEFAULT
        pq2 = [] #from right pointre     #MINHEAP BY DEFAULT
        
        ans = 0 
        for _ in range(k):


            while len(pq1)<candidates and i<=j:
                heapq.heappush(pq1, costs[i])
                i+=1

            while len(pq2)<candidates and i<=j:
                heapq.heappush(pq2, costs[j])
                j-=1
            

            x = pq1[0] if pq1 else 10**14
            y = pq2[0] if pq2 else float("inf")

            if x<=y:        #even if when x==y pick from pq1 cause it might giv one with lower index
                heapq.heappop(pq1) 
                ans +=x
      

            else:
                heapq.heappop(pq2)
                ans+=y
    
        
        return ans
# #------------------------------------------------------------------------------------------------------------------------



#BRUTE FORCE MYSELF -----------------------------------------------------------------------------------------
        n = len(costs)
        ans = 0 
        for _ in range(k):      #O(n)

            temp = []
            i = 0 
            j = len(costs)-1
            for delta in range(candidates):    #O(n)

                if i+delta<len(costs):
                    temp.append((costs[i+delta], i+delta)) # O(1)
                if j-delta>=0:
                    temp.append((costs[j-delta], j-delta)) # O(1)
                # It might do a  redundant work (appending duplicates form both i side and j side,, whenboth i and j will append already added element ),but that wont affect brute force logic correctness, i twll jut make the size o temp increases with some repeated values which will be taken care by the sorting thing below 

            temp.sort()         ##O(m)logm     # m ≈ 2*candidates  ≈ 2*N

            ans +=temp[0][0]
            costs.pop(temp[0][1]) #O(n)    #WE CAN POP ELEMENT FROM ARRAY element by arr.pop(index)  in  #O(n) time
            # because list shifting happens
        
        return ans
#completely valid brute force. total time complexity  O(N*(N+NlogN)) ---> N*N*logN
#------------------------------------------------------------------------------------------------------------------------

