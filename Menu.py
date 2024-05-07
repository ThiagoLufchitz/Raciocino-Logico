'''
Aluno : Thiago Dorfman Lufchitz
Curso :ADS - Analise e Desenvolvimento de Software
'''
import json

# Listas para armazenar dados
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []


def salvar_listas(nome_arquivo, lista):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(lista, arquivo)


def carregar_listas(nome_arquivo_json):
    try:
        with open(nome_arquivo_json, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []


# Carregar listas existentes (se houver)
professores = carregar_listas('professores.json')
estudantes = carregar_listas('estudantes.json')
disciplinas = carregar_listas('disciplinas.json')
turmas = carregar_listas('turmas.json')
matriculas = carregar_listas('matriculas.json')


# Função para incluir estudante
def incluir_estudante():
    while True:
        try:
            codigo = int(input("Digite o código do estudante: "))
            # Verifica se o código já existe
            for estudante in estudantes:
                if estudante['codigo'] == codigo:
                    print("Este código já existe.")
                    return
            break  # Se o código for válido e único, sai do loop
        except ValueError:
            print("Código inválido. Digite um número inteiro.")

    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    estudante = {'nome': nome, 'codigo': codigo, 'cpf': cpf}
    estudantes.append(estudante)
    print("Estudante incluído")
    salvar_listas('estudantes.json', estudantes)


# Função para listar estudantes
def listar_estudantes():
    if len(estudantes) == 0:
        print("Não há estudantes cadastrados.")
    for estudante in estudantes:
        print(f"Nome: {estudante['nome']}, Código: {estudante['codigo']}, CPF: {estudante['cpf']}")


# Função para editar estudante
def editar_estudante():
    try:
        codigo = int(input("Digite o código do estudante que deseja editar: "))
        for i, estudante in enumerate(estudantes):
            if estudante['codigo'] == codigo:
                novo_codigo = input("Digite o novo código do estudante: ")
                if novo_codigo:
                    estudantes[i]['codigo'] = int(novo_codigo)
                estudantes[i]['nome'] = input("Digite o novo nome do estudante: ")
                estudantes[i]['cpf'] = input("Digite o novo CPF do estudante: ")
                print("Estudante editado")
                salvar_listas('estudantes.json', estudantes)
                return
        print("Estudante não encontrado.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para excluir estudante
def excluir_estudante():
    try:
        codigo = int(input("Digite o código do estudante que deseja excluir: "))
        for estudante in estudantes:
            if estudante['codigo'] == codigo:
                estudantes.remove(estudante)
                print("Estudante excluído")
                salvar_listas('estudantes.json', estudantes)
                return
        print("Estudante não encontrado.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para incluir professor
def incluir_professor():
    try:
        codigo = int(input("Digite o código do professor: "))
        for professor in professores:
            if professor['codigo'] == codigo:
                print("Este código já existe.")
                return
        nome = input("Digite o nome do professor: ")
        cpf = input("Digite o CPF do professor: ")
        professor = {'nome': nome, 'codigo': codigo, 'cpf': cpf}
        professores.append(professor)
        print("Professor incluído")
        salvar_listas('professores.json', professores)
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para listar professores
def listar_professores():
    if len(professores) == 0:
        print("Não há professores cadastrados.")
    for professor in professores:
        print(f"Nome: {professor['nome']}, Código: {professor['codigo']}, CPF: {professor['cpf']}")


# Função para editar professor
def editar_professor():
    try:
        codigo = int(input("Digite o código do professor que deseja editar: "))
        for i, professor in enumerate(professores):
            if professor['codigo'] == codigo:
                novo_codigo = input("Digite o novo código do professor: ")
                if novo_codigo:
                    professores[i]['codigo'] = int(novo_codigo)
                professores[i]['nome'] = input("Digite o novo nome do professor: ")
                professores[i]['cpf'] = input("Digite o novo CPF do professor: ")
                print("Professor editado")
                salvar_listas('professores.json', professores)
                return
        print("Professor não encontrado.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para excluir professor
def excluir_professor():
    try:
        codigo = int(input("Digite o código do professor que deseja excluir: "))
        for professor in professores:
            if professor['codigo'] == codigo:
                professores.remove(professor)
                print("Professor excluído")
                salvar_listas('professores.json', professores)
                return
        print("Professor não encontrado.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para incluir disciplina
def incluir_disciplina():
    try:
        codigo = int(input("Digite o código da disciplina: "))
        for disciplina in disciplinas:
            if disciplina['codigo'] == codigo:
                print("Este código já existe.")
                return
        nome = input("Digite o nome da disciplina: ")
        disciplina = {'nome': nome, 'codigo': codigo}
        disciplinas.append(disciplina)
        print("Disciplina incluída")
        salvar_listas('disciplinas.json', disciplinas)
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para listar disciplinas
def listar_disciplinas():
    if len(disciplinas) == 0:
        print("Não há disciplinas cadastradas.")
    for disciplina in disciplinas:
        print(f"Nome Disciplina: {disciplina['nome']}, Código Disciplina: {disciplina['codigo']}")


# Função para editar disciplina
def editar_disciplina():
    try:
        codigo = int(input("Digite o código da disciplina que deseja editar: "))
        for i, disciplina in enumerate(disciplinas):
            if disciplina['codigo'] == codigo:
                novo_codigo = input("Digite o novo código da disciplina: ")
                if novo_codigo:
                    disciplinas[i]['codigo'] = int(novo_codigo)
                disciplinas[i]['nome'] = input("Digite o novo nome da disciplina: ")
                print("Disciplina editada")
                salvar_listas('disciplinas.json', disciplinas)
                return
        print("Disciplina não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para excluir disciplina
def excluir_disciplina():
    try:
        codigo = int(input("Digite o código da disciplina que deseja excluir: "))
        for disciplina in disciplinas:
            if disciplina['codigo'] == codigo:
                disciplinas.remove(disciplina)
                print("Disciplina excluída")
                salvar_listas('disciplinas.json', disciplinas)
                return
        print("Disciplina não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para incluir turma
def incluir_turma():
    try:
        codigo = int(input("Digite o código da turma: "))
        for turma in turmas:
            if turma['codigo'] == codigo:
                print("Este código já existe.")
                return
        codigo_disciplina = int(input("Digite o código da disciplina da turma: "))
        codigo_professor = int(input("Digite o código do professor da turma: "))
        turma = {'codigo': codigo, 'disciplina': {'codigo': codigo_disciplina}, 'professor': {'codigo': codigo_professor}}
        turmas.append(turma)
        print("Turma incluída")
        salvar_listas('turmas.json', turmas)
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para listar turmas
def listar_turmas():
    if len(turmas) == 0:
        print("Não há turmas cadastradas.")
    for turma in turmas:
        print(f"Código: {turma['codigo']}, Disciplina: {turma['disciplina']['codigo']}, Professor: {turma['professor']['codigo']}")

# Função para editar turma
def editar_turma():
    try:
        codigo = int(input("Digite o código da turma que deseja editar: "))
        for i, turma in enumerate(turmas):
            if turma['codigo'] == codigo:
                novo_codigo = input("Digite o novo código da turma: ")
                if novo_codigo:
                    turmas[i]['codigo'] = int(novo_codigo)
                codigo_disciplina = input("Digite o novo código da disciplina: ")
                if codigo_disciplina:
                    turmas[i]['disciplina']['codigo'] = int(codigo_disciplina)
                codigo_professor = input("Digite o novo código do professor: ")
                if codigo_professor:
                    turmas[i]['professor']['codigo'] = int(codigo_professor)
                print("Turma editada")
                salvar_listas('turmas.json', turmas)
                return
        print("Turma não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para excluir turma
def excluir_turma():
    try:
        codigo = int(input("Digite o código da turma que deseja excluir: "))
        for turma in turmas:
            if turma['codigo'] == codigo:
                turmas.remove(turma)
                print("Turma excluída")
                salvar_listas('turmas.json', turmas)
                return
        print("Turma não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para incluir matrícula
def incluir_matricula():
    try:
        codigo_estudante = int(input("Digite o código do estudante: "))
        codigo_turma = int(input("Digite o código da turma: "))
        for matricula in matriculas:
            if matricula['estudante']['codigo'] == codigo_estudante and matricula['turma']['codigo'] == codigo_turma:
                print("Esta matrícula já existe.")
                return
        matricula = {'estudante': {'codigo': codigo_estudante}, 'turma': {'codigo': codigo_turma}}
        matriculas.append(matricula)
        print("Estudante matriculado na turma")
        salvar_listas('matriculas.json', matriculas)
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para listar matrículas
def listar_matriculas():
    if len(matriculas) == 0:
        print("Não há matrículas cadastradas.")
    for matricula in matriculas:
        print(f"Estudante: {matricula['estudante']['codigo']}, Turma: {matricula['turma']['codigo']}")


# Função para editar matrícula
def editar_matricula():
    try:
        codigo_estudante = int(input("Digite o código do estudante da matrícula que deseja editar: "))
        codigo_turma = int(input("Digite o código da turma da matrícula que deseja editar: "))
        for matricula in matriculas:
            if matricula['estudante']['codigo'] == codigo_estudante and matricula['turma']['codigo'] == codigo_turma:
                novo_codigo_estudante = input("Digite o novo código do estudante: ")
                if novo_codigo_estudante:
                    matricula['estudante']['codigo'] = int(novo_codigo_estudante)
                novo_codigo_turma = input("Digite o novo código da turma: ")
                if novo_codigo_turma:
                    matricula['turma']['codigo'] = int(novo_codigo_turma)
                print("Matrícula editada")
                salvar_listas('matriculas.json', matriculas)
                return
        print("Matrícula não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Função para excluir matrícula
def excluir_matricula():
    try:
        codigo_estudante = int(input("Digite o código do estudante da matrícula que deseja excluir: "))
        codigo_turma = int(input("Digite o código da turma da matrícula que deseja excluir: "))
        for matricula in matriculas:
            if matricula['estudante']['codigo'] == codigo_estudante and matricula['turma']['codigo'] == codigo_turma:
                matriculas.remove(matricula)
                print("Matrícula excluída")
                salvar_listas('matriculas.json', matriculas)
                return
        print("Matrícula não encontrada.")
    except ValueError:
        print("Código inválido. Digite um número inteiro.")


# Loop principal do programa
while True:
    print("\n=== MENU ===")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        while True:
            print("\n=== MENU ESTUDANTES ===")
            print("1. Incluir Estudante")
            print("2. Listar Estudantes")
            print("3. Editar Estudante")
            print("4. Excluir Estudante")
            print("0. Voltar")

            opcao_estudante = input("Escolha uma opção: ")

            if opcao_estudante == "1":
                incluir_estudante()
            elif opcao_estudante == "2":
                listar_estudantes()
            elif opcao_estudante == "3":
                editar_estudante()
            elif opcao_estudante == "4":
                excluir_estudante()
            elif opcao_estudante == "0":
                break
            else:
                print("Opção inválida.")

    elif opcao == "2":
        while True:
            print("\n=== MENU PROFESSORES ===")
            print("1. Incluir Professor")
            print("2. Listar Professores")
            print("3. Editar Professor")
            print("4. Excluir Professor")
            print("0. Voltar")

            opcao_professor = input("Escolha uma opção: ")

            if opcao_professor == "1":
                incluir_professor()
            elif opcao_professor == "2":
                listar_professores()
            elif opcao_professor == "3":
                editar_professor()
            elif opcao_professor == "4":
                excluir_professor()
            elif opcao_professor == "0":
                break
            else:
                print("Opção inválida.")

    elif opcao == "3":
        while True:
            print("\n=== MENU DISCIPLINAS ===")
            print("1. Incluir Disciplina")
            print("2. Listar Disciplinas")
            print("3. Editar Disciplina")
            print("4. Excluir Disciplina")
            print("0. Voltar")

            opcao_disciplina = input("Escolha uma opção: ")

            if opcao_disciplina == "1":
                incluir_disciplina()
            elif opcao_disciplina == "2":
                listar_disciplinas()
            elif opcao_disciplina == "3":
                editar_disciplina()
            elif opcao_disciplina == "4":
                excluir_disciplina()
            elif opcao_disciplina == "0":
                break
            else:
                print("Opção inválida.")

    elif opcao == "4":
        while True:
            print("\n=== MENU TURMAS ===")
            print("1. Incluir Turma")
            print("2. Listar Turmas")
            print("3. Editar Turma")
            print("4. Excluir Turma")
            print("0. Voltar")

            opcao_turma = input("Escolha uma opção: ")

            if opcao_turma == "1":
                incluir_turma()
            elif opcao_turma == "2":
                listar_turmas()
            elif opcao_turma == "3":
                editar_turma()
            elif opcao_turma == "4":
                excluir_turma()
            elif opcao_turma == "0":
                break
            else:
                print("Opção inválida.")

    elif opcao == "5":
        while True:
            print("\n=== MENU MATRÍCULAS ===")
            print("1. Incluir Matrícula")
            print("2. Listar Matrículas")
            print("3. Editar Matrícula")
            print("4. Excluir Matrícula")
            print("0. Voltar")

            opcao_matricula = input("Escolha uma opção: ")

            if opcao_matricula == "1":
                incluir_matricula()
            elif opcao_matricula == "2":
                listar_matriculas()
            elif opcao_matricula == "3":
                editar_matricula()
            elif opcao_matricula == "4":
                excluir_matricula()
            elif opcao_matricula == "0":
                break
            else:
                print("Opção inválida.")

    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")
