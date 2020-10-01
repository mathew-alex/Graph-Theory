import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

n = input("Enter no of Edges : ")
for i in range(0,n):
    edge = map(int,raw_input().split(' '))
    g.add_edge(edge[0],edge[1])

print nx.info(g)

nx.draw(g, with_labels=True)

plt.show()

'''Sample Input

Enter no of Edges : 5
1 2
2 3
3 4
4 5
1 5

                            '''
