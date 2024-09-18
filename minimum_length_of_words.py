def min_length(string):
    words = string.split()
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    return min_len
string = input()
print(min_length(string))