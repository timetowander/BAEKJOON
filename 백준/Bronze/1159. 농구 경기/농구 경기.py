N=int(input()) # N개의 행
arr=[input() for _ in range(N)]

#print(arr)

list_first =[]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        list_first.append(arr[i][0])
        break

#print(list_first)

alphabet =[0 for _ in range(26)]


for m in list_first:
    #print(ord(m) - 97)
    alphabet[ord(m)-97] += 1

#print(alphabet)

name=[]
for k in range(len(alphabet)):

    if alphabet[k] >= 5:
        name.append(chr(k+97))
        #print(name)




if len(name) != 0:
    print("".join(name))

else :
    print("PREDAJA")

