
def earliest_ancestor(ancestors, starting_node, path=None, graph=None):
    graph = {}
    for a in ancestors:
        if a[1] in graph:
            graph[a[1]].add(a[0])
        else:
            graph[a[1]] = set()
            graph[a[1]].add(a[0])

    result = [-1]

    stack = []
    stack.append([starting_node])
    completed = set()

    while len(stack) > 0:
        path = stack.pop()
        cur_vertex = path[-1]

        if cur_vertex not in completed:
            completed.add(cur_vertex)

        if cur_vertex in graph:
            for v in graph[cur_vertex]:
                new_path = list(path)
                new_path.append(v)
                stack.append(new_path)

        if len(result) < len(path):
            result = path
        elif len(result) == len(path) and result[-1] > cur_vertex:
            result = path

    return result[-1]
