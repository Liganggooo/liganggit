graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
graph['fin'] = {}
# print(graph)

infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity
# print(costs)

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None
# print(parents)

processed = []
def find_lowest_costs_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return  lowest_cost_node

def dijkstra_algorithm(costs):
    node = find_lowest_costs_node(costs)
    while node is not None:
        print(node)
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_costs_node(costs)
        print(parents)
dijkstra_algorithm(costs)


