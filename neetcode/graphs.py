graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

# def hasPath_recur(graph, src, dst):
#     if (src == dst):
#         return True
#     for neighbor in graph[src]:
#         if hasPath_recur(graph, neighbor, dst) == True:
#             return True
#     return False


def hasPath_bfs(graph, src, dst):
    queue = [src]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current, end=" ")
        if current == dst:
            return True
        for neighbor in graph[current]:
            queue.append(neighbor)
    return False


#print(hasPath_recur(graph, 'f', 'k'))
print(hasPath_bfs(graph, 'f', 'k'))
