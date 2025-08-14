def selecionar_opcao():
    return input('1 - Adicionar contato \n2 - Remover contato \n3 - Consultar contato' \
    '\nDigite a opção que deseja: ')

def adicionar_contato():
    nome = input('Nome: ').strip().title()
    telefone = input('Telefone: ')
    email = input('Email: ')
    contatos[nome] = {
        "telefone": telefone,
        "email": email
    }
    print('Contato adicionado!')

def remover_contato():
    nome = input('Digite o nome do contato que deseja remover: ').title()
    if nome in contatos:
        del contatos[nome]
        print('Contato excluído.')
    else:
        print('Contato não encontrado.')

def consultar_contato():
    nome = input('Digite o nome do contato que deseja consultar: ').title()
    if nome in contatos:
        print(f'Nome: {nome} - Telefone: {contatos[nome]["telefone"]} - Email: {contatos[nome]["email"]}')
    else:
        print('Contato não encontrado')

def agenda_atualizada():
    for nome, dados in contatos.items():
        print(f'{nome} - Telefone: {dados["telefone"]} - Email: {dados["email"]}')

contatos = {}

continua = 's'
while continua in 'Ss' or continua == 'sim':
    opcao = selecionar_opcao()
    if opcao == '1':
        adicionar_contato()
    elif opcao == '2':
        remover_contato()
    elif opcao == '3':
        consultar_contato()
    else:
        print('Opção não encontrada.')
    
    continua = input('Deseja realizar outra operação? [S/N]: ').strip().lower()

print('Operações finalizadas. Agenda atualizada: ')
agenda_atualizada()

exit()
