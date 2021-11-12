def main():
    n=int(input('Number of Subjects: '))
    totalMarks = 0
    print('Enetr marks')
    for i in range(1,n+1):
        marks=float(input('Subject' +str(i) +':'))
        totalMarks += marks

    percentage = totalMarks / n
    print('Percentage is: ', percentage)

if __name__=='__main__':
    main()