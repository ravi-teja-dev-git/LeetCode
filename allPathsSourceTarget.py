class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #resultant array to store paths
        finPaths = []
        
        def pathGraph(start,path):
            
            #if start(node) is the last node in path             
            if start == len(graph) -1:
                #append the path into the resultant finPath
                finPaths.append(path)
            
            #traverse all the neighbor nodes of the starting node
            for neighbor in graph[start]:
                #applying depth first search to find the path, passing the traversed path with current neighbor
                pathGraph(neighbor,[*path,neighbor])
                
        #pass the starting node and initialize the path with 0 as every path starts at 0         
        pathGraph(0,path = [0])
        
        return finPaths
                
                
        