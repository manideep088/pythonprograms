#anagram--> two strings are equal or not

#1. using sorted method

def check(s1,s2):
    if(sorted(s1)==sorted(s2)):
        print("the given strings are anagram")
    else:
        print("the given strings are not anagram")

s1=str(input("enter first string: "))
s2=str(input("enter second string: "))
check(s1,s2)