valor = 0.0
valor_real = 0.0
extrato = []
def mostrar_menu():
    print("========== BANCO PYTHON ==========")
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print("[4] Sair")
while True:
    mostrar_menu()
    try:
      escolha = int(input("Escolha uma opção: "))
      if escolha == 1: #Opção de Depósito
          valor = float(input("Informe o valor do depósito: R$ "))
          if valor > 0.0:
            valor_real = valor_real + valor
            extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Depósito de R$ {valor} realizado com sucesso!\n")
          else:
            print("Não pode depositar Valor Negativo\n")
      elif escolha == 2: # Opção de Saque
            valor = float(input("Informe o valor do saque: R$ "))
            if valor > 0:
                if valor_real >= valor:
                    valor_real -= valor
                    extrato.append(f"Saque: -R$ {valor:.2f}")
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
                else:
                    print("Não tem saldo suficiente para realizar o saque.\n")
            else:
                 print("Não pode Sacar Valor Negativo ou Zero\n")
      elif escolha == 3: # Opção Extrato
            print("\n========== EXTRATO ==========")

            if extrato: # Verifica se a lista não está vazia
                for transacao in extrato: # Para cada item na lista extrato...
                    print(transacao)     # ...imprima esse item.
            else:
                print("Não foram realizadas movimentações.")
            print(f"\nSaldo atual: R$ {valor_real:.2f}")
            print("=============================\n")
      elif escolha == 4:
          print("Saindo do sistema...")
          break
      else:
        print("Opção Inválida, tente novamente \n")
    except ValueError:
        print("Opção Inválida, tente novamente \n")