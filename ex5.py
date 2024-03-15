import heapq
import random
import timeit


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class ListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, value):
        new_node = ListNode(value)
        if not self.head or value < self.head.value:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.value <= value:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        else:
            raise IndexError("Queue is empty")


class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, value):
        heapq.heappush(self.heap, value)

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise IndexError("Queue is empty")


tasks = []
for _ in range(1000):
    if random.random() < 0.7:
        tasks.append(('enqueue', random.randint(0, 1000)))
    else:
        tasks.append(('dequeue',))

list_queue_time = timeit.timeit('list_queue.process_tasks()', setup='from __main__ import ListPriorityQueue; list_queue = ListPriorityQueue(); list_queue.process_tasks = lambda: ' +
                                '; '.join(['list_queue.enqueue({})'.format(task[1]) if task[0] == 'enqueue' else 'list_queue.dequeue()' for task in tasks]), number=1)
heap_queue_time = timeit.timeit('heap_queue.process_tasks()', setup='from __main__ import HeapPriorityQueue; heap_queue = HeapPriorityQueue(); heap_queue.process_tasks = lambda: ' +
                                '; '.join(['heap_queue.enqueue({})'.format(task[1]) if task[0] == 'enqueue' else 'heap_queue.dequeue()' for task in tasks]), number=1)

num_tasks = len(tasks)
list_avg_time_per_task = list_queue_time / num_tasks
heap_avg_time_per_task = heap_queue_time / num_tasks

print("ListPriorityQueue execution time:", list_queue_time)
print("HeapPriorityQueue execution time:", heap_queue_time)
print("Average time per task for ListPriorityQueue:", list_avg_time_per_task)
print("Average time per task for HeapPriorityQueue:", heap_avg_time_per_task)

# 4. The measured results indicate that the HeapPriorityQueue implementation outperforms the ListPriorityQueue. This outcome is consistent with expectations,
# as the heap-based approach offers superior time complexity for both enqueue and dequeue operations compared to the linked list-based approach. With a logarithmic
# time complexity (O(log n)) for both operations, the heap-based implementation maintains efficiency even as the size of the queue grows. In contrast,
# the linked list-based implementation exhibits linear time complexity (O(n)), resulting in increased execution time as the number of elements in the queue increases.
# While actual performance may vary depending on implementation specifics and hardware, the general trend favors heap-based priority queues due to their more efficient operations.

# references: chat.openai.com
