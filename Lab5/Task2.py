def inverse():
    g = {}
    flag = 0
    for i in graph:
        b = graph.get(i)
        if flag == 0:
            g[i] = []
            flag = 1
        if len(b) != 0:
            for num in b:
                z = []
                if num in g:
                    z = g.get(num)
                else:
                    g[num] = []
                z.append(i)
                g.update({num: z})
    return g


graph = {"0": ["1", "2"], "2": ["1"], "1": ["3"], "3": []}
graph = inverse()
print(graph)
