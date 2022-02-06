import sys
import time


gen = (i for i in range(10000))
mylist = [i for i in range(10000)]

print(sys.getsizeof(gen))
print(sys.getsizeof(mylist))
