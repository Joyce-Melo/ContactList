def adicionar_contato(contatos, nome, telefone, email=""):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"Contato de {nome} foi adicionado com sucesso!")
    return

def ver_contatos(contatos):
    print("\nSua Lista de contatos: ")
    for indice, contato in enumerate(contatos, start=1):
        status = " ★ " if contato["favorito"] else ""
        nome_contato = contato["nome"]
        numero_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. {nome_contato} - {numero_contato} - {email_contato}{status}")
    return

def editar_contato(contatos, indice_contato, campo_de_edicao, nome="", telefone="", email=""):
    indice_contato_ajustado = indice_contato - 1
    if nome != "":
        item_para_editar = nome
    elif telefone != "":
        item_para_editar = telefone
    elif email != "":
        item_para_editar = email    
    if indice_contato_ajustado >=0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado][campo_de_edicao] = item_para_editar
        print(f"Campo {campo_de_edicao} atualizado com sucesso para {item_para_editar}")
    return

def favoritar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato - 1
    if contatos[indice_contato_ajustado]["favorito"]:
        contatos[indice_contato_ajustado]["favorito"] = False
        print(f"Contato {indice_contato} não está mais marcado como favorito")
    else:
        contatos[indice_contato_ajustado]["favorito"] = True
        print(f"Contato {indice_contato} marcado como favorito")
    return

def listar_favoritos(contatos):
    print("\nLista de contatos favoritos: ")
    status = " ★ "
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            print(f"{indice}. {contato["nome"]} - {contato["telefone"]} - {contato["email"]}{status}")
    return

def deletar_contato(contatos, indice_contato):
    indice_contato_ajustado = indice_contato-1
    del contatos[indice_contato_ajustado]
    print("Contato deletado com sucesso")


contatos = []
while True:
    print("\nMenu da sua agenda")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Editar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Ver lista de contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha =="1":
        nome = input("Digite um nome para o contato: ")
        telefone = input("Digite o número de telefone do contato: ")
        email = input("Digite o email do contato (Opcional): ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha =="2":
        ver_contatos(contatos)
    elif escolha =="3":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que deseja atualizar: "))
        print("\nQuais das opções abaixo gostaria de editar? ")
        print("1. Nome do contato")
        print("2. Número do contato")
        print("3. Email do contato")
        info_para_ajustar = input("Digite sua escolha: ")
        if info_para_ajustar == "1":
            campo_de_edição = "nome"
            novo_nome = input("Digite um novo nome: ")
            editar_contato(contatos, indice_contato, campo_de_edição, nome=novo_nome)
        elif info_para_ajustar == "2":
            campo_de_edição = "numero"
            novo_numero = input("Digite o novo numero: ")
            editar_contato(contatos, indice_contato, campo_de_edição, telefone=novo_numero)
        elif info_para_ajustar == "3":
            campo_de_edição = "email"
            novo_email = input("Digite o novo email: ")
            editar_contato(contatos, indice_contato, campo_de_edição, email=novo_email)
        else:
            print("Opção inválida")
    elif escolha =="4":
        ver_contatos(contatos)
        indice_contato = int(input("Informe o número do contato que deseja marcar ou desmarcar como favorito "))
        favoritar_contato(contatos, indice_contato)
    elif escolha == "5":
        listar_favoritos(contatos)
    elif escolha =="6":
        ver_contatos(contatos)
        indice_contato = int(input("Digite o número do contato que seja apagar: "))
        deletar_contato(contatos, indice_contato)
        print("")
    elif escolha == "7":
        break
print("Programa Finaliizado")