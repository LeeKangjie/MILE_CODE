import numpy as np


def coarsen(origin_graph, times=3):
	list = []
	list.append(origin_graph)
	for i in range(1, times):
		coarsen_graph = get_coarsen_graph(list[i])
		list.append(coarsen_graph)
	return list


def get_coarsen_graph(graph):
	new_graph = None
	adj = graph.adj_mat
	dgeree = graph.degree_mat
	mapper = {}
	for i in range(graph.node_num):
		mapper[i] = i
	flag = np.zeros(graph.nodenum, dtype=np.int)
	# mile 中第一种粗化方法
	for i in range(graph.node_num):
		for j in range(graph.node_num):
			if dgeree[i][i] == dgeree[j][j] and dgeree[i][i] == 1 and np.where(adj[i] == 1) == np.where(adj[j] == 1) \
					and flag[i] == 0 and flag[j] == 0:
				flag[i] = 1
				flag[j] = 1
				dgeree[np.where(adj[i] == 1)[0]] -= 1
			# TODO ij 改为映射的方法

	# mile 中第二种粗化方法

	return new_graph
