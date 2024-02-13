a = [list(map(int, input().split())) for _ in range(4)]

cost = 0
parking = [0] * 100
#print(parking)

for i in range(a[1][0]-1,a[1][1]-1):
    parking[i] += 1

#print(parking)


for i in range(a[2][0]-1,a[2][1]-1):
    parking[i] =parking[i] + 1
#print(parking)


for i in range(a[3][0]-1,a[3][1]-1):
    parking[i] = parking[i] +1
#print(parking)

cnt01 = parking.count(1)
cnt02 = parking.count(2)
cnt03 = parking.count(3)

#print(cnt01)
#print(cnt02)
#print(cnt03)

#print(a[0][0])
#
for count in parking:
    if count ==1:
        cost = cost + a[0][0]*1
    elif count ==2 :
        cost = cost + a[0][1]*2
    elif count ==3:
        cost = cost + a[0][2]*3


print(cost)

#for J in range(1,len(a[0][0])+1):
#
#
# SUM = (cnt01*5*1 + cnt02*3*2 + cnt03 * 1*3)
# print(SUM)