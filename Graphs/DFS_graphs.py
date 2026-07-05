def dfs_graphs(node,adj,visited,result):
    visited[node]=1
    result.append(node)
    for n in adj[node]:
        if visited[n]==0:
            dfs_graphs(n,adj,visited,result)
        
        
        
number_nodes =8
visited=[0]*(number_nodes+1)
adj=[[],[2,4],[1,3,6],[2],[1,5,7],[4,8],[2],[4,8],[5,7]]
result =[]
dfs_graphs(1,adj,visited,result)
print(result)
"""
                 1
              /     \
             2       4
            / \     / \
           3   6   7  5
                    \ /
                     8
"""
#output:[1, 2, 3, 6, 4, 5, 8, 7]
#TC:o(n)+0(2E)
