"""Програма стрворення та візуалізації графу з використанням даних файлу
cities.csv"""
import networkx as nx
import matplotlib.pyplot as plt


with open('cities.csv', "r") as file:
    all_words = []
    for line in file:
        a = file.readline()
        x = a.replace('\n', '').split(";")
        all_words.append(x)


g = nx.Graph()
for edge in all_words:
    g.add_edge(edge[0], edge[1], weight=edge[2])

print(nx.shortest_path(g, 'Dnipro', 'Odesa', weight=''))
print(nx.shortest_path_length(g, 'Dnipro', 'Odesa', weight=''))


pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Graph Generation")


nx.draw_networkx(g)
plt.show()
