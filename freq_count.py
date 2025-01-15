def freq_count(string):
    freq={}
    words=string.lower().split()

    for char in words:
        if char in freq:
            freq[char] +=1
        else:
            freq[char]=1


    most_repeated=max(freq,key=freq.get)
    return most_repeated,freq[most_repeated]

count=freq_count("Madam is not a madam")
print(count)


# def char_frequency(s):
#     frequen = {}
#     for char in s:
#         frequen[char] = frequen.get(char, 0) + 1
#     return frequen

# Example
#print(char_frequency("testing"))