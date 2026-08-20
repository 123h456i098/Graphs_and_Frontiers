from AStarFrontier import *
from search import *

def tests_one():
    print("\n\nTest one\n\n")
    map_str = """
+-------+
|  9  XG|
|X XXX P|
| S  0FG|
|XX P XX|
+-------+
"""

    graph = RoutingGraph(map_str)

    def print_arc(arc):
        """Avoids wide test output :)"""
        arc_repr = f"Arc(tail={repr(arc.tail)}, "
        arc_repr += f"head={repr(arc.head)},\n    "
        arc_repr += f"action={repr(arc.action)}, "
        arc_repr += f"cost={repr(arc.cost)})"
        print(arc_repr)

    print("Starting nodes:")
    print(sorted(graph.starting_nodes()))
    print("Outgoing arcs at starting states:")
    for s in sorted(graph.starting_nodes()):
        print(f"From {s}:")
        for arc in graph.outgoing_arcs(s):
            print_arc(arc)
        print()

    node = (1,1,5)
    print(f"\nIs {node} goal?", graph.is_goal(node))
    print(f"Outgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    node = (1,7,2)
    print(f"\nIs {node} goal?", graph.is_goal(node))
    print(f"Outgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    node = (3, 7, 0)
    print(f"\nIs {node} goal?", graph.is_goal(node))

    node = (3, 7, math.inf)
    print(f"\nIs {node} goal?", graph.is_goal(node))

    node = (3, 6, 5)
    print(f"\nIs {node} goal?", graph.is_goal(node))
    print(f"Outgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    node = (3, 6, 9)
    print(f"\nIs {node} goal?", graph.is_goal(node))
    print(f"Outgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    node = (2, 7, 4)  # at a location with a portal
    print(f"\nOutgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    print("\n\nTest two\n\n")
    map_str = """\
+--+
|GS|
+--+
"""

    graph = RoutingGraph(map_str)

    def print_arc(arc):
        """Avoids wide test output :)"""
        arc_repr = f"Arc(tail={repr(arc.tail)}, "
        arc_repr += f"head={repr(arc.head)},\n    "
        arc_repr += f"action={repr(arc.action)}, "
        arc_repr += f"cost={repr(arc.cost)})"
        print(arc_repr)

    print("Starting nodes:")
    print(sorted(graph.starting_nodes()))
    print("Outgoing arcs at the start:")
    for start in graph.starting_nodes():
        for arc in graph.outgoing_arcs(start):
            print_arc(arc)



    node = (1,1,1)
    print(f"\nIs {node} goal?", graph.is_goal(node))
    print(f"Outgoing arcs at {node}:")
    for arc in graph.outgoing_arcs(node):
        print_arc(arc)

    print("\n\nTest three\n\n")
    map_str = """\
+------+
|S    S|
|  GXXX|
|S     |
+------+
"""

    graph = RoutingGraph(map_str)
    print("Starting nodes:")
    print(sorted(graph.starting_nodes()))

def tests_two():
    print("\n\nTest one\n\n")
    map_str = """\
+-------+
|   G   |
|       |
|   S   |
+-------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest two\n\n")
    map_str = """\
+-------+
|  GG   |
|S    G |
|  S    |
+-------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest three\n\n")
    map_str = """\
+---+
|  G|
|   |
|S G|
+---+
"""

    map_graph = RoutingGraph(map_str)

    # Testing that the estimated_cost_to_goal method is being used:
    # Overriding the heuristic function to return infinity
    # should make the search behave as a BFS (and yield a suboptimal solution)
    map_graph.estimated_cost_to_goal = lambda node: float('inf')

    frontier = AStarFrontier(map_graph)

    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)

    if sum(arc.cost for arc in solution) != 14:
        print("Does your priority queue take the heuristic into account?")
    print("\n\nTest four\n\n")

    map_str = """\
+-------+
|     XG|
|X XXX  |
| S     |
+-------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest five\n\n")
    map_str = """\
+-------+
|  F  X |
|X XXXXG|
| 3     |
+-------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest six\n\n")
    map_str = """\
+--+
|GS|
+--+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest seven\n\n")
    map_str = """\
+---+
|GF2|
+---+
"""
    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest eight\n\n")
    map_str = """\
+----+
| S  |
| SX |
|GX G|
+----+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest nine\n\n")
    map_str = """\
+------------+
|    P       |
| 5          |
|XXXXXXXXX   |
|  P G       |
+------------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest ten\n\n")

    map_str = """\
+---------+
|         |
|    G    |
|         |
+---------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)
    print("\n\nTest Eleven\n\n")

    map_str = """\
+------------+
|    P       |
| 7          |
|XXXXXXXXX   |
|P F X  G    |
+------------+
"""

    map_graph = RoutingGraph(map_str)
    frontier = AStarFrontier(map_graph)
    solution = next(generic_search(map_graph, frontier), None)
    print_actions(solution)


def main():
    print("\n======== TESTING BASIC GRAPH FUNCTIONALITY ========\n")
    tests_one()
    print("\n======== TESTING A* ROUTE FINDING ========\n")
    tests_two()

if __name__ == "__main__":
    main()
