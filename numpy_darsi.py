import time
import numpy as np
import pandas as pd


my_list = list(range(100000))
my_array = np.array(range(100000))

start_time = time.perf_counter()
for _ in range(10):
	[x * 2 for x in my_list]
list_time = time.perf_counter() - start_time

start_time = time.perf_counter()
for _ in range(10):
	my_array * 2
array_time = time.perf_counter() - start_time





print(f"List time: {list_time:.6f} seconds")
print(f"NumPy array time: {array_time:.6f} seconds")


