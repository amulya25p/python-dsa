# class graph:
#     def __init__(self, nodes, edges):
#          self.nodes=nodes
#          self.data=[[] for _ in range(nodes)]
#          for n1, n2 in edges:
#              self.data[n1].append(n2)
#              self.data[n2].append(n1)
    # def __init__(self, nodes, edges):
    #     self.nodes=nodes
    #     self.data=[[0 for _ in range(nodes)] for _ in range(nodes)]
    #     print(self.data)
    #     for n1, n2 in edges:
    #         if n1>0 or n2>0:
    #             self.data[n1][n2]=1 
    #             self.data[n2][n1]=1 
    # def __repr__(self):
    #     return ['{}: {}'.format(n, neighbours) for n, neighbours in enumerate(self.data)]
    # def __str__(self):
    #     self.__repr__()
def bfs(graph, root):
    queue=[]
    discovered = [False]*len(graph.data)
    discovered[root]=True
    queue.append(root)
    idx=0
    while idx<len(queue):
        current=queue[idx]
        idx+=1

        for node in graph.data[current]:
            if not discovered[node]:
                discovered[node]=True
                queue.append(node)
    return queue

def dfs(graph, root):
    stack=[]
    discovered=[False]*len(graph.data)
    result=[]
    stack.append(root)
    while len(stack)>0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current]=True
            result.append(current)
            for node in graph.data[current]:
               if not discovered[node]:
                stack.append(node)
    return result

class dw_graph:
    def __init__(self, nodes, edges, directed=False, weighted=False):
        self.nodes=nodes
        self.directed=directed
        self.weighted=weighted
        self.data=[[] for _ in range(nodes)]
        self.weight=[[] for _ in range(nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight=edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
            else:
                node1, node2= edge
                self.data[node1].append(node2)
                if not directed:
                    self.data[node2].append(node1)
    def __repr__(self):
        result=""
        if self.weighted:
            for i, (nodes, weights) in enumerate(zip(self.data, self.weight)):
                result += "{}: {}\n".format(i, list(zip(nodes, weights)))
        else:
            for i, nodes in enumerate(self.data):
                result+="{}:{}\n".format(i, nodes)
        return result

def shortest_path(graph, source, target):
    visited= [False]*len(graph.data)
    parent=[False]*len(graph.data)
    distance= [float('inf')]*len(graph.data)
    queue=[]
    distance[source]=0
    queue.append(source)
    idx=0
    while idx<len(queue) and not visited[target]:
        current=queue[idx]
        visited[current]=True
        idx+=1
        update_distances(graph, current, distance, parent)
        next_node= pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)
    return distance[target], parent

def update_distances(graph, current, distance, parent=None):
    """Update the distances of the current node's neighbors"""
    neighbors = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbors):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current

def pick_next_node(distance, visited):
    """Pick the next univisited node at the smallest distance"""
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node
nodes= 6
edges=[(0, 1, 4), (0, 2, 2), (1, 2, 5), (1, 3, 10), (2, 4, 3), (4, 3, 4), (3, 5, 11)]
g1=dw_graph(nodes, edges, weighted=True, directed=True)
print(shortest_path(g1, 0, 5))



# for x in enumerate(g1.data):
#     print(x)

# print(bfs(g1, 4))
# print(dfs(g1, 3))

