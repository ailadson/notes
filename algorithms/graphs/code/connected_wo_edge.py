def connected_wo_edge(G):
    time = [None] * len(G)
    return dfs(G, time, None, 0, 0) is 0

def dfs(G, time, from_node, node, clock):
    time[node] = clock
    earliest_terminating_node = float('inf')

    for e, next_node in enumerate(G[node]):
        clock += 1
        if next_node is from_node:
            continue
        elif time[next_node] is not None:
            earliest_terminating_node = min(earliest_terminating_node, time[next_node])
        else:
            prev_earliest_terminating_node = dfs(G, time, node, next_node, clock)

            if prev_earliest_terminating_node  > time[node]:
                earliest_terminating_node = float('inf')
                break
            else:
                earliest_terminating_node = min(prev_earliest_terminating_node, time[next_node])

    return earliest_terminating_node

g = [
    [2,4],
    [5,3],
    [0,4],
    [5,1],
    [2,0,5],
    [4,1,3]
]

print connected_wo_edge(g)
