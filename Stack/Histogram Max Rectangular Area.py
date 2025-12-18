class Solution:
    def getMaxArea(self, arr):
        # code here
        n=len(arr)
        st=[]
        maxA=0
        for i in range(n+1):
            cur=arr[i] if i < n else 0
            while st and cur <arr[st[-1]]:
                h=arr[st.pop()]
                left=st[-1] if st else -1
                width = i - left - 1
                maxA = max (maxA,h*width)
            st.append(i)
        return maxA