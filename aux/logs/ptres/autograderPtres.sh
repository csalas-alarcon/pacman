#!/bin/bash

# 2. Extraer datos
echo "{"
is_first=true

for maze in mazeA mazeB mazeC; do
    for algo in "dfs" "bfs" "ucs" "astar,heuristic=manhattanHeuristic"; do
        
        if [ "$is_first" = true ]; then
            is_first=false
        else
            echo "    ,"
        fi
        
        output=$(python pacman.py -l "$maze" -p SearchAgent -a fn=$algo -t 2>/dev/null)
        cost=$(echo "$output" | grep "Path found with total cost of" | awk '{print $7}')
        nodes=$(echo "$output" | grep "Search nodes expanded:" | awk '{print $4}')
        
        # Limpiar nombre del algoritmo para el JSON
        algo_name=$algo
        if [ "$algo" = "astar,heuristic=manhattanHeuristic" ]; then algo_name="A*"; fi
        if [ "$algo" = "dfs" ]; then algo_name="DFS"; fi
        if [ "$algo" = "bfs" ]; then algo_name="BFS"; fi
        if [ "$algo" = "ucs" ]; then algo_name="UCS"; fi
        
        echo "    \"${maze}_${algo_name}\": {"
        echo "      \"Algorithm\": \"$algo_name\","
        echo "      \"Maze\": \"$maze\","
        echo "      \"Nodes expanded\": ${nodes:-null},"
        echo "      \"Path length\": ${cost:-null}"
        echo -n "    }"
    done
done
echo ""
echo "}"