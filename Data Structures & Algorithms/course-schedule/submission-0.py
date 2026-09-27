class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap={i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        print(preMap)

        #cycle detetion
        visited=[0] * numCourses

        def rec(x):
            visited[x]=1
            for i in preMap[x]:
                if visited[i]==0:
                    if rec(i):
                        return True
                    
                if visited[i]==1:
                    return True
            visited[x]=2
            return False
        for i in range(numCourses):
            if visited[i] == 0:
                if rec(i):
                    return False
        return True
            

                
        


        



        