def getIslands(graph):
    visited = set()
    islands = 0

    def getConnections(y, x):
        try:
            east = graph[y][x + 1]
        except:
            east = 0
        try:
            south = graph[y + 1][x]
        except:
            south = 0
        try:
            west = graph[y][x - 1]
        except:
            west = 0
        try:
            north = graph[y - 1][x]
        except:
            west = 0
        visited.add((y, x))
        # check east
        if east == 1 and (y, x + 1) not in visited:
            getConnections(y, x + 1)
        # check south
        if south == 1 and (y + 1, x) not in visited:
            getConnections(y + 1, x)
        # check west
        if west == 1 and (y, x - 1) not in visited:
            getConnections(y, x - 1)
        # check north
        if north == 1 and (y - 1, x) not in visited:
            getConnections(y - 1, x)
    for yIndex, array in enumerate(graph):
        for xIndex, island in enumerate(array):
            # check if coord ahs not been visited and coord has land
            if (yIndex, xIndex) not in visited and island != 0:
                # add islands
                islands += 1
                getConnections(yIndex, xIndex)
    return islands
