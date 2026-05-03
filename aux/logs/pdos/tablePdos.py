import json
import matplotlib.pyplot as plt

# 1. Leer los datos del archivo JSON
try:
    with open('results_part2.json', 'r') as f:
        results_dict = json.load(f)
except FileNotFoundError:
    print("Error: No se encuentra 'results_part2.json'. Asegúrate de haber guardado ahí la salida del bash.")
    exit(1)
except json.JSONDecodeError:
    print("Error: El archivo 'results_part2.json' tiene un formato inválido. Revisa el contenido.")
    exit(1)

# 2. Preparar los datos
columns = ["Algorithm", "Maze", "Nodes expanded", "Path length", "Path cost"]
data = []

# Mantenemos el orden exacto usando las claves del JSON (1 al 5)
for key in ["1", "2", "3", "4", "5"]:
    if key in results_dict:
        item = results_dict[key]
        data.append([
            item["Algorithm"],
            item["Maze"],
            item.get("Nodes expanded", "N/A"),
            item.get("Path length", "N/A"),
            item.get("Path cost", "N/A")
        ])

# 3. Renderizar la tabla
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')

table = ax.table(cellText=data, colLabels=columns, cellLoc='center', loc='center')

# Estilo
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.8)  # Celdas más altas para respirar mejor

# Colores (Inspirado en tu imagen)
for (row, col), cell in table.get_celld().items():
    if row == 0:
        # Cabecera
        cell.set_text_props(weight='bold', color='#333333')
        cell.set_facecolor('#FDE9D9') # Color melocotón pastel
    else:
        # Cuerpo
        cell.set_facecolor('#FFF5EB') # Color crema muy suave
    
    # Bordes sutiles
    cell.set_edgecolor('#E5D0C0')

plt.title("Search Algorithms Comparison (Part 2: Costs & Heuristics)", fontweight="bold", pad=20)

# Guardar y mostrar
plt.savefig("part2_results_table.png", bbox_inches="tight", dpi=300)
print("¡Éxito! Tabla generada y guardada como 'part2_results_table.png'")
