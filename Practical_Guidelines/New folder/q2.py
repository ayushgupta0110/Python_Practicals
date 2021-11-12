def main():

    commission = []
    totalSales = []
    remarks = []
    noOfSalesman = int(input("Enter the no of Salesman : "))
    avgWeeklySales = []
    
    for i in range(noOfSalesman):

        sales = eval(input(f"Enter average weekly sales of Salesman {i+1} : "))
        avgWeeklySales.append(sales)
        totalSales.append(4 * avgWeeklySales[i])

    # Commission Calculation

    for i in range(noOfSalesman):

        if totalSales[i]<50000:
            commission.append(0.00)

        else:
            commission.append(0.05*totalSales[i])

    # Assigning Remarks

    for i in range(noOfSalesman):

        if totalSales[i]>=80000:
            remarks.append("Excellent")

        elif totalSales[i]>=60000 and totalSales[i]<80000:
            remarks.append("Good")

        elif totalSales[i]>=40000 and totalSales[i]<60000:
            remarks.append("Average")

        else:
            remarks.append("Work Hard")

    # Printing details of Salesman

    print("--- Details of Salesman ---")

    for i in range(noOfSalesman):

        print()

        print(f"Salesman {i+1} :-")
        print("Total Sales : ",totalSales[i])
        print("Commission : ",commission[i])
        print("Remarks : ",remarks[i])

    print()
    
if __name__=='__main__':
    main()
