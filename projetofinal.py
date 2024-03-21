import random

VERMELHO = '\033[31m'
VERDE = '\033[32m'
AMARELO = '\033[33m'
AZUL = '\033[34m'
ROXO = '\033[35m'
CIANO = '\033[36m'
BRANCO = '\033[37m'
NEGRITO = '\033[1m'
RESETAR = '\033[0m'

tentativassenha = 3
numconta = 0
contacadastrada = False
historico = []
bloquearacoes = False
saldo = 0
limitecredito = 0

########################################################################################################################
def bloquear():
    global bloquearacoes
    bloquearacoes = True
    print(f"{AZUL}Você excedeu o número máximo de tentativas. Acesso bloqueado.{RESETAR}")
#-----------------------------------------------------------------------------------------------------------------------
def fazercadastro():
    global numconta, contacadastrada, nomcliente, historico, senha, tentativassenha, bloquearacoes, saldo, limitecredito

    if not contacadastrada:
        print(f"\n{VERMELHO}{NEGRITO}MACK BANK - CADASTRO DE CONTA CORRENTE{RESETAR}\n")

        numconta = random.randint(1000, 10000)
        print(f"UM NÚMERO ALEATÓRIO SERÁ GERADO PARA SUA CONTA")
        print(f"CONTA CORRENTE: {VERMELHO}{NEGRITO}{numconta}{RESETAR}")

        while True:
            nomcliente = input("NOME DO CLIENTE: ")
            if nomcliente != "" and not nomcliente.isdigit():
                print(f"CADASTRO REALIZADO, SEU NOME É: {VERMELHO}{nomcliente}{RESETAR}")
                break
            else:
                print(f"{AZUL}{NEGRITO}O NOME NÃO PODE ESTAR EM BRANCO OU SER UM NÚMERO, DIGITE NOVAMENTE!{RESETAR}")

        while True:
            telefone = input("TELEFONE DO CLIENTE: ")
            if telefone != "" and telefone.isdigit():
                telefone = int(telefone)
                print(f"CADASTRO REALIZADO, SEU NÚMERO É {VERMELHO}{telefone}{RESETAR}")
                break
            else:
                print(f"{AZUL}O TELEFONE NÃO PODE ESTAR EM BRANCO E DEVE SER UM NÚMERO. DIGITE NOVAMENTE!{RESETAR}")

        while True:
            email = input("E-MAIL DO CLIENTE: ")
            if email != "" and "@" in email and not email.isdigit():
                print(f"CADASTRO REALIZADO, SEU E-MAIL É: {VERMELHO}{email}{RESETAR}")
                break
            else:
                if email == "" or email.isdigit():
                    print(f"{AZUL}O E-MAIL NÃO PODE ESTAR EM BRANCO E OU SER UM NÚMERO. DIGITE NOVAMENTE!{RESETAR}")
                elif "@" not in email:
                    print(f"{AZUL}O E-MAIL DEVE CONTER O CARACTERE '@', DIGITE NOVAMENTE!{RESETAR}")

        while True:
            saldoini = input("SALDO INICIAL R$ [SOMENTE NÚMEROS]: ")
            saldoini = ''.join(char if char.isdigit() or char == '.' or (char == ',' and '.' not in saldoini) else '' for char in saldoini)
            if saldoini.replace('.', '').replace(',', '').isdigit():
                saldoini = float(saldoini.replace(',', '.'))
                if saldoini >= 1000:
                    print(f"CADASTRO REALIZADO, SEU SALDO INICIAL É IGUAL A: {VERMELHO}R${saldoini:.2f}{RESETAR}")
                    break
                else:
                    print(f"{AZUL}O SALDO DEVE SER MAIOR OU IGUAL A R$1000, DIGITE NOVAMENTE!{RESETAR}")
            else:
                print(f"{AZUL}ENTRADA INVÁLIDA. DIGITE APENAS NÚMEROS!{RESETAR}")

        while True:
            limite = input("LIMITE DE CRÉDITO R$ [SOMENTE NÚMEROS]: ")
            limite = ''.join(char if char.isdigit() or char == '.' or (char == ',' and '.' not in limite) else '' for char in limite)
            if limite.replace('.', '').replace(',', '').isdigit():
                limite = float(limite.replace(',', '.'))
                if limite >= 0:
                    print(f"CADASTRO REALIZADO, SEU LIMITE É IGUAL A: {VERMELHO}R${limite:.2f}{RESETAR}")
                    break
                else:
                    print(f"{AZUL}O LIMITE DEVE SER MAIOR OU IGUAL A R$0, DIGITE NOVAMENTE!{RESETAR}")
            else:
                print(f"{AZUL}ENTRADA INVÁLIDA. DIGITE APENAS NÚMEROS!{RESETAR}")

        while True:
            senha = input("SENHA: ")
            if len(senha) == 6:
                senhadnv = input("REPITA A SENHA: ")
                if senhadnv == senha:
                    print(f"{VERMELHO}CADASTRO REALIZADO!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
                    input()
                    break
                else:
                    print(f"{AZUL}A SENHA DEVE SER IDENTICA À MENCIONADA ANTERIORMENTE, DIGITE NOVAMENTE!{RESETAR}")
            else:
                print(f"{AZUL}A SENHA DEVE POSSUIR 6 CARACTERES, DIGITE NOVAMENTE!{RESETAR}")

        contacadastrada = True
        saldo = saldoini
        limitecredito = float(limite)
    else:
        print(f"{AZUL}CONTA CORRENTE JÁ CADASTRADA!!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        input()
#-----------------------------------------------------------------------------------------------------------------------
def fazerdeposito():
    global numconta, contacadastrada, nomcliente, historico, senha, tentativassenha, bloquearacoes, saldo, limitecredito

    print(f"{VERMELHO}\nMACK BANK - DEPÓSITO EM CONTA\n{RESETAR}")

    if contacadastrada:
        while True:
            numcontadois = input("INFORME O NÚMERO DA CONTA: ")
            if numcontadois == str(numconta):
                print(f"NOME DO CLIENTE: {VERMELHO}{nomcliente}{RESETAR}")
                break
            else:
                print(f"{AZUL}O NÚMERO DA CONTA DEVE SER IDENTICO AO CADASTRADO, DIGITE NOVAMENTE!{RESETAR}")

        while True:
            deposito = input("VALOR DO DEPÓSITO R$ [SOMENTE NÚMEROS]: ")
            deposito = ''.join(char if char.isdigit() or char == '.' or (char == ',' and '.' not in deposito) else '' for char in deposito)
            if deposito.replace('.', '').replace(',', '').isdigit():
                deposito = float(deposito.replace(',', '.'))
                if deposito > 0:
                    historico.append(deposito)
                    print(
                        f"{VERMELHO}DEPÓSITO REALIZADO COM SUCESSO!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                    input()
                    break
                else:
                    print(f"{AZUL}O DEPÓSITO DEVE SER MAIOR QUE R$0, DIGITE NOVAMENTE!{RESETAR}")
            else:
                print(f"{AZUL}O DEPOSITO NÃO PODE ESTAR EM BRANCO OU POSSUIR LETRAS, DIGITE NOVAMENTE!{RESETAR}")
    else:
        print(F"{AZUL}VOCÊ SÓ PODE FAZER UM DEPÓSITO APÓS CADASTRAR A CONTA CORRENTE!!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        input()
#-----------------------------------------------------------------------------------------------------------------------
def fazersaque():
    global numconta, contacadastrada, nomcliente, historico, senha, tentativassenha, bloquearacoes, saldo, limitecredito

    print(f"{VERMELHO}\nMACK BANK - SAQUE DA CONTA\n{RESETAR}")

    if contacadastrada and not bloquearacoes:
        while True:
            num_conta_digitado = input("INFORME O NÚMERO DA CONTA: ")
            if num_conta_digitado == str(numconta):
                print(f"NOME DO CLIENTE: {VERMELHO}{nomcliente}{RESETAR}")
                break
            else:
                print(f"{AZUL}O NÚMERO DA CONTA DEVE SER IDENTICO AO CADASTRADO, DIGITE NOVAMENTE!{RESETAR}")

        while tentativassenha > 0:
            senha_digitada = input("INFORME A SENHA : ")
            if senha_digitada != senha:
                tentativassenha -= 1
                print(f"{AZUL}A SENHA DEVE SER IDENTICA À CADASTRADA, DIGITE NOVAMENTE! Tentativas restantes: {tentativassenha}{RESETAR}")
                if tentativassenha == 0:
                    bloquear()
            else:
                saque = input("VALOR DO SAQUE: ")
                saque = ''.join(char if char.isdigit() or char == '.' or (char == ',' and '.' not in saque) else '' for char in saque)
                if saque.replace('.', '').replace(',', '').isdigit():
                    saque = float(saque.replace(',', '.'))
                    if saque > 0:
                        if saque <= saldo:
                            saldo -= saque
                            historico.append(-saque)
                            print(f"{VERMELHO}SAQUE REALIZADO COM SUCESSO!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                            input()
                            break
                        elif saque <= (saldo + limitecredito):
                            saldo = 0
                            limitecredito -= (saque - saldo)
                            historico.append(-saque)
                            print(f"VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO.")
                            print(f"{VERMELHO}SAQUE REALIZADO COM SUCESSO!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                            input()
                            break
                        else:
                            print("Saldo insuficiente e limite de crédito ultrapassado. Saque não realizado.")
                    else:
                        print(f"{AZUL}O SAQUE DEVE SER MAIOR QUE R$0, DIGITE NOVAMENTE!{RESETAR}")
                else:
                    print(f"{AZUL}ENTRADA INVÁLIDA. DIGITE APENAS NÚMEROS!{RESETAR}")
    elif not contacadastrada:
        print(F"{AZUL}VOCÊ SÓ PODE FAZER SAQUE APÓS CADASTRAR A CONTA CORRENTE!!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        input()
#-----------------------------------------------------------------------------------------------------------------------
def consultasaldo():
    global numconta, contacadastrada, nomcliente, historico, senha, tentativassenha, bloquearacoes, saldo, limitecredito

    print(f"{VERMELHO}\nMACK BANK - CONSULTA DE SALDO E LIMITE DE CRÉDITO\n{RESETAR}")

    if contacadastrada and not bloquearacoes:
        while True:
            numcontadois = input("INFORME O NÚMERO DA CONTA: ")
            if numcontadois == str(numconta):
                print(f"NOME DO CLIENTE: {VERMELHO}{nomcliente}{RESETAR}")
                break
            else:
                print(f"{AZUL}O NÚMERO DA CONTA DEVE SER IDENTICO AO CADASTRADO, DIGITE NOVAMENTE!{RESETAR}")

        while tentativassenha > 0:
            confirmsenha = input("INFORME A SENHA : ")
            if confirmsenha != senha:
                tentativassenha -= 1
                print(f"{AZUL}A SENHA DEVE SER IDENTICA À CADASTRADA, DIGITE NOVAMENTE! Tentativas restantes: {tentativassenha}{RESETAR}")
                if tentativassenha == 0:
                    bloquear()
            else:
                print(f"SALDO ATUAL: R${saldo}")
                print(f"LIMITE DE CRÉDITO: R${limitecredito}")
                print("PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
                input()
                break
    elif not contacadastrada:
        print(f"{AZUL}VOCÊ SÓ PODE CONSULTAR SALDO APÓS CADASTRAR A CONTA CORRENTE!!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        input()
#-----------------------------------------------------------------------------------------------------------------------
def consultaextrato():
  global numconta, contacadastrada, nomcliente, historico, senha, tentativassenha, bloquearacoes, saldo, limitecredito

  print(f"{VERMELHO}\nMACK BANK - CONSULTA DE EXTRATO\n{RESETAR}")

  if contacadastrada and not bloquearacoes:
      while True:
          numcontadois = input("INFORME O NÚMERO DA CONTA: ")
          if numcontadois == str(numconta):
              print(f"NOME DO CLIENTE: {VERMELHO}{nomcliente}{RESETAR}")
              break
          else:
              print(f"{AZUL}O NÚMERO DA CONTA DEVE SER IDENTICO AO CADASTRADO, DIGITE NOVAMENTE!{RESETAR}")

      while tentativassenha > 0:
          confirmsenha = input("INFORME A SENHA: ")
          if confirmsenha != senha:
              tentativassenha -= 1
              print(f"{AZUL}A SENHA DEVE SER IDENTICA À CADASTRADA, DIGITE NOVAMENTE! Tentativas restantes: {tentativassenha}{RESETAR}")
              if tentativassenha == 0:
                  bloquear()
          else:
              print(f"LIMITE DO CARTÃO: R${limitecredito}")
              print("LISTA DE OPERAÇÕES:")
              for operacao in historico:
                  if operacao < 0:
                      print(f"SAQUE: R${-operacao}")
                  else:
                      print(f"DEPÓSITO: R${operacao}")
              print(f"SALDO EM CONTA: R${saldo}")
              if saldo < 0:
                  print("Atenção ao seu saldo!")
              print("PRESSIONE UMA TECLA PARA VOLTAR AO MENU... ")
              input()
              break
  elif not contacadastrada:
      print(f"{AZUL}VOCÊ SÓ PODE CONSULTAR O EXTRATO APÓS CADASTRAR A CONTA CORRENTE!!{RESETAR} PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
      input()
########################################################################################################################

opcao = 0
while opcao != 6:
  print(f"{VERMELHO}MACK BANK – ESCOLHA UMA OPÇÃO{RESETAR}")
  print(f"{VERMELHO}(1){RESETAR} CADASTRAR CONTA CORRENTE")
  print(f"{VERMELHO}(2){RESETAR} DEPOSITAR")
  print(f"{VERMELHO}(3){RESETAR} SACAR")
  print(f"{VERMELHO}(4){RESETAR} CONSULTAR SALDO")
  print(f"{VERMELHO}(5){RESETAR} CONSULTAR EXTRATO")
  print(f"{VERMELHO}(6){RESETAR} FINALIZAR")
  while True:
      opcao = input(f"{VERMELHO}SUA OPÇÃO: {RESETAR}")

      if opcao != "" and opcao.isdigit():
          opcao = int(opcao)
          opcao = int(opcao)
          if 1 <= opcao <= 6:

              if opcao == 1:
                  fazercadastro()

              elif opcao == 2:
                  fazerdeposito()
              elif opcao ==3:
                  fazersaque()
              elif opcao ==4:
                  consultasaldo()
              elif opcao ==5:
                  consultaextrato()

              elif opcao == 6:
                  print(f"{AZUL}\nPROGRAMA ENCERRADO!\n{RESETAR}"
                        "\nMACK BANK – SOBRE"
                        "\nEste programa foi desenvolvido por:\n"
                        "Jennifer Tondade - MATRÍCULA: 32393164\n"
                        "Lucas Kato - MATRÍCULA: 32369409\n"
                        "Priscila Herculano - MATRÍCULA: 32388764")
                  break
              else:
                  print(f"{AZUL}Opção inválida! Escolha uma opção entre 1 e 6.{RESETAR}")
              break
          else:
              print(f"{AZUL}A OPÇÃO DEVE SER UM NÚMERO ENTRE 1 E 6. DIGITE NOVAMENTE!{RESETAR}")
      else:
          print(f"{AZUL}A OPÇÃO NÃO PODE ESTAR EM BRANCO E/OU POSSUIR LETRAS. DEVE SER UM NÚMERO ENTRE 1 E 6. DIGITE NOVAMENTE!{RESETAR}")