def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {"3/4 cup milk": set(["1 cup mix"]),
         "1 egg": set(["1 cup mix"]),
         "1 ns Oil": set(["1 cup mix"]),
         "1 cup mix": set(["heat syrup", "pour 1/4 cup"]),
         "heat syrup": set(["eat"]),
         "eat": set([]),
         "heat griddle": set(["pour 1/4 cup"]),
         "pour 1/4 cup": set(["turn when bubbly"]),
         "turn when bubbly": set(["eat"])}

print(*dfs(graph, "heat griddle"), sep=' => ')