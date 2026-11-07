print("============================================")
print("       Sistema De Registro De Clientes      ")
print("               By Miguelprando              ")
print("============================================")

import json


def salvar_clientes():
    with open("clientes.json", "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, ensure_ascii=False, indent=4)


def Carregar_clients():
    try:
        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
clientes = Carregar_clients()


def cadastrar_cliente():
    nome = input(" Digite o nome do cliente: ")
    
    if not nome.replace(" ", "").isalpha():
        print(" Digite um nome Valido !")
        return

    clientes.append(nome)
    salvar_clientes()
    print(" Cliente Cadastrado com sucesso !")


def lista_clientes():
    for cliente in clientes:
        print (cliente)


def Pesquisar_Cliente():
    nome = input (" Digite o nome do cliente que dejesa consultar : ")

    if nome in clientes:
        print (" Cliente Cadastrado ! ")

    else:
        print(" Cliente Nao Encontrado ! ")


def Excluir_cliente():
    nome = input (" Digite o nome do cliente que deseja excluir : ")        
    if nome in clientes:
        clientes.remove(nome)
        salvar_clientes()
        print(" Cliente Removido com Sucesso ! ")
    else:
        print(" Cliente Nao Encontrado ! ")    


while True:

    print(" \nSistema de cadastro de clientes ")
    print("\n1 - Cadastrar Cliente ")
    print("2 - Listar Clientes ")
    print("3 - Pesquisar Cliente ")
    print("4 - Excluir Cliente ")
    print("0 - Sair da aplicacao ")

    opcao = input("Escolha uma Opcao: ")

    if opcao == "1":
        cadastrar_cliente()

    elif opcao == "2":
        lista_clientes()  

    elif opcao == "3":
        Pesquisar_Cliente()

    elif opcao == "4":
        Excluir_cliente()

    elif opcao == "0":
        print (" voce saiu da aplicacao ")
        break

    else:

        print ("opcao invalida! ")            