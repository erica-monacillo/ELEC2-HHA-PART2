import networkx as nx
import matplotlib.pyplot as plt

degrees = [4, 3, 2, 2, 1, 0]

# Vertices
vertices = ["v1", "v2", "v3", "v4", "v5", "v6"]

def havel_hakimi(degree_sequence):

    sequence = sorted(degree_sequence, reverse=True)

    print("\nHAVEL-HAKIMI REDUCTION")
    print("-" * 50)

    step = 0

    while True:

        sequence = [d for d in sequence if d != 0]

        if not sequence:
            print(f"{step}  All zero -> SUCCESS")
            return True

        d = sequence.pop(0)

        print(
            f"{step}  Remove {d}, "
            f"subtract 1 from the next {d} terms"
        )

        if d > len(sequence):
            print("     FAILURE: not enough remaining vertices.")
            return False

        for i in range(d):

            sequence[i] -= 1

            if sequence[i] < 0:
                print("     FAILURE: negative degree.")
                return False

        sequence.sort(reverse=True)

        print("     Result:", sequence)

        step += 1

def construct_graph():

    G = nx.Graph()

    G.add_nodes_from(vertices)

    edges = [
        ("v1", "v2"),
        ("v1", "v3"),
        ("v1", "v4"),
        ("v1", "v5"),
        ("v2", "v3"),
        ("v2", "v4")
    ]

    G.add_edges_from(edges)

    return G

def verify_degrees(G):

    print("\nDEGREE VERIFICATION")
    print("-" * 50)

    all_match = True

    for vertex, target_degree in zip(vertices, degrees):

        actual_degree = G.degree(vertex)

        if actual_degree == target_degree:
            match = "YES"
        else:
            match = "NO"
            all_match = False

        print(
            f"{vertex}: "
            f"Target = {target_degree}, "
            f"Actual = {actual_degree}, "
            f"Match = {match}"
        )

    return all_match

def main():

    print("CS 414-4B - ACTIVITY 1 (Part 2)")
    print("Havel-Hakimi Algorithm")
    print("=" * 60)

    print("Degree Sequence:", tuple(degrees))
    print("Vertices:", vertices)


    print("\nSTEP 1 - PRECONDITIONS")
    print("-" * 50)

    degree_sum = sum(degrees)
    maximum_degree = max(degrees)
    n = len(degrees)

    print(
        f"Sum of degrees: "
        f"{' + '.join(map(str, degrees))} = {degree_sum}"
    )

    if degree_sum % 2 == 0:
        print("Sum is even -> PASS")
    else:
        print("Sum is odd -> NON-GRAPHICAL")
        return

    print(f"Maximum degree = {maximum_degree}")
    print(f"n - 1 = {n - 1}")

    if maximum_degree <= n - 1:
        print("Maximum degree <= n-1 -> PASS")
    else:
        print("Maximum degree > n-1 -> NON-GRAPHICAL")
        return

    print("\nSTEP 2 - HAVEL-HAKIMI REDUCTION")

    graphical = havel_hakimi(degrees)

    if not graphical:

        print("\nVERDICT: NON-GRAPHICAL")
        print("The network cannot be constructed.")
        return

    print("\nVERDICT: GRAPHICAL")

    print("\nSTEP 3 - CONSTRUCTING THE GRAPH")

    G = construct_graph()

    print("\nResulting Edge List:")

    for edge in G.edges():
        print(f"{edge[0]} - {edge[1]}")

    print(f"\nTotal number of edges: {G.number_of_edges()}")

    verified = verify_degrees(G)

    if verified:

        print("\nAll six vertices match their target degrees exactly.")
        print(
            "The graph correctly realizes "
            "S3 = (4, 3, 2, 2, 1, 0)."
        )

    else:

        print("\nERROR: Degree verification failed.")
        return

    print("\nSTEP 5 - RENDERING THE NETWORK")

    pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=1800,
        font_size=12,
        font_weight="bold",
        width=2
    )

    plt.title(
        "Constructed Network: "
        "S3 = (4, 3, 2, 2, 1, 0)"
    )

    plt.axis("off")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()