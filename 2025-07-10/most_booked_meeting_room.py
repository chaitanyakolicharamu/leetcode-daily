import heapq

class Solution:
    def mostBooked(self, n, meetings):
        # Sort meetings by start time
        meetings.sort(key=lambda x: x[0])
        
        # Min-heap of available rooms
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # Busy rooms: (end_time, room_number)
        busy_rooms = []
        
        # Count of meetings handled by each room
        count = [0] * n
        
        for start, end in meetings:
            duration = end - start
            
            # Free rooms that are done by 'start'
            while busy_rooms and busy_rooms[0][0] <= start:
                end_time, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                count[room] += 1
                heapq.heappush(busy_rooms, (start + duration, room))
            else:
                # Get earliest available room
                end_time, room = heapq.heappop(busy_rooms)
                count[room] += 1
                heapq.heappush(busy_rooms, (end_time + duration, room))
        
        # Return the room with most meetings (tie-breaker: smallest room number)
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
