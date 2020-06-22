#!/usr/bin/python3

# Problem Statement #3 {{{
"""
'edges.txt' file describes an undirected graph with integer edge costs.
it has the format:
    [number_of_nodes][number_of_edges]
    [one_node_of_edge_1][other_node_of_edge_1][edge_1_cost]
    [one_node_of_edge_2][other_node_of_edge_2][edge_2_cost]
    [...][...][...]

For example: the 3rd line of the file is "2 3 -8874", indicating that there is
an edge connecting vertex #2 and vertex #3 that has cost -8874.

## problem#3
Task is to run Prim's minimum spanning tree algorithm on this graph. You should
report overall cost of a minimum spanning tree (positive or negative integer).

- problem#3 answer: -3612829
"""
# }}}

