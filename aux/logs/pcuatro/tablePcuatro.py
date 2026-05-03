import json
import matplotlib.pyplot as plt

# 1. Cargar datos
try:
    with open('result_part.json', 'r') as f:
        results = json.load(f)
except Exception as e:
    print("Error cargando result_part.json:", e)
    exit(1)

columns = ["Maze", "Algorithm", "Nodes expanded", "Path length"]
data = []

# Mantenemos el orden lógico de los algoritmos
for algo in ["DFS", "BFS", "UCS", "A*"]:
    if algo in results:
        item = results[algo]
        data.append([item["Maze"], item["Algorithm"], item.get("Nodes expanded", "N/A"), item.get("Path length", "N/A")])

# 2. Dibujar tabla
fig, ax = plt.subplots(figsize=(8, 3))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.6)

# Estilos (Tono morado/lila para diferenciar esta Parte 3)
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(weight='bold', color='white')
        cell.set_facecolor('#6A4C93') 
    else:
        cell.set_facecolor('#F4F1F8')
        # Todo el texto del cuerpo de la tabla quedará con fuente normal

plt.title("Custom Maze", fontweight="bold", pad=20)
plt.savefig("part3_custom_maze.png", bbox_inches="tight", dpi=300)
print("¡Tabla guardada como 'part3_custom_maze.png' sin negritas extra!")
plt.show()