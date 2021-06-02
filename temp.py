from queue import PriorityQueue

q = PriorityQueue()

q.put((4, 2))
q.put((2, 3))
q.put((5, 1))
q.put((1, 4))
q.put((3, 5))

while not q.empty():
    next_item = q.get()
    print(next_item)