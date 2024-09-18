def words_(string):
    words = string.split()
    count = 0
    for word in words:
        count +=1 
    return count
string = input()
print(words_(string))