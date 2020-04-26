"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are
connected.

Return the length of the shortest path that visits every node. You may start and stop at any node,
you may revisit nodes multiple times, and you may reuse edges.



Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]


Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
"""
def pick_option(visited, options):
    # print(visited, options)
    pick = True
    v = options.pop()
    while v and pick and len(options)>=1:
        if v in visited:
            v = options.pop()
        else:
            pick = False
    # print('picked', v)
    return v


def helper(graph_, i):
    c = 0
    visited = [i]
    while len(visited) < len(graph_) and c <= len(graph_)*2:
        # print('visited', visited)
        if i not in visited:
            visited += [i]
        i = pick_option(visited, list(graph_[i]))
        c += 1
    return c


def shortest_path(graph: list) -> int:
    c = float('inf')
    for i in range(len(graph)):
        # print('------- {} ---------'.format(i))
        c = min(helper(graph, i), c)
    # print(c-1)
    return c-1


if __name__ == "__main__":
    # print('test 1 - pick_options', pick_option([1,2,3], [1,2,3,4]) == 4)
    # print('test 2 - pick_options', pick_option([1, 2, 3], [4]) == 4)
    # print('test 3 - pick_options', pick_option([1, 2, 3], [2, 3]) == 3)
    # print('test 4 - pick_options', pick_option([1, 2, 3], [1]) == 1)

    print('test 1: ',shortest_path([[1,2,3],[0],[0],[0]])==4)
    print('test 2: ', shortest_path([[1],[0,2,4],[1,3,4],[2],[1,2]]) == 4)