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


def Depositar(valor_deposito, saldo, extrato):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        valor_deposito = f"{valor_deposito:.2f}"
        extrato += '\n Depósito R$'
        extrato += str(valor_deposito)
        print ('Deposito Realizado com Sucesso')

    else:
        print('Valor informado invalido')
    return extrato, saldo


def Sacar (valor_saque):
    global saldo, limite, extrato, numero_saque
    if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite and numero_saque > 0:
        numero_saque -= 1
        saldo -= valor_saque
        valor_saque = f"{valor_saque:.2f}"
        extrato += '\n Saque R$'
        extrato +=str(valor_saque)
        print ('Saque efetuado com Sucesso')
    elif valor_saque <= 0:
        print('O valor_saque informado é menor ou igual a Zero')
    elif valor_saque > saldo:
        print('O valor_saque do Saque é maior que seu saldo')
        
    elif valor_saque > limite:
        print(f'Você não pode sacar R$ {valor_saque:.2f}', 'porque irá ultrapassar seu limite de saque')

    elif numero_saque == 0:
        print('Você já fez os seus 3 saques diários')
    else:
            print('valor_saque informado é inválido')
    return saldo, limite, extrato, numero_saque



while True:
    opcao = input(menu)
    if opcao == "d":
                 
        valor_deposito = float(input('Informe o Valor do Depósito:\n=>'))
        extrato, saldo = Depositar(valor_deposito, saldo, extrato)
               
                   

    elif opcao == "s":

        valor_saque = float(input('Informe o valor do Saque:\n=>'))
        Sacar(valor_saque)

               
                
    elif opcao == "e":
        print(f'Saldo Atual: R$ {saldo:.2f}', '\n\n Extrato:', extrato)

    elif opcao == "x":
        break
    
    else:
        print("Opção inválida. Selecione novamente outra opção.")
    
