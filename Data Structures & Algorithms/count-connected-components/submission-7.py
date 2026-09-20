class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(adj,start,visited):
            def rec(node):
                visited[node]=1
                for i in adj[node]:
                    if visited[i]==0:
                        rec(i)
            rec(start)
                        
            return visited
        # creating an adj matrix
        adj=[]
        for i in range(n):
            adj.append([])
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        # end of creating an adj matrix 
        print(adj)       
        visited=dfs(adj,0,[0] * len(adj))
        calls=1
        for i in range(len(visited)):
            if visited[i]==0:
                calls=calls+1
                visited=dfs(adj,i,visited)
                print(visited)
            
        

        
        
        return calls
        
        


        