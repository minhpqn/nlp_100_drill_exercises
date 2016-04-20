# -*- coding: utf-8 -*-
""" 57. Phân tích cấu trúc dependency
    Từ kết quả phân tích dependency của Stanford Core NLP
    (collapsed-dependencies), visualize câu đầu vào bằng đồ thị có hướng.
"""

import pydot
import os
import sys
import re
from xml.dom import minidom

def visualize(i, dep_nodes):
    filename = 'dependency_tree_%d.jpg' % i
    graph = pydot.Dot(graph_type='digraph')
    xmlnode = dep_nodes[i]
    dnodes = xmlnode.getElementsByTagName('dep')
    graph_nodes = {}
    for dn in dnodes:
        gov      = dn.getElementsByTagName('governor')[0]
        gov_id   = int(gov.attributes['idx'].value)
        gov_txt  = gov.firstChild.data
        gov_node = None
        if graph_nodes.has_key(gov_id):
            gov_node = graph_nodes[gov_id]
        else:
            gov_node = pydot.Node( gov_id )
            graph_nodes[gov_id] = gov_node

        dep      = dn.getElementsByTagName('dependent')[0]
        dep_id   = int(dep.attributes['idx'].value)
        dep_txt  = dep.firstChild.data
        dep_node = None
        if graph_nodes.has_key(dep_id):
            dep_node = graph_nodes[dep_id]
        else:
            dep_node = pydot.Node( dep_id )
            graph_nodes[dep_id] = dep_node

        print '\t'.join([dep_txt, gov_txt])

        graph.add_edge(pydot.Edge(dep_node, gov_node))

    graph.write(filename, prog='dot', format='jpg')
    

if __name__ == '__main__':
    xmldoc = minidom.parse('../../data/nlp.txt.xml')
    dep_nodes = []
    for node in xmldoc.getElementsByTagName('dependencies'):
        if node.attributes['type'].value == 'collapsed-dependencies':
            dep_nodes.append(node)

    visualize(0, dep_nodes)
    


    
