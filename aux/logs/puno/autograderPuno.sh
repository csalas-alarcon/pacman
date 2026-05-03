#!/bin/bash

# Función para ejecutar el juego, extraer los datos y formatearlos
extract_data() {
    local maze=$1
    local algo_args=$2
    
    # Ejecutamos en modo texto (-t) para evitar el crasheo de tkinter
    output=$(python pacman.py -l "$maze" -p SearchAgent $algo_args -t 2>/dev/null)
    
    # Extraemos los números exactos
    cost=$(echo "$output" | grep "Path found with total cost of" | awk '{print $7}')
    nodes=$(echo "$output" | grep "Search nodes expanded:" | awk '{print $4}')
    
    # Devolvemos el fragmento JSON
    echo "    \"$maze\": {"
    echo "      \"Nodes expanded\": ${nodes:-null},"
    echo "      \"Path length\": ${cost:-null}"
    echo "    }"
}

echo "{"

# Extraemos datos para DFS
echo "  \"DFS\": {"
extract_data "tinyMaze" ""
echo "    ,"
extract_data "mediumMaze" ""
echo "    ,"
extract_data "bigMaze" ""
echo "  },"

# Extraemos datos para BFS
echo "  \"BFS\": {"
extract_data "tinyMaze" "-a fn=bfs"
echo "    ,"
extract_data "mediumMaze" "-a fn=bfs"
echo "    ,"
extract_data "bigMaze" "-a fn=bfs"
echo "  }"

echo "}"
echo ""

# Ejecutamos el autograder normal al final
python autograder.py -q q1
python autograder.py -q q2