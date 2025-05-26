import funcoes
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """


saldo = 0
limite = 500.00
extrato = ""
numero_saque = 3




while True:
    opcao = input(menu)
    if opcao == "d":
                 
        valor_deposito = float(input('Informe o Valor do Depósito:\n=>'))
        extrato, saldo = funcoes.Depositar(valor_deposito, saldo, extrato)
               
                   

    elif opcao == "s":

        valor_saque = float(input('Informe o valor do Saque:\n=>'))
        extrato = funcoes.Sacar(valor_saque, saldo, limite, numero_saque, extrato)
                

    elif opcao == "e":
        print(f'Saldo Atual: R$ {saldo:.2f}', '\n\n Extrato:', extrato)

    elif opcao == "x":
        break
    
    else:
        print("Opção inválida. Selecione novamente outra opção.")
    
