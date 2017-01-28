def clone_graph(node, cloned = {}):
    clone = { 'label' : node['label'], 'edges' : [] }
    cloned[node.get('label')] = clone

    for e, nextNode in enumerate(node['edges']):
        if nextNode['label'] not in cloned:
            nextClone = clone_graph(nextNode, cloned)
            clone['edges'].append(nextClone)
        else:
            clone['edges'].append( cloned[nextNode['label']] )

    return clone

a = [
    { 'label' : 1, 'edges' : [] },
    { 'label' : 2, 'edges' : [] },
    { 'label' : 3, 'edges' : [] },
    { 'label' : 4, 'edges' : [] },
    { 'label' : 5, 'edges' : [] },
]

a[0]['edges'].append(a[1])
a[1]['edges'].extend([a[4], a[2]])
a[2]['edges'].append(a[3])
a[3]['edges'].append(a[4])

b = clone_graph(a[0])
print b
print a[0]
print b == a[0]
print b is a[0]
