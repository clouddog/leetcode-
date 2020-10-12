import heapq

num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

heapq.heapify(num1)
heapq.nsmallest(3, num1)

sorted(num1)[-4:-1]
f = [[0] * 26 for _ in range(10)]
f.append([10] * 26)