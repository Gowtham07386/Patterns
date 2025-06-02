def rectangle(n,m):
    lst = []
    for i in range(n):
        lst.append('*' * m)
    return lst
m= int(input())
n=int(input())
pattern = rectangle(n,m)

print(pattern)    