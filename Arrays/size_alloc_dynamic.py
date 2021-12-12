import sys
# set n no of elements
n = 10

data = []

for i in range(n):
    # Number of elements
    a = len(data)
    #size in bytes
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes:{1:4d}".format(a, b))

    # increase len by 1
    data.append(n)
