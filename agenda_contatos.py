def adcionar_contato(contatos, novo_contato):
    contatos.append(novo_contato)
    print(f"\nO contato de {novo_contato['nome'].upper()} foi salvo com sucesso!")
    return

def listar_contatos(contatos):
    print("\n Lista de contatos:\n")

    for indice,contato in enumerate(contatos, start=1):
        favorito = "✓" if contato['favorito'] == True else ""
        dados_contato = f"nome: {contato['nome']} - telefone: {contato['telefone']} - e-mail: {contato['email']}"
        print(f"{indice}. [{favorito}] - {dados_contato}")
    return

def atualizar_contato(contatos, indice, novo_email, novo_telefone):
    indice_contato_ajustado = int(indice) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if len(novo_email) != 0 and len(novo_telefone) != 0:
            contatos[indice_contato_ajustado]['email'] = novo_email
            contatos[indice_contato_ajustado]['telefone'] = novo_telefone
        elif len(novo_email) == 0 and novo_telefone:
            contatos[indice_contato_ajustado]['telefone'] = novo_telefone
        elif novo_email and len(novo_contato) == 0:
            contatos[indice_contato_ajustado]['email'] = novo_email
        else:
            print("\nPor favor preencha os campos email e telefone para atualizar o contato")
            return
        
        print(f"O contato {contatos[indice_contato_ajustado]['nome']} foi atualizado com sucesso!")
        return

def favoritar_contato(contatos, indice):
    indice_contato_ajustado = int(indice) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        if not contatos[indice_contato_ajustado]['favorito']:
            contatos[indice_contato_ajustado]['favorito'] = True
            print(f"\nContato de {contatos[indice_contato_ajustado]['nome']} foi favoritado com sucesso")
        else:
            contatos[indice_contato_ajustado]['favorito'] = False
            print(f"\nContato de {contatos[indice_contato_ajustado]['nome']} foi desfavoritado com sucesso")
    else:
        print("Contato não encotrado")
    return

def listar_favoritos(contatos):
    print("\n Lista de favoritos: ")

    for indice, contato in enumerate(contatos, start=1):
        if contato['favorito']:
            print(f"{indice}. [✓] Nome: {contato['nome']} - telefone: {contato['telefone']} - e-mail: {contato['email']}")
    return

def deletar_contato(contatos, indice):
    indice_contato_ajustado = int(indice) - 1

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato_remover = contatos[indice_contato_ajustado]
        contatos.remove(contato_remover)
    else:
        print("Contato não encotrado")

    print(f"\n Contado deletado com sucesso!")


contatos = []
while True:
    print("\nGerenciamento de contatos\n")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Atualizar contato")
    print("4. Favoritar/Desfavoritar contato")
    print("5. Listar contatos favoritados")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == '7':
        break

    if escolha == '1':
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone - (21)99999-9999: ")
        email = input("Digite o email: ")           
        
        novo_contato = {
            "nome" : nome,
            "telefone" : telefone,
            "email" : email,
            "favorito" : False
        }

        adcionar_contato(contatos=contatos, novo_contato=novo_contato)

    if escolha == '2':
        listar_contatos(contatos=contatos)

    if escolha == '3':
        listar_contatos(contatos=contatos)
        indice = input("\nDigite o indice do contato que deseja atualizar: ")
        novo_telefone = input("Digite o telefone: ")
        novo_email= input("Digite o e-mail: ")
        atualizar_contato(contatos=contatos,indice=indice, novo_email= novo_email, novo_telefone=novo_telefone )

    if escolha == '4':
        listar_contatos(contatos=contatos)
        indice = input("\nDigite o indice do contato que deseja favoritar: ")
        favoritar_contato(contatos=contatos, indice=indice)

    if escolha == '5':
        listar_favoritos(contatos=contatos)

    if escolha == '6':
        listar_contatos(contatos=contatos)
        indice = input("\nDigite o indice do contato que deseja deletar: ")
        deletar_contato(contatos=contatos, indice=indice)
    
