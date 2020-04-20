import random


class TraversalGraph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, new_room, exits):
        self.rooms[new_room] = {}
        for exit in exits:
            self.rooms[new_room][exit] = '?'

    def add_connection(self, current_room, previous_room, direction, reverse_direction):
        self.rooms[current_room][reverse_direction] = previous_room
        self.rooms[previous_room][direction] = current_room

    def pick_direction(self, current_room, exits):
        # find the next unexplored direction (?)
        for direction in exits:
            if self.rooms[current_room][direction] == '?':
                return direction
