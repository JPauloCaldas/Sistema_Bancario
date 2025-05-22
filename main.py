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
        extrato, saldo = funcoes.Depositar(valor_deposito,saldo,extrato)
               
                   

    elif opcao == "s":
        while True:
            try:
                valor_saque = float(input('Informe o valor do Saque:\n=>'))
                if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite and numero_saque > 0:
                    numero_saque -= 1                    
                    saldo -= valor_saque
                    valor_saque = f"{valor_saque:.2f}"
                    extrato += '\n Saque R$ '
                    extrato += str(valor_saque)
                    print('Saque efetuado com Sucesso')
                    break

                elif valor_saque <= 0:
                    print('O valor informado é menor ou igual a Zero')

                elif valor_saque > saldo:
                    print('O valor do Saque é maior que seu saldo')
                
                elif valor_saque > limite:
                   print(f'Você não pode sacar R$ {valor_saque:.2f}', 'porque irá ultrapassar seu limite de saque')

                elif numero_saque == 0:
                    print('Você já fez os seus 3 saques diários')

                else:
                    print('valor informado é inválido')
                break

            except:
                print('Valor informado invalido')
                break

    elif opcao == "e":
        print(f'Saldo Atual: R$ {saldo:.2f}', '\n\n Extrato:', extrato)

    elif opcao == "x":
        break
    
    else:
        print("Opção inválida. Selecione novamente outra opção.")
    
