#!/usr/bin/python3

# Problem Statement #3 {{{
"""
In this programming problem you'll code up Prim's minimum spanning tree
algorithm.
'edges.txt' file describes an undirected graph with integer edge costs.
it has the format:
    [number_of_nodes][number_of_edges]
    [one_node_of_edge_1][other_node_of_edge_1][edge_1_cost]
    [one_node_of_edge_2][other_node_of_edge_2][edge_2_cost]
    [...][...][...]

For example: the 3rd line of the file is "2 3 -8874", indicating that there is
an edge connecting vertex #2 and vertex #3 that has cost -8874.

You should NOT assume that edge costs are positive, nor should you assume that
they are distinct.

## problem#3
Task is to run Prim's minimum spanning tree algorithm on this graph. You should
report overall cost of a minimum spanning tree (positive or negative integer).

IMPLEMENTATINO NOTES: This graph is small enough that the straightforward O(mn)
time implementation of Prim's algorithm should work fine.
OPTIMAL: For those of you seeking an additional challenge, try implementing
a heap-based version. The simpler approach, which should already give you
a healthy speed-up, is to maintain relevant edges in a heap (with keys = edge
costs).
SUPERIOR approach stores the unprocessed vertices in the heap, as described in
lecture. Not this requires a heap that supports deletions, and you'll probably
need to maintain some kind of mapping between vertices and their positions in
the heap.

- problem#3 answer: -3612829
"""
# }}}

# vim:foldmethod=marker:foldlevel=0
