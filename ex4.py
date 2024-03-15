import unittest
from random import shuffle


class Heap:
    def __init__(self):
        self.heap = []

    def heapify(self, array):
        self.heap = array[:]
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)

    def enqueue(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] <= self.heap[parent_index]:
                break
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def _heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < n and self.heap[left_child_index] > self.heap[largest]:
                largest = left_child_index

            if right_child_index < n and self.heap[right_child_index] > self.heap[largest]:
                largest = right_child_index

            if largest == index:
                break

            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            index = largest


class TestHeap(unittest.TestCase):
    def setUp(self):
        self.heap = Heap()

    def test_heapify_sorted_heap(self):
        input_array = [1, 2, 3, 4, 5]
        expected_output = [5, 4, 3, 1, 2]
        self.heap.heapify(input_array)
        self.assertEqual(self.heap.heap, expected_output)

    def test_heapify_empty_array(self):
        input_array = []
        expected_output = []
        self.heap.heapify(input_array)
        self.assertEqual(self.heap.heap, expected_output)

    def test_heapify_random_shuffle(self):
        input_array = list(range(1, 101))
        shuffle(input_array)
        expected_output = sorted(input_array, reverse=True)
        self.heap.heapify(input_array)
        self.assertEqual(self.heap.heap, expected_output)


if __name__ == '__main__':
    unittest.main()
