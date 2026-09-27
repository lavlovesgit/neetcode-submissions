class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree=[0] * numCourses
        preMap={i: [] for i in range(numCourses)}
        res=[]
        for i, j in prerequisites:
            preMap[j].append(i)
        for i,j in prerequisites:
            indegree[i]+=1
        q=collections.deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        while(q):
            val=q.popleft()
            res.append(val)
            for i in preMap[val]:
                indegree[i]-=1
                
                if indegree[i]==0:
                    q.append(i)
                    

        if len(res) == numCourses:
            return res
        else:
            return [] 
        
        