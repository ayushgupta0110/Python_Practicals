# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup


# Driver Code
tuples = ('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')
print(Reverse(tuples))
