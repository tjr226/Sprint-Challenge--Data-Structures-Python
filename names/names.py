import time
from binary_search_tree import BinarySearchTree
from max_heap import Heap
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []



# fourth attempt code, heap
# names_1_heap = Heap()
# names_2_heap = Heap()

# for i in names_1:
#     names_1_heap.insert(i)
# for j in names_2:
#     names_2_heap.insert(j)

# i_max = names_1_heap.get_max()
# j_max = names_2_heap.get_max()

# while i_max is not None and j_max is not None:
#     if i_max == j_max:
#         duplicates.append(i_max)
#         i_max = names_1_heap.delete()
#         j_max = names_2_heap.delete()
#     elif i_max < j_max:
#         j_max = names_2_heap.delete()
#     elif j_max < i_max:
#         i_max = names_1_heap.delete()




# third attempt code
# names_1_tree = BinarySearchTree(names_1[0])
# names_2_tree = BinarySearchTree(names_2[0])

# for j in names_2[1:]:
#     names_2_tree.insert(j)

# for i in names_1:
#     if names_2_tree.contains(i):
#         duplicates.append(i)

# second attempt code
# names_1.sort()
# names_2.sort()
# i is iterable var for names_1
# j is iterable var for names_2
# i = 0
# j = 0

# while i < len(names_1) and j < len(names_2):
#     # print(f"i, j, {i}, {j}")
#     # print(names_1[i], names_2[sj])
#     if names_1[i] == names_2[j]:
#         duplicates.append(names_1[i])
#         i += 1
#         j += 1
#     elif names_1[i] < names_2[j]:
#         i += 1
#     elif names_1[i] > names_2[j]:
#         j += 1

# code for original, then 1st attempt
# for name_1 in names_1:
    # 1st attempt
    # if name_1 in names_2:
    #     duplicates.append(name_1)

    # ORIGINAL
    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

