menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas

=>"""

def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato += f"Depósito:\tR$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, numero_saques):
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n==========EXTRATO==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=============================")

def criar_usuario(cpf, usuarios, nome, data_nascimento, endereco):
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print((linha))

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"
usuarios = []
contas = []

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo, extrato = depositar(saldo, valor, extrato)
            print("\n$$$Deposito realizado com sucesso.$$$")
            
        else:
            print("\n!!!Valor informado inválido.!!!")
    
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("\n!!!Saldo insuficiente. Saque não realizado.!!!")
        elif valor > limite:
            print("\n!!!O valor do saque excede limite. Saque não realizado.!!!")
        elif numero_saques >= LIMITE_SAQUES:
            print("\n!!!Número máximo de saque excedido. Saque não realizado.!!!")
        elif valor > 0:
            saldo, extrato, numero_saques  = sacar(
                        saldo=saldo, 
                        valor=valor, 
                        extrato=extrato, 
                        numero_saques=numero_saques)
            print("\n$$$Saque realizado com sucesso.$$$")
            
        else:
            print("\n!!!Valor inválido. Operação cancelada.!!!")
    
    
    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        cpf = input("Informe o CPF (somente números): ")
        usuario = filtrar_usuario(cpf, usuarios)
        
        if usuario:
            print("\n!!!Já existe usuário com esse CPF.!!!")
        
        else:
            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            criar_usuario(cpf, usuarios, nome, data_nascimento, endereco)
            print("\n$$$Usuário criado com sucesso.$$$")

    elif opcao == "nc":
        cpf = input("Informe o CPF do usuário: ")
        usuario = filtrar_usuario(cpf, usuarios)

        if usuario:
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuario)
            print("\n$$$Conta criada com sucesso.$$$")
        else:
            print("\n!!!Usuário não encontrado, fluxo de criação de conta encerrado!!!")

    elif opcao == "lc":
        if len(contas) == 0:
            print("\n!!!Nenhuma conta encontrada.!!!")
        else:
            listar_contas(contas)

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")

