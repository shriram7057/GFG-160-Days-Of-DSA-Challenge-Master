
class Solution:
    def maxLength(self, s):
        # code here
        st=[-1]
        ans=0
        for i , ch in enumerate(s):
            if ch=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    ans=max(ans,i-st[-1])
        return ans 