"""
Graph Representations, Traversals, Shortest Paths, Topological Sort, and Disjoint Set.

Time Complexities:
- BFS / DFS: O(V + E)
- Dijkstra's Algorithm: O((V + E) log V)
- Topological Sort (Kahn's Algorithm): O(V + E)
- Union-Find (Find & Union with Path Compression & Rank): O(α(N)) amortized (~O(1))
"""

from collections import deque
import heapq
from typing import Any, Dict, List, Optional, Set, Tuple


class Graph:
    """Graph using Adjacency List supporting directed/undirected and weighted edges."""

    def __init__(self, directed: bool = False) -> None:
        self.directed: bool = directed
        self.adj_list: Dict[Any, List[Tuple[Any, float]]] = {}

    def add_vertex(self, vertex: Any) -> None:
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, u: Any, v: Any, weight: float = 1.0) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].append((v, weight))
        if not self.directed:
            self.adj_list[v].append((u, weight))

    def get_vertices(self) -> List[Any]:
        return list(self.adj_list.keys())

    def get_neighbors(self, vertex: Any) -> List[Tuple[Any, float]]:
        return self.adj_list.get(vertex, [])


def bfs(graph: Graph, start_vertex: Any) -> List[Any]:
    """
    Breadth-First Search traversal starting from start_vertex.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start_vertex not in graph.adj_list:
        return []

    visited: Set[Any] = {start_vertex}
    queue: deque = deque([start_vertex])
    result: List[Any] = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor, _ in graph.get_neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def dfs(graph: Graph, start_vertex: Any) -> List[Any]:
    """
    Depth-First Search traversal starting from start_vertex.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if start_vertex not in graph.adj_list:
        return []

    visited: Set[Any] = set()
    result: List[Any] = []

    def _dfs_helper(v: Any) -> None:
        visited.add(v)
        result.append(v)
        for neighbor, _ in graph.get_neighbors(v):
            if neighbor not in visited:
                _dfs_helper(neighbor)

    _dfs_helper(start_vertex)
    return result


def dijkstra(graph: Graph, start_vertex: Any) -> Dict[Any, float]:
    """
    Dijkstra's Single Source Shortest Path Algorithm for non-negative weights.

    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    if start_vertex not in graph.adj_list:
        return {}

    distances: Dict[Any, float] = {v: float("inf") for v in graph.get_vertices()}
    distances[start_vertex] = 0.0

    priority_queue: List[Tuple[float, Any]] = [(0.0, start_vertex)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph.get_neighbors(current_vertex):
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def topological_sort(graph: Graph) -> List[Any]:
    """
    Topological Sort using Kahn's Algorithm for Directed Acyclic Graphs (DAG).

    Returns topological order or empty list if graph contains a cycle.

    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if not graph.directed:
        raise ValueError("Topological sort is defined only for directed graphs.")

    in_degree: Dict[Any, int] = {v: 0 for v in graph.get_vertices()}
    for u in graph.adj_list:
        for v, _ in graph.adj_list[u]:
            in_degree[v] += 1

    queue: deque = deque([v for v in in_degree if in_degree[v] == 0])
    topo_order: List[Any] = []

    while queue:
        u = queue.popleft()
        topo_order.append(u)

        for v, _ in graph.get_neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(topo_order) != len(graph.get_vertices()):
        return []  # Cycle detected

    return topo_order


class DisjointSet:
    """Disjoint Set Union (DSU) / Union-Find with path compression and union by rank."""

    def __init__(self, vertices: List[Any]) -> None:
        self.parent: Dict[Any, Any] = {v: v for v in vertices}
        self.rank: Dict[Any, int] = {v: 0 for v in vertices}

    def find(self, item: Any) -> Any:
        """Finds representative of set containing item with path compression."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x: Any, y: Any) -> bool:
        """Unions two sets containing x and y. Returns True if sets were disjoint."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # Already in same set

        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True
