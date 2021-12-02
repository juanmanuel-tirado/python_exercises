import argparse

"""
This is a greedy approach to the problem.
Another solution would to be to generate all
the potential combinations of solutions and 
return the first one that solves the problem.
"""

WHITE = False
BLACK = True


def process_graph(g):
    visited = []
    colors = [WHITE for i in range(len(g))]

    for v in range(len(g)):
        if v in visited:
            continue
        colors, visited = process_graph_aux(g, v, colors, visited+[v])
    
    black_vertices = [x + 1 for x in range(len(colors)) if colors[x] == BLACK ]

    return len(black_vertices), black_vertices

def process_graph_aux(g, u, colors, visited):
   
    #find our color
    current_color = colors[u]
    # check our neighbors
    for v in g[u]:
        if v in visited:
            continue
        adjacent_color = colors[v]
        if current_color == adjacent_color:
            new_plan = colors
            new_plan[v] = not adjacent_color
            next_plan, visited = process_graph_aux(g, v, new_plan, visited + [v])
            colors = next_plan

    return colors, visited


def read_graph(reader):
    # The first line is the number of vertices and edges
    first_line = reader.readline().strip()
    tokens = first_line.split(' ')
    n = int(tokens[0])
    k = int(tokens[1])
    # our graph will be an adjacency list
    g = [set() for i in range(n)]
    for edge in range(k):
        edge_line = reader.readline().strip()
        tokens = edge_line.split(' ')
        # vertices indexed starting from 0
        a = int(tokens[0]) - 1
        b = int(tokens[1]) - 1
        # this is an undirected graph
        g[a].add(b)
        g[b].add(a)

    return g

def process_file(input_file):
    graphs = []
    with open(input_file) as reader:
        # first line is the number of graphs
        ngraphs = reader.readline().strip()
        if not ngraphs.isdigit():
            print('Expected number of graphs in the first line')
            return None
        ngraphs = int(ngraphs)
        if ngraphs <= 0:
            print('Expected positive number of graphs')
            return None
        for id in range(ngraphs):
            g = read_graph(reader)
            graphs.append(g)
    return graphs

def main():
    parser = argparse.ArgumentParser(description='Graph coloring')
    parser.add_argument('--input_file', dest='input_file', type=str, help='Path to the input file')
    args = parser.parse_args()
    graphs = process_file(args.input_file)
    if graphs is None:
       return
    for g in graphs:
        num_black, black_vertices = process_graph(g)
        print(num_black)
        print(' '.join(str(x) for x in black_vertices))

if __name__ == '__main__':
    main()
