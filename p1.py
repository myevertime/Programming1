def max3(n1,n2,n3):
    if n1 > n2 and n1 > n3 :
        maxn = n1
    elif n1 < n2 and n2 > n3 :
        maxn = n2
    elif n1 < n3 and n2 < n3:
        maxn = n3
    return maxn

print('The Biggest:', max3(4,-9,10))
