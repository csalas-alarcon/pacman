import json
import matplotlib.pyplot as plt

# 1. Leer los datos del archivo JSON
try:
    with open('results.json', 'r') as f:
        results_dict = json.load(f)
except FileNotFoundError:
    print("Error: No se encuentra 'results.json'. Asegúrate de haber guardado ahí la salida del bash.")
    exit(1)
except json.JSONDecodeError:
    print("Error: El archivo 'results.json' tiene un formato inválido. Revisa que no haya texto sobrante al final.")
    exit(1)

# 2. Transformar el diccionario JSON en una lista plana para matplotlib
columns = ["Algorithm", "Maze", "Nodes expanded", "Path length"]
data = []

# Forzamos el orden de los laberintos para que quede bonito
mazes_order = ["tinyMaze", "mediumMaze", "bigMaze"]

for algo in ["DFS", "BFS"]:
    if algo in results_dict:
        for maze in mazes_order:
            if maze in results_dict[algo]:
                metrics = results_dict[algo][maze]
                nodes = metrics.get("Nodes expanded", "N/A")
                path_length = metrics.get("Path length", "N/A")
                data.append([algo, maze, nodes, path_length])

# 3. Configuración y renderizado de la tabla con Matplotlib
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center')

# Estilo
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.5)

# Color de la cabecera
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#4C72B0')

plt.title("Search Algorithms Comparison (Part 1)", fontweight="bold", pad=20)

# Guardar y mostrar
plt.savefig("search_results_table.png", bbox_inches="tight", dpi=300)
print("Tabla generada a partir de results.json y guardada como 'search_results_table.png'")
