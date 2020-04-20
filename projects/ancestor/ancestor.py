from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        graph.add_vertex(parent)
        graph.add_vertex(child)
        graph.add_edge(child, parent)

    path_result = graph.dft(starting_node)

    if len(path_result) == 1:
        return -1
    else:
        return path_result[-1]
