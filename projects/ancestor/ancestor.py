from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for item in ancestors:
        if item[0] not in graph.vertices and item[1] in graph.vertices:
            graph.add_vertex(item[0])
        elif item[0] in graph.vertices and item[1] not in graph.vertices:
            graph.add_vertex(item[1])
        elif item[0] in graph.vertices and item[1] in graph.vertices:
            pass
        else:
            graph.add_vertex(item[0])
            graph.add_vertex(item[1])

        for item in ancestors:
            graph.add_edge(item[1], item[0])

    visited = graph.bft(starting_node)
    last = visited[-1]
    if last == starting_node:
        return -1
    return last
