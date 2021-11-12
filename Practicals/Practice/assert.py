def percent (marks, maxMarks):
    '''
    Objective: To find percentage of marks obtained in a subject
    Input Parameters: marks, maxMarks - float
    Return value: percentage - float
    '''
    percentage = (marks/ maxMarks)*100
    return percentage

def main():
    '''
    Objective: To find percentage of marks obtained in a subject
    based on user input
    Input Parameter: None
    Return value: None
    '''
    maxMarks = float (input('Enter maximum marks: '))
    assert maxMarks>=0 and maxMarks <=500
    marks = float(input('Enter marks obtained: '))
    assert marks >=0 and marks <=maxMarks
    percentage = percent (marks, maxMarks)
    print('Percentage is :', percentage,'%')

if __name__=='__main__':
    main()
