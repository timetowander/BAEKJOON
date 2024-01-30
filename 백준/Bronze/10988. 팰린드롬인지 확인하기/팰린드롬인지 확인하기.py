text = list(input())
mok = len(text) // 2  # 몫

def is_pal(text):

    for i in range(mok):
        if text[i] != text[len(text)-i-1]:
            return False

    return True


result = is_pal(text)

if result == True:
    print(1)
else:
    print(0)