def isPalindrome(s):
    return s == s[::-1]#draait het woord om

# Driver code
s = "abcde"
ans = isPalindrome(s)
print(s[::-1])

if ans:
    print("Yes")
else:
    print("No")
