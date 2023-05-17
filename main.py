import contcont

sqlconnector = contcont


def main():
    print("\t\t\t\t@===========================================@")
    print("\t\t\t\t@===========-REPORT THE PASSWORD-===========@")
    print("\t\t\t\t@===========================================@")
    senha = 9645
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

    def WITHDRAW():
        entrada1 = int(input("Entry with the amount to add in entrada value "))
        gastos2 = int(input("Entry with the amount to add in gastos value"))

        def add(entrada1, gastos2):
            entrada = entrada1
            gastos = gastos2
            sqlconnector.Cont.adicionar_dados_seg(entrada, gastos)

    print("\t1 - ADD values")
    contador = int(input("\tPlease Select one:"))

    while contador != 0:
        if contador == 1:
            WITHDRAW()


if __name__ == '__main__':
    main()
