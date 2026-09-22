class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            adj=[]
            for i in range(n):
                adj.append([])
            for i,j in edges:
                adj[i].append(j)
                adj[j].append(i)
            # end of creating an adj matrix 
            print(adj)
            visited=[0] * n
            def rec(node,par):
                visited[node]=1
                for i in adj[node]:
                    if visited[i]==1 and par!=i:
                        return False
                    if visited[i]==0:
                       if not rec(i,node):
                        return False

                return True
                        
            
            # Check for cycle
            if not rec(0, -1):
                return False

            # Check that every node is connected
            return all(visited)
        
    

    
    
   
        
        