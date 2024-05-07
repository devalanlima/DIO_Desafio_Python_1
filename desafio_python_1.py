divisor = "_"*80
saldo = 0
limite = 500
extrato = []
numero_saques = 0
limite_saques = 3
limite_atingido_msg = "\n\033[91mVocê ultrapassou o seu limite de saques diário, tente novamente em 24 horas.\033[0m"

menu = f'''
{divisor}

[1] DEPOSITAR
[2] SACAR
[3] EXTRATO
[0] SAIR

-> Digite a opção correspondente: '''

menu_sacar = f'''
{divisor}

[0] SAIR

-> Quanto você gostaria de sacar? R$'''

menu_depositar = f'''
{divisor}

[0] SAIR

-> Quanto você gostaria de depositar? R$'''

while True:
    
    opcao = input(menu)

    match opcao:
        case '1':
            while True:
                valor = round(float(input(menu_depositar)), 2) 
                while valor < 0:
                    print("\n\033[91mA Transação não pode ser concluida, pois o valor não pode ser negativo.\033[0m")
                    valor = round(float(input(menu_depositar)), 2)

                if (valor == 0):
                    break
                else:
                    saldo += valor
                    extrato.append(f"{'DEPÓSITO'.ljust(10, ' ')}| Valor depositado: R${valor:.2f} | Novo saldo: R${saldo:.2f}")
                    print(f"\nTransação concluída, seu novo saldo é de R${saldo:.2f}")

                repetir_acao = input(f"\nGostaria de realizar outro depósito? s/n: ").lower()
                while repetir_acao != "n" or repetir_acao != "s":
                    if repetir_acao == "n":
                        break
                    elif repetir_acao == "s":
                        break
                    else:
                        print("\033[91mOpção inválida.\033[0m")
                        repetir_acao = input(f"\nGostaria de realizar outro depósito? s/n: ").lower()
                if repetir_acao == "n":
                    break
        case '2':
            while True:
                if limite_saques == 0:
                    print(limite_atingido_msg)
                    break
                
                valor = round(float(input(menu_sacar)), 2)

                while valor < 0:
                    print("\n\033[91mA Transação não pode ser concluida, pois o valor não pode ser negativo.\033[0m")
                    valor = round(float(input(menu_sacar)), 2)

                if (valor == 0):
                    break
                elif (valor > saldo):
                    print(f"\n\033[91mTransação não pode ser concluída porque o valor (R${valor:.2f}) é maior que o seu saldo (R${saldo:.2f})\033[0m")
                elif (valor > limite):
                    print(f"\n\033[91mTransação não pode ser concluída porque o valor (R${valor:.2f}) é maior que o seu limite (R${limite:.2f})\033[0m")
                else:
                    saldo -= valor
                    limite_saques -= 1
                    extrato.append(f"{'SAQUE'.ljust(10, ' ')}| Valor sacado: R${valor:.2f} | Novo saldo: R${saldo:.2f}")
                    print(f"\nTransação concluída, seu novo saldo é de R${saldo:.2f}")
                
                repetir_acao = input(f"\nGostaria de realizar outro saque? s/n: ").lower()
                while repetir_acao != "n" or repetir_acao != "s":
                    if repetir_acao == "n":
                        break
                    elif repetir_acao == "s":
                        break
                    else:
                        print("\033[91mOpção inválida.\033[0m")
                        repetir_acao = input(f"\nGostaria de realizar outro saque? s/n: ").lower()
                if repetir_acao == "n":
                    break
        case '3':
            if (len(extrato) == 0):
                print(divisor)
                print(f"\nNão foi realizada nenhuma transação até o momento, o seu saldo é de R${saldo:.2f}")
            else:
                print("\n")
                print(" EXTRATO ".center(80, "~"))
                for item in extrato:
                    print(item)
                print(f"\nO saldo total é de R${saldo:.2f}")
                print("~"*80)
        case '0':
            break
        case _:
            print("\033[91mOpção inválida.\033[0m")

print("Obrigado por utilizar o nosso banco, tenha um ótimo dia!")