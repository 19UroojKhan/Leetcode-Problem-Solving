class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #approach 1 : sc=O(1), tc=O(n)
        # l=0 
        # r=len(s)-1 

        # while l<r:
        #     s[l],s[r]=s[r],s[l]
        #     l=l+1 
        #     r=r-1 
        #approach 2: tc.sc=O(n)
        stack=[] 
        for c in s: 
            stack.append(c)
        i=0 
        while stack:
            s[i]=stack.pop()
            i+=1 

        #take exyta scpace -O(n)
        