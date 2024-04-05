import random
import time
import math
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

class AVLNode:
    def __init__(self, data, parent=None) -> None:
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None
        
        
class AVLTree:
    def __init__(self) -> None:
        self.__root = None
        
        
    def insert(self, data):
        if not self.__root:
            self.__root = AVLNode(data)
            
        else:
            self.__insert_data(data, self.__root)
    
    def __insert_data(self, data, node):
        if data < node.data:
            if node.left:
                self.__insert_data(data, node.left)
            
            else:
                node.left = AVLNode(data, node)                
                self.__violation_handler(node.left)
        
        if data > node.data:
            if node.right:
                self.__insert_data(data, node.right)
            else:
                node.right = AVLNode(data, node)
                self.__violation_handler(node.right)
    
    
    def __violation_handler(self, node):
        while node:
            node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
            self.__violation_fix(node)
            node = node.parent

    def __calculate_height(self, node):
        if not node:
            return -1
        return node.height
    
    def __violation_fix(self, node):
        if self.__balance_factor(node) > 1:
            if self.__balance_factor(node.left) < 0:
                self.__rotation_left(node.left)
            self.__rotation_right(node)
            
        if self.__balance_factor(node) < -1:
            if self.__balance_factor(node.right) > 0:
                self.__rotation_right(node.right)
            self.__rotation_left(node)
            
            
    def __balance_factor(self, node):
        if not node:
            return 0
        return self.__calculate_height(node.left) - self.__calculate_height(node.right)

    def __rotation_left(self, node):
        temp_right_node = node.right
        t = node.right.left
        
        temp_right_node.left = node
        node.right = t

        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node
        if t:
            t.parent = node
        
        if temp_right_node.parent:
            if temp_right_node.parent.left == node:
                temp_right_node.parent.left = temp_right_node
            elif temp_right_node.parent.right == node:
                temp_right_node.parent.right = temp_right_node
        else:
            self.__root = temp_right_node
            
            
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_right_node.height =  max(self.__calculate_height(temp_right_node.left), self.__calculate_height(temp_right_node.right)) + 1
        
        

        
    def __rotation_right(self, node):
        temp_left_node = node.left
        t = node.left.right
        
        temp_left_node.right = node
        node.left = t
        
        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node
        
        if t:
            t.parent = node
            
        if temp_left_node.parent:
            if temp_left_node.parent.left == node:
                temp_left_node.parent.left = temp_left_node
            elif temp_left_node.parent.right == node:
                temp_left_node.parent.right = temp_left_node
                
        else:
            self.__root = temp_left_node
        node.height = max(self.__calculate_height(node.left), self.__calculate_height(node.right)) + 1
        temp_left_node.height =  max(self.__calculate_height(temp_left_node.left), self.__calculate_height(temp_left_node.right)) + 1
        
        
        
        
    def traverse(self):
        if self.__root:
            self.__in_order(self.__root)
            
    def __in_order(self, node):
        if node.left:
            self.__in_order(node.left)
            
        print(node.data)
        
        if node.right:
            self.__in_order(node.right)
            
            
def run_key_insertion_avl_tree(binary_tree, keys):
    start_time = time.time()
    for key in keys:
        binary_tree.insert( key)
    return (time.time() - start_time) * 1e6
            
def run_key_insertion_binary_tree(binary_tree, keys):
    start_time = time.time()
    for key in keys:
        node = Node(key)
        binary_tree.insert(node, key)
    return (time.time() - start_time) * 1e6

def run_key_BEST_CASE_binary_tree(binary_tree, keys, start, end):
    if start > end:
        return 
    
    middle = (start + end) // 2
    node = Node(keys[middle])
    binary_tree.insert(node, keys[middle])
    run_key_BEST_CASE_binary_tree(binary_tree, keys, start, middle - 1)
    run_key_BEST_CASE_binary_tree(binary_tree, keys, middle + 1, end)
    

def graph_measuring(measure_sizes):
    binary_tree_times = []
    avl_tree_times = []
    binary_tree_BestCase_times = []
    set_times = []
    
    
    for data_size in measure_sizes:
        random_keys = [random.randint(1, data_size) for _ in range(data_size)]
        best_case_keys = list(range(1, data_size + 1))
        binary_tree = BinaryTree()
        avl_tree = AVLTree()
        binary_tree_BestCase = BinaryTree()
        set_cont = set()
        
        binary_tree_time = 0
        avl_tree_time = 0
        set_cont_time = 0
        binary_tree_BestCase_time = 0
        
        binary_tree_time = run_key_insertion_binary_tree(binary_tree, random_keys)
        avl_tree_time = run_key_insertion_avl_tree(avl_tree, random_keys)
        
        
        start_time_best_case = time.time()
        run_key_BEST_CASE_binary_tree(binary_tree_BestCase, best_case_keys, 0, data_size - 1)
        best_case_time = (time.time() - start_time_best_case) * 1e6
        binary_tree_BestCase_time = best_case_time
        
        start_time = time.time()
        for key in random_keys:
            set_cont.add(key)
        set_cont_time = (time.time() - start_time) * 1e6
        binary_tree_times.append(binary_tree_time)
        binary_tree_BestCase_times.append(binary_tree_BestCase_time)
        
        avl_tree_times.append(avl_tree_time)
        set_times.append(set_cont_time)
    

    plt.figure(figsize=(10, 6))

    plt.plot(measure_sizes, binary_tree_times, marker='o', label='Binary Tree (Random order)')
    plt.plot(measure_sizes, avl_tree_times, marker='o', label='AVL Tree (Random Order)')
    plt.plot(measure_sizes, binary_tree_BestCase_times, marker='o', label='Binary Tree(Best Case Order)')
    plt.plot(measure_sizes, set_times, marker='o', label='Set')

    plt.title('Insertion Time Comparison')
    plt.xlabel('Data Size')
    plt.ylabel('Time (nanoseconds)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
