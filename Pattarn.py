def pattarn(n):
    if (n==0):
        return
    print("*"*n)
    pattarn(n-1)
    return n


pattarn(5)

