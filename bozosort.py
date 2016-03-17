import random
import time

def bozosort(L):
	start_time = time.time()

	while not sorted(L) == L:
		a, b = random.sample(range(0, len(L)), 2)
		L[a], L[b] = L[b], L[a]

	print("sorted to " + str(L) + " in %s seconds." % (time.time() - start_time))

#test
L = [4, 32, 6, 19, 18, 3, 59, 1]
bozosort(L)