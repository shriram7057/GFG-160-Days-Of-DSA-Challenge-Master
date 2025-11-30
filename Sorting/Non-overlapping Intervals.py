class Solution:
    def minRemoval(self, intervals):
        # code here
        intervals.sort(key=lambda x:x[1])
        count=0
        prev_end=float('-inf')
        
        for interval in intervals:
            if interval[0]>=prev_end:
                prev_end=interval[1]
            else:
                count +=1
        return count