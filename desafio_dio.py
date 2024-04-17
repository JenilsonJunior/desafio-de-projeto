menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = " "
numero_saque = 0
LIMITE_Saque = 3

while True:

    opção = input(menu)

    if opção == "1":
        Valor = float(input("Informe o valor do deposito: "))

        if Valor > 0:
            saldo += Valor
            extrato += f"Depósito: R$ {Valor:.2f}\n"

        else:
            print("Operação falhou, o Valor informado é invalido!")

    elif opção == "2":
        Valor = float(input("Informe o valor a Sacar: "))

        excedeu_saque = Valor > saldo
        excedeu_limite = Valor > limite
        excedeu_quantidade_saques = numero_saque >= LIMITE_Saque

        if excedeu_saque:
            print("Operação falhou!, Valor informado ultrapassa o Valor máximo de saque!")

        elif excedeu_limite:
            print("Operação falhou! Seu Limite é insuficiente!")

        elif excedeu_quantidade_saques:
            print("Operação falhou, quantidade de saques excedida!")

        elif Valor > 0:
            saldo -= Valor
            extrato += f"Saque: R$ {Valor:.2f}\n"
            numero_saque += 1

        else:
            print("Operação falhou! o Valor informado é inválido")



    elif opção == "3":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("==============================================")

    elif opção == "0":
        print(f'''saindo...
     Obrigado por utilizar nosso serviço bancário!
              ''')
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")