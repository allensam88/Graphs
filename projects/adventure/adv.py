from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from traversal_graph import TraversalGraph

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

visited = TraversalGraph()

reversal_stack = []
reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# initialize starting room
visited.add_room(player.current_room.id, player.current_room.get_exits())

# run until the number of visited rooms equals the number of rooms in the maze
while len(visited.rooms) < len(room_graph):
    # assign initial variables
    current_room = player.current_room.id
    exits = player.current_room.get_exits()

    # sift thru exits and find an unexplored direction (?)
    direction = visited.pick_direction(current_room, exits)

    # if unexplored directions (?)
    if direction:
        # save the current_room as the previous room, then travel to next room
        prev_room = current_room
        player.travel(direction)

        # update the traversal path & reversal stack
        traversal_path.append(direction)
        reversal_stack.append(reverse[direction])

        # get the new room & exits
        new_room = player.current_room.id
        new_exits = player.current_room.get_exits()

        # add the new room if player has been there before
        if new_room not in visited.rooms:
            visited.add_room(new_room, new_exits)

        # connect the new room to the previous room
        visited.add_connection(new_room, prev_room,
                               direction, reverse[direction])

    # else reached a dead end or all exit directions have been explored
    else:
        reversal = reversal_stack.pop()
        player.travel(reversal)
        traversal_path.append(reversal)

    # print('Traversal Path: ', traversal_path)
    # print('Visited Rooms: ', visited.rooms)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
