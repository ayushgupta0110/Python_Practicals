"""
2. Consider a showroom of electronic products, where there are various
salesmen. Each salesman is given a commission of 5%, depending on the sales
made per month. In case the sale done is less than 50000, then the salesman is
not given any commission. Write a function to calculate total sales of a salesman
in a month, commission and remarks for the salesman. Sales done by each
salesman per week is to be provided as input. Use tuples / list to store data of
salesmen.
Assign remarks according to the following criteria:
Excellent: Sales >=80000
Good: Sales>=60000 and <80000
Average: Sales>=40000 and <60000
Work Hard: Sales < 40000
"""


def main():
    commission = []
    totalSales = []
    remarks = []
    noOfSalesman = int(input("Enter the no of Salesman : "))
    salesPerWeek = []

    for i in range(noOfSalesman):
        print(f"Enter weekly sales of Salesman {i + 1} : ")
        for j in range(0, 4):
            sales = eval(input(f"Enter sales of week {j + 1} : "))
            salesPerWeek.append(sales)
        totalMonthlySales = 0
        totalMonthlySales = sum(salesPerWeek)
        print(f"Total sales per month for Salesman {i + 1} :  {totalMonthlySales}")
        totalSales.append(totalMonthlySales)

        # commission calculation
    for i in range(noOfSalesman):
        if totalSales[i] < 50000:
            commission.append(0.00)
        else:
            commission.append(0.05 * totalSales[i])

    # Assigning remarks
    for i in range(noOfSalesman):
        if totalSales[i] >= 80000:
            remarks.append("Excellent")
        elif totalSales[i] >= 60000 and totalSales[i] < 80000:
            remarks.append("Good")
        elif totalSales[i] >= 40000 and totalSales[i] < 60000:
            remarks.append("Average")
        else:
            remarks.append("Work Hard")

    # Printing details of Salesman
    print("--- Details of Salesman ---")
    for i in range(noOfSalesman):
        print()
        print(f"Salesman {i + 1} :-")
        print("Total Sales : ", totalSales[i])
        print("Commission : ", commission[i])
        print("Remarks : ", remarks[i])
    print()


if __name__ == '__main__':
    main()
