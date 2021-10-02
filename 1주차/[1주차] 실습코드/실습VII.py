def max3(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3:
        return n2
    else:
        return n3

def min3(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n3:
        return n2
    else:
        return n3

def max_and_min(n1, n2, n3):
    return max3(n1, n2, n3), min3(n1, n2, n3)

n1, n2, n3 = map(int, input('3 수를 입력하시오 : ').split())
maximum, minimum = max_and_min(n1, n2, n3)
print('가장 큰 수 :', maximum)
print('가장 작은 수 :', minimum)
