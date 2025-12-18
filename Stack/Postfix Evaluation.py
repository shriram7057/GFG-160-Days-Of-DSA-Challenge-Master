class Solution:
    def evaluatePostfix(self, arr):
        # code here
        st=[]
        for ch in arr:
            if ch.lstrip('-').isdigit():
                st.append(int(ch))
            else:
                b=st.pop()
                a=st.pop()
                if ch =='+':
                    st.append(a+b)
                elif ch =='-':
                    st.append(a-b)
                elif ch == '/':
                    st.append(a//b)
                elif ch =='*':
                    st.append(a*b)
                elif ch=='^':
                    st.append(a**b)
        return st[-1]