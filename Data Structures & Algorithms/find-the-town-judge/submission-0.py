class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming=[0] * (n+1)
        outgoing=[0] * (n+1)
        for i,j in trust:
            outgoing[i]+=1
            incoming[j]+=1
        print(outgoing)
        print(incoming)
        for i in range(1,n+1):
            if incoming[i]==n-1 and outgoing[i]==0:
                return i
        return -1
        
            




        