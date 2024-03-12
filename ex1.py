import random
import timeit


class TNode:
    def __init__(num, key):
        num.key = key
        num.left = None
        num.right = None


class BinarySearchTree:
    def __init__(num):
        num.root = None

    def insert(num, key):
        num.root = num._recursive_insertion(num.root, key)

    def _recursive_insertion(num, root, key):
        if root is None:
            return TNode(key)
        if key < root.key:
            root.left = num._recursive_insertion(root.left, key)
        else:
            root.right = num._recursive_insertion(root.right, key)
        return root

    def search(num, key):
        return num._recursive_search(num.root, key)

    def _recursive_search(num, root, key):
        if root is None or root.key == key:
            return root is not None
        if key < root.key:
            return num._recursive_search(root.left, key)
        return num._recursive_search(root.right, key)


def _performance_measuring(tree, elements):
    total_time = 0
    for element in elements:
        start_time = timeit.default_timer()
        for _ in range(10): 
            tree.search(element)
        end_time = timeit.default_timer()
        total_time += end_time - start_time
    average_time = total_time / len(elements)
    return average_time, total_time


if __name__ == "__main__":
    vector = list(range(10000))
    bst = BinarySearchTree()

    for element in vector:
        bst.insert(element)

    avg_time_sorted, total_time_sort = _performance_measuring(bst, vector)

    random.shuffle(vector)

    bst.root = None 
    for element in vector:
        bst.insert(element)

    avg_time_shuffled, total_time_shuffled = _performance_measuring(bst, vector)


    print("Search Performance on Sorted Vector:")
    print("Average Time:", avg_time_sorted)
    print("Total Time:", total_time_sort)

    print("\nSearch Performance on Shuffled Vector:")
    print("Average Time:", avg_time_shuffled)
    print("Total Time:", total_time_shuffled)

    # Question 4
    """
    It is expected that the shuffled vector will perform better in searches than the sorted vector. 
    thus is because building a BST with a sorted list yields a degenerate tree, which is really a linked list, 
    and thus has an O(n) worst-case search time complexity. The search efficiency is improved with an average 
    time complexity of O(log n) when the vector is shuffled, since this introduces unpredictability and results in a more balanced tree.
    """
#Used ChatGPT for help with code