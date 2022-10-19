
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        #node(v) is passed to colorDfs() to explore its neighbor nodes
        def colorDfs(v):
            
            for nbr in graph[v]:
                
                 #if the neighbor is colored and color of neighbor is same that of the 'v', return false as adjacent nodes can't have same color
                if nbr in color:
                    if color[nbr] == color[v]:
                        return False
                
                #color the neighbor with different color than that of 'v'
                else:
                    color[nbr] = 1 - color[v]
                    
                    #apply the dfs on the neighbor too such that we can explore its neighbors too
                    #Again if coloring failed, the colorDfs() returns false then graph gets terminated
                    if not colorDfs(nbr):
                        return False
                    
            #True is returned iff no two adjacent nodes didn't have same color
            return True
                    
                
            
            
        
        
        color = {}
        
        #Take the starting vertex and apply dfs
        for v in range(len(graph)):
            
            #if the given vertex is not at all colored,color it
            if v not in color:
                color[v] = 0
                
                #if coloring failed, the colorDfs() returns false then graph gets terminated
                if not colorDfs(v):
                    return False
        
        #if graph is bipartite
        return True
            
                
                
            
        