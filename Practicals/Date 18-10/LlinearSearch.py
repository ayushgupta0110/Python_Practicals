def linearSearch(l,key):
  for i in range(len(l)):
    if key==l[i]:
      return i
  return -1

def main():
  list1 = [1,4,4,2,5,-3,6,2]
  i = linearSearch(list1,4)
  j = linearSearch(list1,-4)
  k = linearSearch(list1,-3)
  print(i,j,k)

if __name__ == '__main__':
    main()
