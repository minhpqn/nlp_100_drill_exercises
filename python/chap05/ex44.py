# -*- coding: utf-8 -*-

""" 44. Visualize cây dependency
"""
import pydot
from collections import defaultdict
import sys
from chunk_ex41 import read_chunks
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

def draw_dependency_tree(sen):
    graph = pydot.Dot(graph_type='digraph')
    nodes = []
    for i,ck in enumerate(sen):
        lb = '%d- %s' % (i, ck.surf2())
        node = pydot.Node( lb )
        nodes.append(node)
        
    for i,ck in enumerate(sen):
        j = ck.dst
        if j == -1: continue
        graph.add_edge(pydot.Edge(nodes[i], nodes[j]))

    graph.write_jpeg('dependency_tree.jpg', prog='dot')

if __name__ == '__main__':
    sentences = read_chunks()

    sen = sentences[7]
    draw_dependency_tree(sen)
    

