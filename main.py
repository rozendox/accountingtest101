import contabilidade

sqlconnector = contabilidade.accountancy()
sqlconnectlook = contabilidade.ViewAccont()


# =======================================================================================================================
# fixme -> adicionar dados
# =======================================================================================================================


def deposit():
    year = int(input("Enter the year value: "))
    month = input("Enter the month value: ")
    Cash_Inflow = float(input("Enter the amount to add to the entry value: "))
    Cash_Outflow = float(input("Enter the amount to be added to the cost amount: "))

    result = sqlconnector.add_data(year, month, Cash_Inflow, Cash_Outflow)
    print(result)

# =======================================================================================================================

def mensage():
    print("\t\t\t\t@==============================================@")
    print("\t\t\t\t@===========-Welcome To the System!-===========@")
    print("\t\t\t\t@==============================================@")


def main():
    contador = 0
    while contador < 5:
        print(".", end=" " + "\n")
        contador += 1
    print("\t@==========-MENU-==========@")
    print("\t@==== 1 - ADD values ======@")
    print("\t@==== 2 - SEE Values ======@")
    print("\t@==========================@")

    choice = int(input("@@ Choose an Option - \n === @@"))

    if choice == 1:
        deposit()
        choice_return = input("Do you want to return to main menu? -- Y or N --")
        if choice_return.lower() == "y":
            print("== Returning to Main Menu ==")
            main()
        if choice_return.lower() == "n":
            exit()
        else:
            print("== Wrong Value ==")
            exit()
    elif choice == 2:
        pass
    else:
        print("ERROR, INCORRECTLY ENTERED VALUE")


if __name__ == '__main__':
    mensage()
    main()
