import numpy as np


class Graph(object):
	def __init__(self, node_num, edge_num):
		self.node_num = node_num
		self.edge_num = edge_num
		self.adj_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.degree_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.lap_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.nor_lap_mat = np.zeros((node_num, node_num), dtype=np.float)

	def get_adj_mat(self, edges):
		for edge in edges:
			self.adj_mat[edge[0]][edge[1]] = 1
			self.adj_mat[edge[1]][edge[0]] = 1

	def get_degree_mat(self):
		tmp = np.sum(self.adj_mat, axis=0)
		for i in range(len(tmp)):
			self.lap_mat[i][i] = tmp[i]

	def get_lap_mat(self):
		self.lap_mat = self.degree_mat - self.adj_mat

	# 计算图的归一化拉普拉斯矩阵
	def get_nor_lap_mat(self):
		return None

	# TODO 未完成归一化拉普拉斯矩阵的计算

	def __str__(self):
		return "graph size:\n node_number: %d\t edge_number: %d" % (self.node_num, self.edge_num)
