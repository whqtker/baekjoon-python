import sys
from collections import deque
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    ops=input().strip()
    n=int(input())
    dq=deque(input().strip()[1:-1].split(','))

    reverse_flag=False
    error_flag=False

    for op in ops:
        if op=='R':
            reverse_flag=not reverse_flag

        elif op=='D':
            if not dq or dq[0]=='':
                error_flag=True
                break
            else:
                if reverse_flag:
                    dq.pop()
                else:
                    dq.popleft()

    if error_flag:
        print("error")

    else:
        if reverse_flag:
            dq.reverse()

        print(f"[{','.join(dq)}]")
        