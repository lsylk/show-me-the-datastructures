import heapq
from collections import defaultdict 
from typing import Optional
from math import sqrt, pow

from helpers import Map

def heuristic(a: tuple[float, float], b: tuple[float, float]) -> float:
    """
    Calculate the Euclidean distance between two points.

    Args:
        a (tuple[float, float]): The coordinates of the first point (x1, y1).
        b (tuple[float, float]): The coordinates of the second point (x2, y2).

    Returns:
        float: The Euclidean distance between the two points.
    """
    return sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    

def reconstruct_path(came_from: dict[int, int], current: int) -> list[int]:
    """
    Reconstruct the path from the start node to the goal node.

    Args:
        came_from (dict[int, int]): A dictionary mapping each node to the node it came from.
        current (int): The goal node.

    Returns:
        list[int]: The reconstructed path from the start node to the goal node.
    """
    curr = current
    path = []
    while curr in came_from:
        path.insert(0, curr)
        curr = came_from[curr]
    return path

def findElement(lst, elem):
    return next(i for i,v in enumerate(lst) if v[1]==elem)
    # for i in range(len(lst)):
    #     if lst[i][1] == elem:
    #         return i
    # return -1

def shortest_path(M: Map, start: int, goal: int) -> Optional[list[int]]:
    """
    Find the shortest path between two nodes in a map using the A* algorithm.

    Args:
        M (Map): The map containing the graph, intersections, and roads.
        start (int): The starting node.
        goal (int): The goal node.

    Returns:
        Optional[list[int]]: The shortest path from the start node to the goal node, or None if no path is found.
    """
    # based on https://en.wikipedia.org/wiki/A*_search_algorithm
    openSet: set[int] = {start}
    cameFrom: dict[int, int] = dict()
    gScore = defaultdict(lambda: float('inf'))
    gScore[start] = 0
    # print(M.intersections.keys())
    fScore = [[float('inf'), i] if i != start else [heuristic(M.intersections[start], M.intersections[goal]), i] for i in M.intersections.keys()]
    heapq.heapify(fScore)

    while len(openSet) > 0:
        current = heapq.heappop(fScore)[1]
        if current == goal:
            return [start]+reconstruct_path(cameFrom, current)

        openSet.remove(current)
        
        for neighbor in M.roads[current]:
            tentative_gScore = gScore[current] + heuristic(M.intersections[current], M.intersections[neighbor])
            if tentative_gScore < gScore[neighbor]:
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                # alter key/priority in fScore
                neighborIndex = findElement(fScore, neighbor)
                fScore[neighborIndex][0] = gScore[neighbor] + heuristic(M.intersections[neighbor], M.intersections[goal])
                heapq._siftdown(fScore, 0, neighborIndex)
                
                if neighbor not in openSet:
                    openSet.add(neighbor)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)