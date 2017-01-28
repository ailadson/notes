from collections import namedtuple, defaultdict
from Queue import *

def network_max_flow(network, source, sink):
    residual_network = build_residual_network(network)

    pred = bfs(residual_network, source)
    volume = get_volume(residual_network, pred, source, sink)

    while volume > 0:
        augment_path(residual_network, pred, source, sink, volume)
        pred = bfs(residual_network, source)
        volume = get_volume(residual_network, pred, source, sink)

    return get_flow(residual_network, sink)

def get_flow(network, sink):
    max_flow = 0
    checks = map(lambda e : e['val'], network[sink])

    for i, edgeNode in enumerate(checks):
        edge_to_sink = filter(lambda e : e['val'] is sink, network[edgeNode]).pop()
        max_flow += edge_to_sink['flow']

    return max_flow

def augment_path(network, pred, source, sink, volume):
    if source is sink:
        return

    edge = get_edge(network, pred[sink], sink)
    edge['flow'] += volume
    edge['residual'] -= volume

    edge = get_edge(network, sink, pred[sink])
    edge['residual'] += volume

    augment_path(network, pred, source, pred[sink], volume)



def get_volume(network, pred, source, sink):
    volume = float('inf')

    while source is not sink:
        if pred[sink] is None:
            return 0
        edge = get_edge(network, pred[sink], sink)
        volume = min(edge['residual'], volume)
        sink = pred[sink]

    return volume

def get_edge(g, from_v, to_v):
    for i, edgeNode in enumerate(g[from_v]):
        if edgeNode['val'] is to_v:
            return edgeNode

def bfs(g, source):
    pred = [None] * len(g)
    q = Queue()
    q.put(source)

    while q.empty() is not True:
        vertex = q.get()

        for i, edgeNode in enumerate(g[vertex]):
            if pred[edgeNode['val']] is None and edgeNode['residual'] > 0:
                pred[edgeNode['val']] = vertex
                q.put(edgeNode['val'])

    pred[source] = None
    return pred


def build_residual_network(network):
    res_network = [[] for i in range(len(network))]
    for node, edgeList in enumerate(network):
        for i, edge in enumerate(edgeList):
            res_network[node].append({ 'val' : edge.val, 'capacity' : edge.w, 'flow' : 0, 'residual' : edge.w })
            res_network[edge.val].append({ 'val' : node, 'capacity' : edge.w, 'flow' : 0, 'residual' : 0 })


    return res_network

EdgeNode = namedtuple("EdgeNode", "val w")
nw = [
    [EdgeNode(2, pow(10,9)), EdgeNode(3, pow(10,9))],
    [],
    [EdgeNode(3, 1), EdgeNode(1, pow(10,9))],
    [EdgeNode(1, pow(10,9))],
]

print network_max_flow(nw, 0, 1)
