#!/bin/bash

{
echo "{"
is_first=true

for algo in "dfs" "bfs" "ucs" "astar,heuristic=manhattanHeuristic"; do
    if [ "$is_first" = true ]; then
        is_first=false
    else
        echo "    ,"
    fi
    
    # Ejecutamos en texto. En un mapa normal de coste 1, Path Cost == Path Length
    output=$(python pacman.py -l customMaze -p SearchAgent -a fn=$algo -t 2>/dev/null)
    cost=$(echo "$output" | grep "Path found with total cost of" | awk '{print $7}')
    nodes=$(echo "$output" | grep "Search nodes expanded:" | awk '{print $4}')
    
    algo_name=$algo
    if [ "$algo" = "astar,heuristic=manhattanHeuristic" ]; then algo_name="A*"; fi
    if [ "$algo" = "dfs" ]; then algo_name="DFS"; fi
    if [ "$algo" = "bfs" ]; then algo_name="BFS"; fi
    if [ "$algo" = "ucs" ]; then algo_name="UCS"; fi
    
    echo "    \"$algo_name\": {"
    echo "      \"Algorithm\": \"$algo_name\","
    echo "      \"Maze\": \"customMaze\","
    echo "      \"Nodes expanded\": ${nodes:-null},"
    echo "      \"Path length\": ${cost:-null}"
    echo -n "    }"
done
echo ""
echo "}"
} > result_part.json

echo "¡Análisis completado! Datos guardados en result_part.json"