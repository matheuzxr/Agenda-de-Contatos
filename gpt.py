def formatar_nome(s: str) -> str:
    return " ".join(s.strip().title().split())

def validar_telefone(t: str) -> bool:
    so_digitos = "".join(c for c in t if c.isdigit())
    return len(so_digitos) >= 8

def validar_email(e: str) -> bool:
    e = e.strip()
    return " " not in e and "@" in e and "." in e.split("@")[-1]

def exibir_contato(nome: str, dados: dict) -> None:
    print(f'Nome: {nome} - Telefone: {dados["telefone"]} - Email: {dados["email"]}')

def adicionar_contato(contatos: dict):
    nome = formatar_nome(input('Nome: '))
    if not nome:
        print('Nome inválido.')
        return

    telefone = input('Telefone: ').strip()
    if not validar_telefone(telefone):
        print('Telefone inválido (mín. 8 dígitos).')
        return

    email = input('Email: ').strip()
    if not validar_email(email):
        print('Email inválido.')
        return

    if nome in contatos:
        print('Contato já existe:')
        exibir_contato(nome, contatos[nome])
        if input('Deseja atualizar? [s/n]: ').strip().lower() in ('s', 'sim'):
            contatos[nome] = {"telefone": telefone, "email": email}
            print('Contato atualizado!')
        else:
            print('Operação cancelada.')
    else:
        contatos[nome] = {"telefone": telefone, "email": email}
        print('Contato adicionado!')

def remover_contato(contatos: dict):
    nome = formatar_nome(input('Digite o nome do contato que deseja remover: '))
    if nome in contatos:
        del contatos[nome]
        print('Contato excluído.')
    else:
        print('Contato não encontrado.')

def consultar_contato(contatos: dict):
    nome = formatar_nome(input('Digite o nome do contato que deseja consultar: '))
    if nome in contatos:
        exibir_contato(nome, contatos[nome])
    else:
        print('Contato não encontrado.')

def listar_contatos(contatos: dict):
    if not contatos:
        print('Nenhum contato cadastrado.')
        return
    print('--- Agenda (ordenada) ---')
    for nome in sorted(contatos.keys()):
        exibir_contato(nome, contatos[nome])

def buscar_parcial(contatos: dict):
    termo = input('Digite parte do nome, telefone ou email: ').strip().lower()
    resultados = []
    for nome, dados in contatos.items():
        if (termo in nome.lower() or
            termo in dados["telefone"].lower() or
            termo in dados["email"].lower()):
            resultados.append((nome, dados))
    if not resultados:
        print('Nenhum resultado encontrado.')
    else:
        print(f'--- {len(resultados)} resultado(s) ---')
        for nome, dados in sorted(resultados, key=lambda x: x[0]):
            exibir_contato(nome, dados)

def selecionar_opcao() -> str:
    return input(
        '1 - Adicionar contato\n'
        '2 - Remover contato\n'
        '3 - Consultar contato\n'
        '4 - Listar todos (ordenado)\n'
        '5 - Buscar (parcial)\n'
        '6 - Sair\n'
        'Escolha: '
    ).strip()

def main():
    contatos = {}
    while True:
        opcao = selecionar_opcao()
        if opcao == '1':
            adicionar_contato(contatos)
        elif opcao == '2':
            remover_contato(contatos)
        elif opcao == '3':
            consultar_contato(contatos)
        elif opcao == '4':
            listar_contatos(contatos)
        elif opcao == '5':
            buscar_parcial(contatos)
        elif opcao == '6':
            break
        else:
            print('Opção inválida.')

        if input('Deseja realizar outra operação? [s/n]: ').strip().lower() not in ('s', 'sim'):
            break

    print('\nOperações finalizadas. Agenda atualizada:')
    listar_contatos(contatos)

if __name__ == "__main__":
    main()
