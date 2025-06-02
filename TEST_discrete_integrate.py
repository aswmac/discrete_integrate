from discrete_integrate import *
import time # to give some timing information
import random # to make up random test values

LIM = 200 # the magnitude for random values
DIM = 200 # the size for random lists of random values
N = 200 # the number of random tests


print("--------------------------------FILE: TEST_discrete_inegrate.py--------------------------------")
print("this tests that the forward difference")
print("and the discrete integral are inverses")
print("of each other up to the constant term")
print("(Doing random discrete integrations would")
print(" end up giving fractions)")
print("")
print(f"Testing random magnitudes {LIM} sizes {DIM} of length {N}")
print(time.ctime())
print(time.strftime('%Y.%m.%d.%H%M%S'))
dtime = time.time()
count = 0
for i in range(N):
	y = [random.randint(-LIM, LIM) for _ in range(DIM)]
	y1 = polyFromShift(y, 1)
	yd = [y1[i] - y[i] for i in range(len(y))]
	#print(yd)
	yy = discreteIntegrate(yd)
	for j in range(1, DIM):
		diff = y[j] - yy[j]
		if diff != 0: print(".", end="")
		else: count = count + 1
	#print(y)
	#print(yy)

dtime = time.time() - dtime
print("Time taken overall:", dtime)
print("Total values checked and good:", count)
