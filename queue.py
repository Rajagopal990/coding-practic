queue = []

n = int(input("Enter number of elements: "))

# Enqueue
for i in range(n):
    x = int(input("Enter element: "))
    queue.append(x)

print("Queue:", queue)

# Enqueue operation
x = int(input("Enter element to insert: "))
queue.append(x)
print("After Enqueue:", queue)

# Dequeue operation
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Deleted element:", queue.pop(0))

# Front operation
if len(queue) > 0:
    print("Front element:", queue[0])

# Rear operation
if len(queue) > 0:
    print("Rear element:", queue[-1])

# Display
print("Final Queue:", queue)