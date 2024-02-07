from itertools import combinations
import random

N=9

list01 = []

for i in range(N):
    list01.append(int(input()))

#print(list01)

result =list(combinations(list01, 7))
#print(result)


for i in range(len(result)):
    if sum(result[i]) == 100:
        print(*sorted(result[i]), sep = '\n')

        break