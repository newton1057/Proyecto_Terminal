import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

#['Johnson, Casey Rebecca']
#
G.add_node("Egerton, Karl")
G.add_node("Capitelli-McMahon, Helen")
G.add_node("Johnson, Casey Rebecca")
G.add_node("Chirimuuta, M.")

G.add_nodes_from(['Li, Kunpeng', 'Li, Qingye', 'Lv, Liye', 'Song, Xueguan', 'Ma, Yunsheng', 'Lee, Ikjin'])


G.add_edge('Li, Kunpeng', 'Li, Qingye')
G.add_edge('Li, Kunpeng', 'Lv, Liye')
G.add_edge('Li, Kunpeng', 'Song, Xueguan')
G.add_edge('Li, Kunpeng', 'Ma, Yunsheng')
G.add_edge('Li, Kunpeng', 'Lee, Ikjin')


G.add_edge("Egerton, Karl", "Capitelli-McMahon, Helen")

nx.draw(G, with_labels=True, font_weight='bold', font_size='5', node_size=100, linewidths=2.0, alpha=0.5, label="Relations of Authors")
plt.margins(0.5, 0.5)
plt.show()  