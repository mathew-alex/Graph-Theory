'''
    Program to identify the type of graph
'''

from graphviz import Graph

dot = Graph(comment='Simple Graph')

edges = []
n = input("Enter no.of Edges : ")
for i in range(0,n):
    edge = raw_input().split(' ')
    dot.edge(edge[0],edge[1],label=edge[2])
    edges.append((edge[0],edge[1]))

if len(edges) != len(set(edges)):
    dot.comment = "Multi Graph"

for edge in edges:
    if edge[0]==edge[1]:
        dot.comment = "Pseudo Graph"
        break
        
print dot.source
dot.save('file')
dot.render('file', view=True)
