def strFilterations(s):
    nstr = ""
    for i in range(0, len(s)):
        if "A" <= s[i] <= "Z":
            nstr = nstr + chr(ord(s[i]) + 32)
        elif "a" <= s[i] <= "z":
            nstr=nstr+s[i]
    return nstr
def isPangram(s):
    s = strFilterations(s)
    for i in range(0, 26):
       if len(s)<26:
              return False
       else:
           dict = {}
           for i in range(0, len(s)):
               if s[i] in dict:
                   dict[s[i]] = dict[s[i]] + 1
               else:
                   dict[s[i]] = 1
           return len(dict) == 26
s=input("Enter the string: ")
flag=isPangram(s)
if flag:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")