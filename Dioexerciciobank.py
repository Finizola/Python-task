import math

print("SISTEMA BANCARIO V0.0001")
dinheiro = 0
extrato = []
while True:
    try:
        menu = int(input("digite a opcao desejada: \n 1: DEPOSITO \n 2: SAQUE \n 3: EXTRATO \n 4: Sair\n\n"))
    
    except:
        print("\n \n DIGITE UM NUMERO INTEIRO: ")

    if(menu ==  1):
        print("Deposito \n\n")
        dinheiro += int(input("digite o valor para deposito: \n"))
        extrato.append(dinheiro)

    
    if(menu ==  2):
        print("Saque\n\n")
        dinheiro -= int(input("digite o valor para saque: \n"))
    
    if(menu ==  3):
        print("Extrato\n\n")
        print('o dinheiro na conta e: {}'.format(dinheiro))
        print("\n \n os valores de deposito foram: {}\n\n".format(extrato[:]))

    if(menu ==  4):
        print("\n SAINDO,OBRIGADO POR UTILIZAR")
        break