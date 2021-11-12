#   Counting Vowels

str = "Encyclopedia"
vowels = "AEIOUaeiou"
vowelCount = 0

for ch in vowels:
    vowelCount += str.count(ch)

print(f"No. of vowels in {str} is {vowelCount}")

#   rfind() and find()

colors = "red, green, blue, yellow, black"

print(colors.rfind('red'))
print(colors.find('red'))

print(colors.find('black'))
print(colors.rfind('black'))

#   split() and partition()

colours = "Red, Green, Blue, Orange, Yellow, Cyan"

print(colours.split(','))   #   returns a LIST, with separated colour names
print(colours.partition(','))   #   returns a TUPLE, with separated colour names

#   join()

print(' > '.join(['I', 'am', 'ok']))
print(' '.join(('I', 'am', 'ok')))
print(' > '.join("'I', 'am', 'ok'"))

#   String Slicing

String = "I love Python programming language and Computer Science course"
  
print(String[:18]) 
print(String[1:27:2])  
print(String[-1:-25:-2])    

#   max() and min()

strList = ["Harry", "John", "Apple", "Microsoft", "Redmi", "Realme", "Oneplus", "Okay"]

print(f"The word from this list that would occur FIRST in dictionary is {min(strList)}")
print(f"The word from this list that would occur LAST in dictionary is {max(strList)}")
