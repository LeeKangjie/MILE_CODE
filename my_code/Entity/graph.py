import math
import numpy as np


class Graph(object):
	def __init__(self, node_num, edge_num):
		self.node_num = node_num
		self.edge_num = edge_num
		self.adj_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.degree_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.lap_mat = np.zeros((node_num, node_num), dtype=np.int)
		self.nor_lap_mat = np.zeros((node_num, node_num), dtype=np.float)

	# 计算图的邻接矩阵
	def get_adj_mat(self, edges):
		for edge in edges:
			self.adj_mat[edge[0]][edge[1]] = 1
			self.adj_mat[edge[1]][edge[0]] = 1

	# 计算图度矩阵 对角矩阵
	def get_degree_mat(self):
		tmp = np.sum(self.adj_mat, axis=0)
		for i in range(len(tmp)):
			self.lap_mat[i][i] = tmp[i]

	# 计算图的拉普拉斯矩阵
	def get_lap_mat(self):
		self.lap_mat = self.degree_mat - self.adj_mat

	# 计算图的归一化拉普拉斯矩阵
	def get_nor_lap_mat(self):
		for i in range(self.node_num):
			for j in range(self.node_num):
				if i == j and self.degree_mat[i][i] != 0:
					self.nor_lap_mat[i][j] = 1
				elif i != j and self.adj_mat[i][j] == 1:
					self.nor_lap_mat[i][j] = -(1.0 / math.sqrt(self.degree_mat[i][i] * self.degree_mat[j][j]))

	def __str__(self):
		return "graph size:\n node_number: %d\t edge_number: %d" % (self.node_num, self.edge_num)
