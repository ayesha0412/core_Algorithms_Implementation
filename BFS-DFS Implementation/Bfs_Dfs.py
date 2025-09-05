from collections import deque
graph={
    'A':['B','C']
    ,'B':['A','D','E']
    ,'C':['A','F']
    ,'D':['B']
    ,'E':['B']
    ,'F':['C']

}
def breath_first_search(graph, start, goal):
    visited=set( )
    queue=deque([start])
    visited.add(start)

    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        if node==goal:
            print("\nGoal found:",goal)
            return
breath_first_search(graph,'A','E')



# def BFS(graph, start, goal):
#     queue = deque([[start]])
#     visited = set()
#     if start == goal:
#         print("Goal found:", goal)
#         return
#     while queue:
#         path = queue.popleft()
#         node = path[-1]
#         if node == goal:
#             print("Goal found:", goal)
#             print("Path:", '->'.join(path))
#             return
#         if node not in visited:
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     new_path = list(path)
#                     new_path.append(neighbor)
#                     queue.append(new_path)
#     return None

# BFS(graph, 'A', 'E')
