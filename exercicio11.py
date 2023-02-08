N = int(input("digite o numero de repeticoes:  "))

while(N > 0 ):
    A = int(input("digite o valor de A: "))
    B = int(input("digite o Valor de B: "))
    print(A)
    print(B)
    str(A)
    str(B)
    print(len(str(A)))
    N -= 1
    
    if B == A:
        print("encaixa")
    else:
      print("nao encaixa")

