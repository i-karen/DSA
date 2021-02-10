import sys

n = 50

data = []
## demo to view that byte allocation happens in chunks
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)

    print('Length: {0:3d}; Size in bytes: {1:4d}'.format(a,b))

    data.append(n)
