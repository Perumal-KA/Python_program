def isanagram(s1, s2):
    # Sort both strings
    sort_s1 = sorted(s1)
    sort_s2 = sorted(s2)

    # Compare sorted strings
    if sort_s1 == sort_s2:
        return "anagrams"
    else:
        return "not anagrams"


# Take user input
s1 = input("Enter the 1st word: ").strip().lower()
s2 = input("Enter the 2nd word: ").strip().lower()

# Check if the strings are anagrams
ans = isanagram(s1, s2)
print(ans)