saldo = 0
limite = 500.00
extrato = ""
numero_saque = 3



def Mostra_menu():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

=> """
    return print(menu)






def Deposito(valor_deposito,saldo,extrato):
    
    if valor_deposito > 0:
        saldo += valor_deposito
        valor_deposito = f"{valor_deposito:.2f}"
        extrato += '\n Depósito R$'
        extrato += str(valor_deposito)
        print ('Deposito Realizado com Sucesso')

    else:
        print('Valor informado invalido')
    return extrato, saldo


valor_deposito = float(input('Informe o Valor do Depósito:\n=>'))

extrato, saldo = Deposito(valor_deposito, saldo, extrato)
print(extrato, '\n', saldo)