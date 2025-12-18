class Solution:
    def decodedString(self, s):
        # code here
        st=[]
        curr = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num=num*10 + int(ch)
            elif ch=='[':
                st.append(curr)
                st.append(num)
                curr = ""
                num=0
            elif ch==']':
                k=st.pop()
                prev=st.pop()
                curr = prev+curr*k
            else:
                curr+=ch
        return curr