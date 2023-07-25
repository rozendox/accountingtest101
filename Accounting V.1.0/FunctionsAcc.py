import contabilidade
# ======================================================================================================================
"""
mudanças permanentes ->
    introdução do match case dentro da função main()
        resolution : 10/07/2023 - 25/07/2023


futuras resoluções :

    drop of data by year and month 25/07/2023
        resolution : ???

    view data by month and value >= and <= and 
        resolution: ???



"""
# ======================================================================================================================


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


def viewDataM():
    sqlconnectlookM.view_by_month()


def viewDatay():
    sqlconnectlookY.view_by_year()


# ======================================================================================================================
# fixme -> MAIN FUNCTION --
# ======================================================================================================================


def main():
    print("@@===================@@")
    print("@ $ ADD Values    = 1 @")
    print("@ $ View by Month = 2 @")
    print("@ $ View by year  = 3 @")
    print("@@===================@@")
    command = int(input("$ \tWhats is your command?\n"))

    def runMatch(command2: int):
        try:
            match command2:
                case 1:
                    try:
                        print("$ Do you want do Add Values?")
                        inputConfirmation = input("Y/N")
                        if inputConfirmation.lower() == "y":
                            deposit()
                            print("$ Thank you to use the system")
                            print("$ Do you want to do another Transation?")
                            confirmation = input("Y/N")
                            if confirmation.lower() == "y":
                                print("@ Do you want do add or view values? ")
                                dec_ins_c1 = str(input("$ A TO ADD \n V to view \n ---"))
                                if dec_ins_c1.lower() == "a":
                                    deposit()
                                elif dec_ins_c1 == "v":
                                    print("Ok, do you want to see by Year or By month?")
                                    operation_insade = input("$ Y TO YEAR, M TO MONTH")
                                    if operation_insade.lower() == "y":
                                        viewDatay()
                                        print("$ Thank you to use the system")
                                    elif operation_insade.lower() == "m":
                                        viewDataM()
                                    else:
                                        print(" -- ERROR -- ")
                                        print("$ Thank you to use the system")
                                        exit()
                            elif confirmation.lower() == "n":
                                print("$ Exit Successfuly")
                                print("$ Thank you to use the system")
                                exit()
                            else:
                                print("$ Thank you to use the system")
                                print("$ Invalid command")
                                exit()

                        elif inputConfirmation.lower() == "n":
                            print("$ Exit Successfuly")
                            exit()
                        else:
                            exit()
                        return "$ OPERATION SUCESSFUL ..."
                    except Exception as e:
                        return f"$ OPERATION NOT SUCESSFUL. \n ERROR - {e}"
                case 2:
                    try:
                        viewDataM()
                        print("\n$ Data Returned")
                        print("$ Thank you to use the system!")
                        decision_view = str(input("$ Do you wanna do another Transation? \n Y/n"))
                        if decision_view.lower() == "y":
                            print("$ OK \n . \n . \n . \n .")
                            main()
                        elif decision_view.lower() == "n":
                            print("$ Exiting...")
                            print("$ Thank you to use the system")
                            exit()
                        return "$ OPERATION SUCESSFULY! "
                    except Exception as e:
                        return f"$ OPERATION NOT SUCESSFUL. ERROR -> {e}"

                case 3:
                    try:
                        viewDatay()
                        print("$ Data Returned")
                        print("$ thank you to use the system")
                        dec_view = str(input("$ Do you wanna Look your data? \n Y/N?"))
                        if dec_view.lower() == "y":
                            print("$ OK")
                            dec_month_or_year = str(input("\nlook by year or by month? \n Y - year M - month\n\n"))
                            if dec_month_or_year.lower() == "y":
                                viewDatay()
                                print("\n@ Do you wanna do annother transition?")
                                dec_inside = str(input("Y/N"))
                                if dec_inside.lower() == "y":
                                    main()
                                if dec_inside.lower() == "n":
                                    print("$ Thank you to use the system")
                                    exit()
                                else:
                                    print("@ Wrong Entry.\n Exiting ...")
                                    print("$ Thank you to use the system")
                                    exit()
                            if dec_month_or_year.lower() == "m":
                                viewDataM()
                            else:
                                print("$ - Wrong Entry")
                                print("$ Thank you to use the system")
                        elif dec_view.lower() == "n":
                            exit()
                        else:
                            print("... Wrong Data")
                            print("$ Thank you to use the system")
                            exit()
                        return "$ OPERATION SUCESSFULY! "
                    except Exception as e:
                        return f"$ OPERATION NOT SUCESSFUL. ERROR -> {e}"

                case _:
                    print("$ Invalid case")
        except TypeError:
            print(TypeError)

    runMatch(command)


if __name__ == "__main__":
    for _ in range(3):
        main()
