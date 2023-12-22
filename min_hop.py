import random
import time
from collections import deque

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = {node: [] for node in range(num_nodes)}

    def add_edge(self, start, end):
        self.adj_list[start].append(end)

    def bfs_min_hop_path(self, start, end):
        visited = [False] * self.num_nodes
        queue = deque([(start, [start])])

        while queue:
            current_node, path = queue.popleft()
            if current_node == end:
                return path

            for neighbor in self.adj_list[current_node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, path + [neighbor]))

        return None  # No path found

def generate_random_graph(num_nodes, num_edges):
    graph = Graph(num_nodes)
    all_possible_edges = [(i, j) for i in range(num_nodes) for j in range(num_nodes) if i != j]

    for start, end in random.sample(all_possible_edges, num_edges):
        graph.add_edge(start, end)

    return graph

def test_min_hop_path(graph, num_tests=25):
    total_time = 0

    for _ in range(num_tests):
        s, t = random.sample(range(graph.num_nodes), 2)
        start_time = time.perf_counter_ns()
        path = graph.bfs_min_hop_path(s, t)
        end_time = time.perf_counter_ns()
        total_time += (end_time - start_time)

        print(f"Path from {s} to {t}: {path}")

    avg_time = total_time / num_tests
    return avg_time

def main():
    graph_sizes = [(50, 100), (100, 400), (200, 1600), (400, 3200)]

    for num_nodes, num_edges in graph_sizes:
        graph = generate_random_graph(num_nodes, num_edges)
        avg_time = test_min_hop_path(graph)
        print(f"Graph with {num_nodes} nodes and {num_edges} edges took on average {avg_time:.0f} nanoseconds per query")

if __name__ == "__main__":
    main()
