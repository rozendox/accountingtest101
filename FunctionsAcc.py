import contabilidade

sqlconnector = contabilidade.accountancy()
sqlconnectlookM = contabilidade.ViewAccontM()
sqlconnectlookY = contabilidade.ViewAccounntY()


# ======================================================================================================================
# fixme -> adicionar dados
# ======================================================================================================================


def deposit():
    year = int(input("Enter the year value: "))
    month = input("Enter the month value: ")
    Cash_Inflow = float(input("Enter the amount to add to the entry value: "))
    Cash_Outflow = float(input("Enter the amount to be added to the cost amount: "))

    result = sqlconnector.add_data(year, month, Cash_Inflow, Cash_Outflow)
    print(result)

# ======================================================================================================================
# fixme -> VIEW DATA
# ======================================================================================================================


def viewData():
    print("\t 1 == month")
    print("\t 2 == year")
    print("\t 0 == exit")
    counter = int(input("\tWHICH FILTER DO YOU WANT TO USE?"))
    while counter != 0:
        if counter == 1:
            sqlconnectlookM.view_by_month()
        elif counter == 2:
            sqlconnectlookY.view_by_year()
        elif counter == 0:
            exit()
