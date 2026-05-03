import json
import matplotlib.pyplot as plt

try:
    with open('results_part3.json', 'r') as f:
        results_dict = json.load(f)
except Exception as e:
    print("Error cargando el JSON:", e)
    exit(1)

columns = ["Maze", "Algorithm", "Nodes expanded", "Path length"]
data = []

mazes = ["mazeA", "mazeB", "mazeC"]
algos = ["DFS", "BFS", "UCS", "A*"]

for maze in mazes:
    for algo in algos:
        key = f"{maze}_{algo}"
        if key in results_dict:
            item = results_dict[key]
            data.append([item["Maze"], item["Algorithm"], item.get("Nodes expanded", "N/A"), item.get("Path length", "N/A")])

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.4)

for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#5A8E7A') # Verde elegante
    elif row % 4 == 0: # Separador visual por laberinto
        cell.set_edgecolor('#333333')

plt.title("Algorithm Comparison (Part 3: Custom Mazes)", fontweight="bold", pad=20)
plt.savefig("part3_results_table.png", bbox_inches="tight", dpi=300)
print("Tabla guardada como 'part3_results_table.png'")
plt.show()