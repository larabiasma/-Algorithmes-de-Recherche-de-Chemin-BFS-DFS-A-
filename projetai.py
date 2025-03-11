import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

class GraphSearch:
    def __init__(self):
        # ✅ Graphe fourni
        self.graph = {
            'A': ['1'], '1': ['2'], '2': ['3', '4'], '3': ['5'],
            '5': ['6', '7'], '6': ['8'], '7': ['9'], '4': ['10'],
            '10': ['11', '12'], '12': ['13'], '13': ['14'],
            '14': ['15', '17'], '17': ['18', '20'], '18': ['19'],
            '20': ['21'], '21': ['B'], '15': ['16', '14']
        }
        
        # ✅ Heuristique fournie
        self.heuristic = {
            'A': 8, '1': 6, '2': 6, '3': 6, '4': 7, '5': 4, '6': 12,
            '7': 7, '8': 15, '9': 18, '10': 6, '11': 8, '12': 6, '13': 5,
            '14': 4, '15': 8, '16': 6, '17': 3, '18': 5, '19': 5,
            '20': 2, '21': 1, 'B': 0
        }

    # ✅ BFS : Parcours en largeur 
    def bfs(self, start, goal):
        queue = [[start]]
        visited = set()

        while queue:
            path = queue.pop(0)  # FIFO
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)  # ✅ Ajout du nœud visité

                for neighbor in sorted(self.graph.get(node, [])):
                    if neighbor not in visited:  # ✅ Vérification avant ajout
                        queue.append(path + [neighbor])  # ✅ Ajout correct

        return None  # ✅ Si aucun chemin trouvé

    # ✅ DFS : Parcours en profondeur 
    def dfs(self, start, goal):
        stack = [[start]]
        visited = set()

        while stack:
            path = stack.pop()  # LIFO
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)  # ✅ Ajout du nœud visité

                for neighbor in sorted(self.graph.get(node, []), reverse=True):
                    if neighbor not in visited:  # ✅ Vérification avant ajout
                        stack.append(path + [neighbor])  # ✅ Ajout correct

        return None  # ✅ Si aucun chemin trouvé

    # ✅ A* : Recherche heuristique optimisée
    def astar(self, start, goal):
        queue = PriorityQueue()
        queue.put((self.heuristic[start], [start]))  # 🔥 Coût initial = heuristique
        visited = {}

        while not queue.empty():
            cost, path = queue.get()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited or cost < visited[node]:  
                visited[node] = cost
                for neighbor in self.graph.get(node, []):
                    new_path = path + [neighbor]
                    new_cost = len(new_path) + self.heuristic.get(neighbor, 0)  # 🔥 Distance + heuristique
                    queue.put((new_cost, new_path))

        return None  # ✅ Si aucun chemin trouvé

    # ✅ Affichage du graphe non orienté
    def draw_graph(self, path, title):
        G = nx.Graph()  # 🔥 Graph non orienté
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)  # 🔥 Disposition naturelle
        plt.figure(figsize=(10, 6))

        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)

        if path:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red", node_size=2200)

        plt.title(title)
        plt.show()

# ✅ Exécution et affichage des résultats
if __name__ == "__main__":
    search = GraphSearch()

    bfs_solution = search.bfs('A', 'B')
    dfs_solution = search.dfs('A', 'B')
    astar_solution = search.astar('A', 'B')

    print("Solution BFS:", bfs_solution)
    print("Solution DFS:", dfs_solution)
    print("Solution A* :", astar_solution)

    # 🔥 Affichage des graphes
    search.draw_graph(bfs_solution, "Chemin BFS")
    search.draw_graph(dfs_solution, "Chemin DFS")
    search.draw_graph(astar_solution, "Chemin A*")
import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

class GraphSearch:
    def __init__(self):
        # ✅ Graphe fourni
        self.graph = {
            'A': ['1'], '1': ['2'], '2': ['3', '4'], '3': ['5'],
            '5': ['6', '7'], '6': ['8'], '7': ['9'], '4': ['10'],
            '10': ['11', '12'], '12': ['13'], '13': ['14'],
            '14': ['15', '17'], '17': ['18', '20'], '18': ['19'],
            '20': ['21'], '21': ['B'], '15': ['16', '14']
        }
        
        # ✅ Heuristique fournie
        self.heuristic = {
            'A': 8, '1': 6, '2': 6, '3': 6, '4': 7, '5': 4, '6': 12,
            '7': 7, '8': 15, '9': 18, '10': 6, '11': 8, '12': 6, '13': 5,
            '14': 4, '15': 8, '16': 6, '17': 3, '18': 5, '19': 5,
            '20': 2, '21': 1, 'B': 0
        }

    # ✅ BFS : Parcours en largeur 
    def bfs(self, start, goal):
        queue = [[start]]
        visited = set()

        while queue:
            path = queue.pop(0)  # FIFO
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)  # ✅ Ajout du nœud visité

                for neighbor in sorted(self.graph.get(node, [])):
                    if neighbor not in visited:  # ✅ Vérification avant ajout
                        queue.append(path + [neighbor])  # ✅ Ajout correct

        return None  # ✅ Si aucun chemin trouvé

    # ✅ DFS : Parcours en profondeur 
    def dfs(self, start, goal):
        stack = [[start]]
        visited = set()

        while stack:
            path = stack.pop()  # LIFO
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)  # ✅ Ajout du nœud visité

                for neighbor in sorted(self.graph.get(node, []), reverse=True):
                    if neighbor not in visited:  # ✅ Vérification avant ajout
                        stack.append(path + [neighbor])  # ✅ Ajout correct

        return None  # ✅ Si aucun chemin trouvé

    # ✅ A* : Recherche heuristique optimisée
    def astar(self, start, goal):
        queue = PriorityQueue()
        queue.put((self.heuristic[start], [start]))  # 🔥 Coût initial = heuristique
        visited = {}

        while not queue.empty():
            cost, path = queue.get()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited or cost < visited[node]:  
                visited[node] = cost
                for neighbor in self.graph.get(node, []):
                    new_path = path + [neighbor]
                    new_cost = len(new_path) + self.heuristic.get(neighbor, 0)  # 🔥 Distance + heuristique
                    queue.put((new_cost, new_path))

        return None  # ✅ Si aucun chemin trouvé

    # ✅ Affichage du graphe non orienté
    def draw_graph(self, path, title):
        G = nx.Graph()  # 🔥 Graph non orienté
        for node, neighbors in self.graph.items():
            for neighbor in neighbors:
                G.add_edge(node, neighbor)

        pos = nx.spring_layout(G, seed=42)  # 🔥 Disposition naturelle
        plt.figure(figsize=(10, 6))

        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)

        if path:
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red", node_size=2200)

        plt.title(title)
        plt.show()

# ✅ Exécution et affichage des résultats
if __name__ == "__main__":
    search = GraphSearch()

    bfs_solution = search.bfs('A', 'B')
    dfs_solution = search.dfs('A', 'B')
    astar_solution = search.astar('A', 'B')

    print("Solution BFS:", bfs_solution)
    print("Solution DFS:", dfs_solution)
    print("Solution A* :", astar_solution)

    # 🔥 Affichage des graphes
    search.draw_graph(bfs_solution, "Chemin BFS")
    search.draw_graph(dfs_solution, "Chemin DFS")
    search.draw_graph(astar_solution, "Chemin A*")
