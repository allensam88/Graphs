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
        graph.add_edge(item[1], item[0])

    # for item in ancestors:

    # for pair in ancestors:
    #     parent = pair[0]
    #     child = pair[1]
    #     graph.add_vertex(parent)
    #     graph.add_vertex(child)
    #     graph.add_edge(child, parent)

    visited = graph.bft(starting_node)
    last = visited[-1]
    if last == starting_node:
        return -1
    return last
