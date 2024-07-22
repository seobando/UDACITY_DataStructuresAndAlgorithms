import heapq
import math

def squared_euclidean_distance(start, end):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    return math.sqrt(dx * dx + dy * dy)

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    total_path.reverse()
    return total_path

def shortest_path(M, start, goal):
    print("shortest path called")
    
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_score = {node: float('inf') for node in M.intersections}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in M.intersections}
    f_score[start] = squared_euclidean_distance(M.intersections[start], M.intersections[goal])
    
    while open_list:
        current_f_score, current = heapq.heappop(open_list)
        
        if current == goal:
            return reconstruct_path(came_from, current)
        
        for neighbor in M.roads[current]:
            tentative_g_score = g_score[current] + squared_euclidean_distance(M.intersections[current], M.intersections[neighbor])
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + squared_euclidean_distance(M.intersections[neighbor], M.intersections[goal])
                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None

