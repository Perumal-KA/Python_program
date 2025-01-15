# def reverse_s(st):
#
#     reversed_st=""
#
#     for i in range(len(st)-1,-1,-1):   #len(st)-1---> starts at last index, -1--> enda at 0 position, -1 to reverse
#         reversed_st += st[i]
#
#     return reversed_st
#
# rev=reverse_s("perumal")
# print(rev)


def reversed_string(s):

    reversed=""

    for char in s:
        reversed=char+reversed # p+"", e+p,r+ep,u+rep,m+urep,a+murep,l+amurep
    return reversed
rev=reversed_string("perumal")
print(rev)