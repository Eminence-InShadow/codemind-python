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
    Max = max(digits(i) for i in arr)
    element = [i for i in arr if digits(i) == Max]
    return element

size = int(input())  
arr = list(map(int, input().split()))  
print(" ".join(map(str, elements(arr))))
