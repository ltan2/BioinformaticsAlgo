def bipartite_graph(num_graphs, edges_representation):
    res = []
    for i in range(0,num_graphs):
        two_color_possible = two_color(edges_representation[i])
        if two_color_possible == True:
            res.append(1)
        else:
            res.append(-1)
    return res

def two_color(edges_representation):
    num_vertices, adj_vertices = count_vertices(edges_representation)
    nodes_color = [-1] * num_vertices # mark as uncolored

    for vertex in adj_vertices.keys():
        if nodes_color[vertex-1] == -1: # not colored
            #color it
            nodes_color[vertex-1] = 0
            for node in adj_vertices[vertex]:
                # check if nodes are colored.
                if nodes_color[node-1] == -1:
                    nodes_color[node-1] = 1 # assign alternate color
                elif nodes_color[node-1] == 0:
                    return False
    return True
        

def count_vertices(edges_representation):
    map_adj = {}
    unique_nodes = 0
    for edge in edges_representation:
        if edge[0] in map_adj:
            map_adj[edge[0]].append(edge[1])
        else:
            map_adj[edge[0]] = [edge[1]]
            unique_nodes += 1
        if edge[1] in map_adj:
            map_adj[edge[1]].append(edge[0])
        else:
            map_adj[edge[1]] = [edge[0]]
            unique_nodes += 1

    return unique_nodes, map_adj

res = bipartite_graph(2,[[[3,3],[1,2],[3,2],[3,1]],[[4,3],[1,4],[3,1],[1,2]]])
print(res)

