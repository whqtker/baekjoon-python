import sys
input=sys.stdin.readline

string=input().strip()
bomb=list(input().strip())
stack=[]

for i in string:
    stack.append(i)
    if stack[-len(bomb):]==bomb:
        del stack[-len(bomb):]

if stack:
    print("".join(stack))
else:
    print("FRULA")