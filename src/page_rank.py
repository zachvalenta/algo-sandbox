from collections import defaultdict

def pagerank(graph, damping_factor=0.85, iterations=100):
    # Initialize PageRank values to 1/N
    nodes = list(graph.keys())
    N = len(nodes)
    ranks = {node: 1 / N for node in nodes}
    
    # Run the PageRank algorithm
    for _ in range(iterations):
        new_ranks = defaultdict(float)
        for node in nodes:
            # Distribute current rank to outbound links
            outbound_links = graph[node]
            if outbound_links:
                shared_rank = ranks[node] / len(outbound_links)
                for outbound in outbound_links:
                    new_ranks[outbound] += shared_rank
            # Handle dangling nodes (no outbound links)
            else:
                for other_node in nodes:
                    new_ranks[other_node] += ranks[node] / N

        # Apply the damping factor
        for node in nodes:
            new_ranks[node] = (1 - damping_factor) / N + damping_factor * new_ranks[node]
        
        ranks = new_ranks

    return ranks

# Example directed graph
# Each key is a node, and its value is a list of nodes it links to
example_graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["A"],
    "D": ["C"],
    "E": ["A", "D"],
}

# Run the toy PageRank implementation
result = pagerank(example_graph)

# Print the results
print("PageRank results:")
for page, rank in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{page}: {rank:.4f}")
