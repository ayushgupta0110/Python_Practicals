def sum(a=1,b=3,c=4,d=5,e=2,f=10):
    return a+b+c+d+e+f
def main():
    s=sum()
    print(s)
    s=sum(c=1,a=3)
    print(s)
if __name__=='__main__':
    main()
