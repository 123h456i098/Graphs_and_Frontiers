from search import *
import math
import heapq
import itertools

class RoutingGraph(Graph):
    def __init__(self, map_string):
        self.map = map_string.strip().split("\n")
        self.teleports = []
        for row_num, row in enumerate(self.map):
            for col_num, col in enumerate(row):
                if col == "P":
                    self.teleports.append((row_num, col_num))

    def is_goal(self, node):
        """Returns true if the given node is a goal state, false otherwise."""
        row, col, fuel = node
        return self.map[row][col] == "G"

    def starting_nodes(self):
        """Returns a sequence of starting nodes."""
        agents = []
        for row_num, row in enumerate(self.map):
            for col_num, col in enumerate(row):
                if col in "S0123456789":
                    agents.append((row_num, col_num, int(col) if col != "S" else math.inf))
        return agents


    def outgoing_arcs(self, tail_node):
        """Given a node it returns a sequence of arcs (Arc objects)
        which correspond to the actions that can be taken in that
        state (node)."""
        directions = [
            ('N' , -1, 0),
            ('NE', -1, 1),
            ('E' ,  0, 1),
            ('SE',  1, 1),
            ('S' ,  1, 0),
            ('SW',  1, -1),
            ('W' ,  0, -1),
            ('NW', -1, -1)
            ]
        arcs = []

        row, col, fuel = tail_node
        for direction, y, x in directions:  # Possible direction arcs4
            if self.map[row + y][col + x] not in "-+|X" and fuel > 0:
                arcs.append(Arc(
                    tail_node,
                    (row + y, col + x, fuel - 1),
                    direction, 
                    5 if direction in ['N', 'S', 'E', 'W'] else 7
                    ))
        if self.map[row][col] == "F" and fuel < 9:  # Fuel up arc
            arcs.append(Arc(
                tail_node,
                (row, col, 9),
                "Fuel up",
                15
            ))
        if self.map[row][col] == "P":  # Possible portal arcs
            for teleport_row, teleport_col in self.teleports:
                if (row, col) != (teleport_row, teleport_col):
                    arcs.append(Arc(
                        tail_node,
                        (teleport_row, teleport_col, fuel),
                        f"Teleport to ({teleport_row}, {teleport_col})",
                        10
                    ))
        return arcs
    
    def estimated_cost_to_goal(self, node):
        return 0

class AStarFrontier(Frontier):
    def __init__(self, graph):
        self.container = []
        self.best_cost_found = {}
        self.graph = graph
        self.counter = itertools.count()

    def add(self, path):
        count = next(self.counter)
        path_cost = self.graph.estimated_cost_to_goal(path[-1].tail) + sum([arc.cost for arc in path])
        if path[-1].head not in self.best_cost_found or path_cost < self.best_cost_found[path[-1].head]:
            self.best_cost_found[path[-1].head] = path_cost
            heapq.heappush(self.container, [path_cost, count, path])
        
    def __next__(self):
        try:
            priority, count, path = heapq.heappop(self.container)
            return path
        except IndexError:
            raise StopIteration
  
