import networkx as nx
from karateclub import DeepWalk

g = nx.gnm_random_graph(100, 1000)  # 随机生成n节点，m条边的图

model = DeepWalk()  # 随机行走
model.fit(g)
print(model.dimensions)

model = DeepWalk(dimensions=64)
model.fit
print(model.dimensions)
