

def is_anagram(s1,s2):

    count1={}
    count2={}

    for ch in s1:
        if ch in count1:
            count1[ch]+=1
        else:
            count1[ch]=1
    for ch in s2:
        count2[ch]=count2.get(ch,0)+1

    if count1==count2:
        return "anagrams"
    else:
        return "not anagrams"

s1=input("Enter the 1st word:").strip().lower()
s2=input("Enter the 2nd word:").strip().lower()

result=is_anagram(s1,s2)
print(result)