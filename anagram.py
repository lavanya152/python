st1 = input("Enter string1:").lower()
st2 = input("Enter string2:").lower()
if len(st1)==len(st2):
    s1 = sorted(list(st1))
    s2 = sorted(list(st2))
    if s1 == s2:
        print(st1 +" and "+st2 +" are anagrams")
    else:
        pass
else:
    print(st1 +" and "+st2+ " are not anagrams")
