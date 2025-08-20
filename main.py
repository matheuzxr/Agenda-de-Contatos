def formatar_nome(n: str) -> str:
    nome = n.strip().title().split()
    return " ".join(nome)

def validar_telefone(t: str) -> bool:
    digitos = "".join(digito for digito in t if digito.isdigit())
    return len(digitos) >= 8

def validar_email(e: str) -> bool:
    return " " not in e and "@" in e and "." in e.split("@")[-1]

def exibir_contato(n: str, contatos: dict):
    if n not in contatos:
        print('Contato não encontrado. Tente novamente.')
        return
    print(f'Nome: {n} - Telefone: {contatos[n]["telefone"]} - Email: {contatos[n]["email"]}')

def selecionar_opcao():
    return input('1 - Adicionar contato \n2 - Remover contato \n3 - Consultar contato' \
    '\nDigite a opção que deseja: ')

def adicionar_contato():
    nome = formatar_nome(input('Nome: '))
    if not nome:
        print('Nenhum nome inserido. Tente novamente.')
        return
    if nome in contatos:
        print('Contato já existente')
        exibir_contato(nome)
        if input('Deseja atualizar os dados salvos? [S/N]: ').lower().strip() in ('s', 'sim'):
            print('Informe os dados atualizados: ')
        else:
            return

    telefone = input('Telefone: ').strip()
    if not validar_telefone(telefone):
        print('Telefone inválido. Tente novamente.')
        return

    email = input('Email: ').strip()
    if not validar_email(email):
        print('Email inválido. Tente novamente.')
        return


    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
    print('Contato adicionado!')

def remover_contato():
    nome = formatar_nome(input('Digite o nome do contato que deseja remover: '))
    if nome in contatos:
        del contatos[nome]
        print('Contato excluído.')
    else:
        print('Contato não encontrado.')

def busca_parcial(contatos: dict):
    termo = input('Digite parte do nome, telefone ou email: ').strip().lower()
    resultados = []
    for nome, dados in contatos.items():
        if termo in nome.lower() or termo in dados["telefone"].lower() or termo in dados["email"].lower():
            resultados.append((nome, dados))
    if not resultados:
        print('Nenhum resultado encontrado.')
    else:
        print('Resultados encontrados:')
        for nome, dados in sorted(resultados, key=lambda x: x[0]):
            exibir_contato(nome, contatos)

def agenda_atualizada(agenda: dict):
    if not agenda:
        print('Nenhum contato encontrado.')
        return
    for nome, dados in sorted(contatos.items()):
        print(f'{nome} - Telefone: {dados["telefone"]} - Email: {dados["email"]}')

contatos = {}

continua = 's'
while continua in ('s', 'sim'):
    opcao = selecionar_opcao()
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        remover_contato()
    elif opcao == '3':
        busca_parcial(contatos)
    else:
        print('Opção não encontrada.')
    
    continua = input('Deseja realizar outra operação? [S/N]: ').strip().lower()

print('Operações finalizadas. Agenda atualizada: ')
agenda_atualizada(contatos)
exit()
