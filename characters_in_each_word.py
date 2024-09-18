def Characters(string):
    words = string.split()
    new = []
    for word in words:
        new.append(len(word))
    return new
string = input()
print(" ".join(map(str,Characters(string))))