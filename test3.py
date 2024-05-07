import json

# Exceção personalizada para nome inválido
class NomeInvalidoError(Exception):
    def __init__(self, mensagem="O nome deve conter apenas letras"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# Classes para entidades
class Aluno:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome
        self.cpf = cpf

    def to_dict(self):
        return {"codigo": self.codigo, "nome": self.nome, "cpf": self.cpf}

class Professor:
    def __init__(self, codigo, nome, cpf):
        self.codigo = codigo
        self.nome = nome 
        self.cpf = cpf

    def to_dict(self):
        return {"codigo": self.codigo, "nome": self.nome, "cpf": self.cpf}

class Disciplina:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def to_dict(self):
        return {"codigo": self.codigo, "nome": self.nome}

class Turma:
    def __init__(self, codigo, codigo_professor, codigo_disciplina):
        self.codigo = codigo
        self.codigo_professor = codigo_professor
        self.codigo_diciplina = codigo_disciplina

    def to_dict(self):
        return {
            "codigo": self.codigo,
            "codigo_professor": self.codigo_professor,
            "codigo_disciplina": self.codigo_disciplina
        }

class Matricula:
    def __init__(self, codigo_turma, codigo_estudante):
        self.codigo_turma = codigo_turma
        self.codigo_estudante = codigo_estudante

    def to_dict(self):
        return {
            "codigo_turma": self.codigo_turma,
            "codigo_estudante": self.codigo_estudante
        }

# Classe para gerenciar a escola
class Escola:
    def __init__(self):
        self.estudantes = []
        self.professores = []
        self.disciplinas = []
        self.turmas = []
        self.matriculas = []
        self.carregar_dados() # Carregar dados do arquivo JSON

    # Método para validar nomes
    def validar_nome(self, nome):
        if not all(part.isalpha() for part in nome.split()):
            raise NomeInvalidoError("O nome deve conter apenas letras")

    # Método genérico para adicionar um item a uma lista
    def adicionar_item(self, lista, criador):
        try:
            item = criador()  # Cria o item usando a função fornecida
            lista.append(item)  # Adiciona à lista
            print("Item adicionado com sucesso!")
        except ValueError as e:
            print(f"Erro ao adicionar item: {e}")

    # Método genérico para listar itens de uma lista
    def listar_itens(self, lista):
        if not lista:
            print("Nenhum item encontrado.")
        else:
            for item in lista:
                print(item.to_dict())  # Usa o método `to_dict()` para exibição
    # Atualizar um item em uma lista
    def atualizar_item(self, lista, atualizar_funcao):
        try:
            atualizar_funcao(lista)  # Chama a função para atualizar o item
        except Exception as e:
            print(f"Erro ao atualizar item: {e}")

    # Excluir um item de uma lista
    def excluir_item(self, lista, codigo):
        removido = None
        for item in lista:
            if item.to_dict().get("codigo") == codigo:
                removido = item
                break
        if removido:
            lista.remove(removido)  # Remover o item da lista
            print("Item excluído com sucesso!")
        else:
            print("Código não encontrado.")

    def salvar_dados(self):
        dados = {
            "estudantes": [estudante.to_dict() for estudante in self.estudantes],
            "professores": [professor.to_dict() for professor in self.professores],
            "disciplinas": [disciplina.to_dict() for disciplina in self.disciplinas],
            "turmas": [turma.to_dict() for turma in self.turmas],
            "matriculas": [matricula.to_dict() for matricula in self.matriculas]
        }

        with open("escola.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")

    def carregar_dados(self):
        try:
            with open("escola.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self.estudantes = [Aluno(**aluno) for aluno in dados.get("estudantes", [])]
                self.professores = [Professor(**professor) for professor in dados.get("professores", [])]
                self.disciplinas = [Disciplina(**disciplina) for disciplina in dados.get("disciplinas", [])]
                self.turmas = [Turma(**turma) for turma in dados.get("turmas", [])]
                self.matrículas = [Matricula(**matricula) for matricula in dados.get("matriculas", [])]
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Iniciando com listas vazias.")

# Função para criar uma matrícula
def criar_matricula():
    try:
        codigo_turma = int(input("Digite o código da turma: "))
        codigo_estudante = int(input("Digite o código do estudante: "))
        return Matricula(codigo_turma, codigo_estudante)
    except ValueError:
        raise ValueError("Os códigos devem ser números inteiros")
# Função para atualizar uma matrícula
def atualizar_matricula(lista):
    codigo_turma = int(input("Digite o código da turma da matrícula a ser atualizada: "))
    codigo_estudante = int(input("Digite o código do estudante da matrícula: "))
    encontrado = False
    for matricula in lista:
        if matricula.to_dict()["código_turma"] == codigo_turma and matricula.to_dict()["código_estudante"] == codigo_estudante:
            novo_codigo_turma = int(input("Digite o novo código da turma: "))
            novo_codigo_estudante = int(input("Digite o novo código do estudante: "))
            matricula.codigo_turma = novo_codigo_turma
            matricula.código_estudante = novo_codigo_estudante
            encontrado = True
            print("Matrícula atualizada com sucesso!")
            break
    if not encontrado:
        print("Matrícula não encontrada.")

# Menu genérico para gerenciar qualquer entidade
def menu_generico(titulo, lista, criar_funcao, atualizar_funcao, escola):
    while True:
        print(f"\n----- MENU {titulo} -----")
        print("(1) Incluir.")
        print("(2) Listar.")
        print("(3) Atualizar.")
        print("(4) Excluir.")
        print("(9) Sair.")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            escola.adicionar_item(lista, criar_funcao)  # Incluir item
        if opcao == "2":
            escola.listar_itens(lista)  # Listar itens
        if opcao == "3":
            escola.atualizar_item(lista, atualizar_funcao)  # Atualizar item
        if opcao == "4":
            código = int(input("Informe o código do item a ser excluído: "))
            escola.excluir_item(lista, código)  # Excluir item
        if opcao == "9":
            break
        else:
            print("Opção inválida. Tente novamente.")


# Menus para gerenciar a escola
def menu_principal():
    escola = Escola()  # Instância da escola

    while True:
        print("\n----- MENU PRINCIPAL -----")
        print("(1) Gerenciar estudantes.")
        print("(2) Gerenciar professores.")
        print("(3) Gerenciar disciplinas.")
        print("(4) Gerenciar turmas.")
        print("(5) Gerenciar matrículas.")
        print("(9) Sair.")

        opcao = input("Informe a opção desejada: ")

        if opcao == "1":
             menu_generico("Alunos",escola.alunos,lambda: Aluno(int(input("Digite o código do aluno: ")), input("Digite o nome do aluno: "), input("Digite o CPF do aluno: ")),
             lambda lista: print("Atualização de alunos em desenvolvimento"),escola, )
             # Gerenciar alunos
        elif opcao == "2":
            menu_generico("Professores",escola.professores,lambda: Professor(int(input("Digite o código do professor: ")), input("Digite o nome do professor: "), 
                input("Digite o CPF do professor: ")),lambda lista: print("Atualização de professores em desenvolvimento"),escola, )  
            # Gerenciar professores
        elif opcao == "3":
           menu_generico("Disciplinas",escola.disciplinas,lambda: Disciplina(int(input("Digite o código da disciplina: ")), input("Digite o nome da disciplina: ")),
                lambda lista: print("Atualização de disciplinas em desenvolvimento"),escola, )
           # Gerenciar disciplinas
        elif opcao == "4":
            menu_generico("Turmas",escola.turmas,lambda: Turma(int(input("Digite o código da turma: ")), int(input("Digite o código do professor: ")), int(input("Digite o código da disciplina: "))),
                lambda lista: print("Atualização de turmas em desenvolvimento"),escola, )
           # Gerenciar turmas
        elif opcao == "5":
            menu_generico("Matrículas",escola.matriculas,criar_matricula,atualizar_matricula,escola,)
            # Gerenciar matrículas
        elif opcao == "9":
            escola.salvar_dados()  # Salvar dados ao sair
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_principal()