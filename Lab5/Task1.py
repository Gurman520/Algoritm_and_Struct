from collections import deque
import Graph as G


g = G.Graph()
g.addEdge("you", "alice")
g.addEdge("you", "bob")
g.addEdge("you", "claire")
g.addEdge("alice", "peggy")
g.addEdge("bob", "anuj")
g.addEdge("bob", "peggy")
g.addEdge("claire", "thom")
g.addEdge("claire", "jonny")
g.addEdge("claire", "you")


def search(name_start, name_stop):
    search_queue = deque()
    search_queue += look(name_start)
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == name_stop:
                return True
            else:
                search_queue += look(person)
                searched.add(person)
    return False


def look(name):
    a = g.getVertex(name)
    b = a.getConnections()
    nam = []
    for i in b:
        nam.append(i.id)
    return nam


if search("claire", "alice"):
    print("The connection exists")
else:
    print("The connection does not exist")
