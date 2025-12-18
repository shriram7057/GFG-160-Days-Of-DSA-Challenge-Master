class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        res = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            # Pop elements from stack smaller than or equal to current
            while stack and stack[-1] <= arr[i]:
                stack.pop()
            # If stack is not empty, top is the next greater
            if stack:
                res[i] = stack[-1]
            # Push current element to stack
            stack.append(arr[i])
        
        return res
