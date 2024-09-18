def max_length(string):
    words = string.split()
    max_len = len(words[0])
    for word in words:
        if len(word)  >  max_len:
            max_len = len(word)
    return max_len
string = input()
print(max_length(string))