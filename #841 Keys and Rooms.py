def unlock(rooms,visited,i):
    visited[i] = True
    for j in rooms[i]:
        if visited[j]==False:
            visited = unlock(rooms,visited,j)
    return visited

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited = [False for i in range(n)]
        
        visited = unlock(rooms,visited,0)

        for i in visited:
            if i==False:
                return False
        return True
