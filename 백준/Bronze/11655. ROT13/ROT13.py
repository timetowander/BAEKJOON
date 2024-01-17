
def alphabet_number01(alphabet, n):
    return chr(ord("A")+(ord(alphabet) + n - ord("A"))% 26)

#print(alphabet_number("A",13))

# 질문 1 . 대문자와 소문자를 나눠서 해야하는가
# 질문 2. 쭉 입력받아서 함수에 대입할 수 있는가

def alphabet_number02(alphabet, n):
    return chr(ord("a")+(ord(alphabet) + n - ord("a"))% 26)


K = input()
my_list = list(K)
#print(K)
#print(my_list)
temp = []

for i in range(len(my_list)):
    if my_list[i].isupper() == True:

        temp.append(alphabet_number01(my_list[i], 13))
    elif my_list[i].islower() == True:
        temp.append(alphabet_number02(my_list[i], 13))

    else:
        temp.append(my_list[i])



#print(temp)


print(''.join(temp))

#print(alphabet_number01(my_list[0],13))
#print(alphabet_number02(my_list[1],13))
