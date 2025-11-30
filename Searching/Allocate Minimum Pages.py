class Solution:
    def findPages(self, arr, k):
        # code here
        n = len(arr)
        if k >n:
            return -1
        low=max(arr)
        high=sum(arr)
        result =-1
        while low<=high:
            mid=(low+high)//2
            if self.isPossible(arr,k,mid):
                result=mid
                high=mid-1
            else:
                low=mid+1;
        return result
    def isPossible(self,arr,k,maxPages):
        students =1
        pages=0
        
        for num in arr:
            if pages+num>maxPages:
                students+=1
                pages=num
                if students>k:
                    return False
            else:
                pages+=num
        return True
            