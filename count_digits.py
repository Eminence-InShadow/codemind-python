def digits(num):
    if num == 0:
        return 1
    count = 0
    num = abs(num)  
    while num != 0:
        num //= 10
        count += 1
    return count

def elements(arr):
    new = []
    for i in arr:
        l = digits(i)
        new.append(l)
    return new

size =int(input())  
arr = list(map(int, input().split()))  
print(" ".join(map(str,elements(arr))))
