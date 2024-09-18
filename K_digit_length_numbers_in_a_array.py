def digits(num):
    if num == 0:
        return 1
    count = 0
    num = abs(num)  
    while num != 0:
        num //= 10
        count += 1
    return count

def elements(arr,k):
    element = sum( 1 for i in arr if digits(i) == k )
    return element

size , k = map(int,input().split())  
arr = list(map(int, input().split()))  
print(elements(arr,k))
