def reverse(s):
  if (len(s)<2):
    return s
  else:
    return s[-1] + reverse(s[0:len(s)-1])

str = input("Enter string: ")
reversestr = reverse(str)
print(reversestr)