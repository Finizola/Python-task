import math

print("SISTEMA BANCARIO V0.0001")
dinheiro = 0
saques = 0
extrato = []
while True:
    try:
        menu = int(input("digite a opcao desejada: \n 1: DEPOSITO \n 2: SAQUE \n 3: EXTRATO \n 4: Sair\n\n"))
    
    except:
        print("\n \n DIGITE UM NUMERO INTEIRO: ")

    if(menu ==  1):
        print("Deposito \n\n")
        dinheiro += float(input("digite o valor para deposito: \n"))
        extrato.append(dinheiro)

    
    if(menu ==  2):
        print("Saque\n\n")
        if (dinheiro == 0):
            print("\n sem dinheiro na conta!\n")
        
        elif (saques == 3):
            print("limite de saques alcançado")

        else:
            retiradas = float(input("digite o valor para saque: \n"))
            if ((dinheiro - retiradas )< 0):
                print("ERRO,verifique o extrato bancario")
            else:
                saques += 1
                dinheiro -= retiradas
                print("\nsaques feitos: {}\n".format(saques))
    
    if(menu ==  3):
        if(extrato == []):
            print("nao foram realizadas movimentacoes")
            
        else:
            print("Extrato\n\n")
            print(f'o dinheiro na conta e: R${dinheiro:.2f}')
            print("\n \n os valores de deposito foram: R${}\n\n".format(extrato[:]))


    if(menu ==  4):
        print("\n SAINDO,OBRIGADO POR UTILIZAR")
        break