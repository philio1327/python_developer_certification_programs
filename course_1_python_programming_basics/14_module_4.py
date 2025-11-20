import timeit

# List lookup
list_data = list(range(100000))
lookup_value = 99999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=10000)

# Dictionary lookup
dict_data = {i: i for i in range(100000)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data, number=10000)

print("List lookup time:", list_time)
print("Dictionary lookup time:", dict_time)

from collections import deque, Counter

# Deque example
queue = deque()
queue.append("task1")
queue.append("task2")
print(queue.popleft())  # Output: task1

# Counter example
text = "This is a sample text with some repeated words words"
word_counts = Counter(text.split())
print(word_counts)  # Output: Counter({'words': 2, 'This': 1, 'is': 1, ...})