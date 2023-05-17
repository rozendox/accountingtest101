import contcont

sqlconnector = contcont.Cont()


def main():
    print("\t\t\t\t@===========================================@")
    print("\t\t\t\t@===========-REPORT THE PASSWORD-===========@")
    print("\t\t\t\t@===========================================@")
    senha = 4587
    sen = int(input("..."))
    while sen != senha:
        print("\tvocê tem mais 3 tentaivas...\n")
        sen = int(input("informe a senha novamente\n"))
        if sen != senha:
            print("\tvocê tem mais 2 tentivas\n")
            sen = int(input("informe a senha novamente\n"))
            if sen != senha:
                print("\tvocê tem mais 1 tentivas\n")
                sen = int(input("informe a senha novamente\n"))
                if sen != senha:
                    print("\tA senha informada está errada...\n")
                    print("finalizando o sistema\n")
                    contador = 0
                    while contador < 10:
                        print(".", end=" " + "\n")
                        contador += 1
                    exit()
                else:
                    print("\t\t\t\t@==============================================@")
                    print("\t\t\t\t@===========-Welcome To the System!-===========@")
                    print("\t\t\t\t@==============================================@")
            else:
                print("\t\t\t\t@==============================================@")
                print("\t\t\t\t@===========-Welcome To the System!-===========@")
                print("\t\t\t\t@==============================================@")
        else:
            print("\t\t\t\t@==============================================@")
            print("\t\t\t\t@===========-Welcome To the System!-===========@")
            print("\t\t\t\t@==============================================@")
    else:
        print("\t\t\t\t@==============================================@")
        print("\t\t\t\t@===========-Welcome To the System!-===========@")
        print("\t\t\t\t@==============================================@")

    def deposit_january():
        entrada = int(input("Enter with the value to add to the Entry value"))
        gastos = int(input("Enter the amount to be added to the cost amount"))
        sqlconnector.adicionar_dados_seg(entrada, gastos)

    def deposit_february():
        entrada = int(input("Enter with the value to add to the Entry value"))
        gastos = int(input("Enter the amount to be added to the cost amount"))
        sqlconnector.adicionar_dados_fev(entrada, gastos)

    print("\t1 - ADD values")
    counter = int(input("\tPlease Select one:"))

    while counter != 0:
        if counter == 1:
            print(":\t\tWICH MONTH DO YOU WANT TO PERFORM AN OPERATION??:")
            print("\t1 - Janruary")
            print("\t2 - February")
            month = int(input("@@-INFORM THE DESIRED MONTH-@@"))
            if month == 1:
                deposit_january()
                print("@@ DATA ENTERED SUCCESSFULLY @@")
                print("@@ DO YOU WANT TO RETURN TO MAIN MENU? @@")
                end = input("... Y/N")
                if end.lower() == "y":
                    main()
                else:
                    exit()
            elif month == 2:
                deposit_february()
                print("@@ DATA ENTERED SUCCESSFULLY @@")
                print("@@ DO YOU WANT TO RETURN TO MAIN MENU? @@")
                end = input("... Y/N")
                if end.lower() == "y":
                    main()
                else:
                    exit()

        elif counter == 2:
            pass


if __name__ == '__main__':
    main()
