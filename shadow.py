import sys
import math
from enum import Enum


def err(message) -> None:
    print(message, file=sys.stderr, flush=True)


class Distance(Enum):
    UNKNOWN = "UNKNOWN"
    COLDER = "COLDER"
    WARMER = "WARMER"
    SAME = "SAME"


class Tile:
    def __init__(self, x: int, y: int, visited: bool = False):
        self.x = x
        self.y = y
        self.visited = self.visited

    def __eq__(self, other):
        assert isinstance(other, Tile)
        return self.x == self.x and self.y == other.y

    def __repr__(self):
        return "Tile at position ({}, {})".format(self.x, self.y)

    def get_position(self):
        return self.x, self.y

    def position_to_string(self):
        return "{} {}".format(self.x, self.y)


class Grid:
    def __init__(self):
        self.width,self.height = [int(i) for i in input().split()]
        self.list_tiles = list()

    def visit(self, tile: Tile):
        next(filter(lambda x: x == tile, self.list_tiles)).visited = True


class Batman:
    def __init__(self, tile: Tile):
        self.tile = tile
        self.distance_to_bomb = Distance.UNKNOWN


class Game:
    def __init__(self):
        self.grid = Grid()
        self.remaining_turns = int(input())
        x, y = [int(i) for i in input().split()]
        self.batman = Batman(Tile(x, y, True))

    def update(self):
        self.batman.distance_to_bomb = Distance(input())

    def next_action(self):
        return "0 0"


game = Game()

# game loop
while True:
    game.update()
    next_action = game.next_action()

    print(next_action)
