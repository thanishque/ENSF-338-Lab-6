import random
import timeit


class BinarySearchTree:
    def __init__(num):
        num.root = None

    def insert(num, key):
        num.root = num._recursion_insert(num.root, key)

    def _recursion_insert(num, root, key):
        if root is None:
            return TreeNode(key)
        if key < root.key:
            root.left = num._recursion_insert(root.left, key)
        else:
            root.right = num._recursion_insert(root.right, key)
        return root

    def search(num, key):
        return num._rescursion_search(num.root, key)

    def _rescursion_search(num, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return num._rescursion_search(root.left, key)
        return num._rescursion_search(root.right, key)


class TreeNode:
    def __init__(num, key):
        num.key = key
        num.left = None
        num.right = None


def binary(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def performance_binary_measure(elements):
    BinaryTree = BinarySearchTree()
    total_time = 0
    for element in elements:
        BinaryTree.insert(element)

    for element in elements:
        start_time = timeit.default_timer()
        for _ in range(10):  # 10 tries for each element
            BinaryTree.search(element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    average_time = total_time / len(elements)
    return average_time, total_time


def pressure_measuring(elements):
    sorted_elements = sorted(elements)
    total_time = 0

    for element in sorted_elements:
        start_time = timeit.default_timer()
        for _ in range(10):  # 10 tries for each element
            binary(sorted_elements, element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    average_time = total_time / len(elements)
    return average_time, total_time


if __name__ == "__main__":
    elements = list(range(10000))
    random.shuffle(elements)

    avg_binary_time, total_binary_time = performance_binary_measure(elements)

    elements_sorted = sorted(elements)

    avg_array_time, array_total_time = pressure_measuring(elements)

    # Output results
    print("BST Performance:")
    print("Average Time:", avg_binary_time)
    print("Total Time:", total_binary_time)

    print("\nArray Performance:")
    print("Average Time:", avg_array_time)
    print("Total Time:", array_total_time)

    # Discuss results
    """
    In comparison to the BST performance, the array performance is anticipated to be quicker.
    This is due to the fact that the average time complexity of O(log n) for search in a 
    balanced BST is less efficient than the time complexity of O(log n) for binary search in a sorted array.
    Furthermore, compared to tree traversal, binary search in an array usually has greater cache locality, 
    which can enhance speed even further.
    """
    #Used ChatGPT for help with the code
