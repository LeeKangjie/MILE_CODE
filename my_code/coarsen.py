def coarsen(origin_graph, times=3):
	list = []
	list.append(origin_graph)
	for i in range(1, times):
		coarsen_graph = get_coarsen_graph(list[i])
		list.append(coarsen_graph)
	return list


def get_coarsen_graph(graph):
	new_graph = None

	return new_graph
