graph = {'1': set(['2', '11', '3']),
'2': set(['9', '10', '1']),
'3': set(['4', '5', '6']),
'6': set(['7', '8', '3']),
'7': set(['9', '6']),
'10': set(['2']),
'9': set(['4', '7', '2']),
'4': set(['3', '9']),
'5': set(['3']),
'8': set(['6']),
'11': set(['1'])}

def width_graph(start, graph, visited = []):
	queue = []
	queue.append(start)
	visited.append(start)
	while queue:

		for elem in graph[queue[0]]:
			if elem not in visited:
				queue.append(elem)
				visited.append(elem)

		queue.pop(0)

	return visited

print(width_graph('10', graph))
