from igraph import *
import igraph as ig
from sympy import *
import math
import sympy
import numpy as np
g = Graph.Load('./karate.gml', format='gml')

label = [int(a) for a in g.vs()['id']]
color_dict = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
color_dict = {"m": "blue", "f": "red"}
g.vs["color"] = [color_dict[gender] for gender in color_dict]

# plot(g,vertex_size='30', vertex_label = label, )
a = g.get_adjacency()
b = sympy.Matrix(a)
print(b.shape)



# value, xiangliang = np.linalg.eig(b)
# print(value)
# print(xiangliang)

print(b.eigenvals())