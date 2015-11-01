def update_graph_undirected(node, neighbors, graph):
    adjacency_list = graph.get(node, set())
    while neighbors:
        neighbor = neighbors.pop()
        adjacency_list.add(neighbor)
        neighbors_adjacency_list = graph.get(neighbor, set())
        neighbors_adjacency_list.add(node)
        graph[neighbor] = neighbors_adjacency_list
    graph[node] = adjacency_list

def graph_search(graph, start, end=None, do_breadth_first=True):
    '''Produces path generator for the given graph, endpoints, and search type.
    '''
    paths = [[start]]
    visited = []
    while paths:
        path =  paths.pop(0) if do_breadth_first else paths.pop()
        last_node = path[-1]
        if last_node == end:
            yield path
        elif not last_node in visited:
            visited.append(last_node)
        for neighbor in graph.get(last_node, []):
            if neighbor not in path:
                paths.append(path.copy() + [neighbor])
    if end is None:
        yield visited
        
test_graph_one = {}
update_graph_undirected(1, [2, 3, 4], test_graph_one)
update_graph_undirected(3, [5, 6], test_graph_one)
update_graph_undirected(5, [8], test_graph_one)
update_graph_undirected(6, [9, 10, 11], test_graph_one)
update_graph_undirected(4, [7], test_graph_one)
