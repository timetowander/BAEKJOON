import sys
input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    command = input().rstrip()
    
    #push
    if command[:4] == 'push':
        stack.append(int(command[5:]))
    
    #pop
    elif command == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    
    #size
    elif command == 'size':
        print(len(stack))

    #empty
    elif command == 'empty':
        print(1 if len(stack)==0 else 0)
    
    #top
    elif command == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
