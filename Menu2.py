'''
Aluno : Thiago Dorfman Lufchitz
Curso :ADS - Analise e Desenvolvimento de Software
'''
import json
estudantes = []
professores = []
diciplinas = []
turmas = []
matriculas = []

def escrever_json(colegio,Flag):
    if Flag == 1: # n
        try:
            with open('escola.json', 'w', encoding = 'utf-8') as colegio:
                json.dump(colegio,escola.json) # type: ignore
        except FileExistsError:
                print("Aquivo nao existe")
    elif Flag == 2:
        inc()
    elif Flag == 3:
        inc()
    elif Flag == 4:
        inc()
    elif Flag == 5:
        inc()
  
def menu_pri():     # Menu Principal
    print("\n----- MENU PRINCIPAL -----")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matriculas.")
    print("(9) Sair.")

def menu_gere(): # Submenu Generico
     print("(1) Incluir.")
     print("(2) Listar.")
     print("(3) Atualizar.")
     print("(4) Excluir.")
     print("(9) Voltar ao menu principal.\n")

def menu_estu(x): # menu Estudantes       || Flag = 1
    print("\n***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op(x) 
    return None

def menu_pro(x): # menu Professores       || Flag = 2
    print("\n***** [PROFESSORES] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op(x)
    return None

def menu_disc(x): # menu Diciplina        || Flag = 3
    print("\n***** [DICIPLINAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op(x)
    return None
    
def menu_turm(x): # menu Turma             || Flag = 4
    print("\n***** [TURMAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op(x)
    return None
    
def menu_matri(x): # menu Matriculas        || Flag = 5
    print("\n***** [MATRICULAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op(x) 
    return None  

def menu_op(Flag): # menu de Opcoes
     while True:
       
        opcao = input("Informe a opção desejada: ") # selecionando a opcao 
        if opcao == "1" and (Flag >= 1 or opcao == "Incluir"): # selecionando a opcao e qual menu esta sendo acessado o indentificador do meno e a variavel Flag
            if Flag == 1:
                inc(Flag,a = int(input("Codigo do Aluno: ")), b = input("Nome: "), c = input("Cpf: ")) # adicionando na lista o codigo o nome e o cpf do aluno que sera digitado pelo usuario
            elif Flag == 2:
                inc()
            elif Flag == 3:
                inc()
            elif Flag == 4:
                inc()
            elif Flag == 5:
                inc()
        elif opcao == "2" and  (Flag >= 1 or opcao == "Listar"): # mostrar o que esta dentro da lista
            if Flag == 1:
                listar(Flag)
            elif Flag == 2:
                listar(Flag)
            elif Flag == 3:
                listar(Flag)
            elif Flag == 4:
                listar(Flag)
            elif Flag == 5:
                listar(Flag)
        elif opcao == "3" and  (Flag >= 1 or opcao == "Atualizar"): # opcao no menu para atualizar os dados em desenvolvimento ainda 
            if Flag == 1:
                atualiz(Flag)
            elif Flag == 2:
                atualiz(Flag)
            elif Flag == 3:
                atualiz(Flag)
            elif Flag == 4:
                atualiz(Flag)
            elif Flag == 5:
                atualiz(Flag)
        elif opcao == "4" and  (Flag >= 1 or opcao == "Excluir"): # opcao de excluir dados inceridos
            if Flag == 1:
            #    dev()
               excluir(Flag,x = int(input("O Codigo do Aluno que deseja Excluir: ")))
            elif Flag == 2:
              dev() 
            #   excluir()
            elif Flag == 3:
               dev() 
            #   excluir()
            elif Flag == 4:
               dev() 
            #   excluir()
            elif Flag == 5:
               dev() 
            #   excluir()
        elif opcao == "9" or  opcao =="Sair":
           break
        else:
            print("\nOpção Invalida. Tente novamente.\n")
    
def inc(Flag,a,b,c): #metodo que incluindo na lista as informaçoes e em qual lista deve ser adicionada
    if Flag == 1:
        estudantes.append(f"Codigo: {a}, Nome: {b}, Cpf: {c}")
    elif Flag == 2:
        professores.append("a,b,c")
    elif Flag == 3:
        diciplinas.append("a,b,c")
    elif Flag == 4:
        turmas.append("a,b,c")
    elif Flag == 5:
        matriculas.append("a,b,c")
    print("===== INCLUINDO =====\n")
    

def listar(Flag): #metodo que mostra o que tem dentro da lista e vendo que menu foi pedido para mostrar
    print("===== LISTANDO =====")
    if Flag == 1:
        if len(estudantes) == 0:
            print("Não a aluno cadastrado!!")
        else:
            for i in estudantes:
                print(f"{i}")
    elif Flag == 2:
        if len(professores) == 0:
            print("Não a Professor cadastrado!!")
        else:
            for i in professores:
                print(f"{i}")
    elif Flag == 3:
        if len(diciplinas) == 0:
            print("Não a Diciplina cadastrada!!")
        else:
            for i in diciplinas:
                print(f"{i}")
    elif Flag == 4:
        if len(turmas) == 0:
            print("Não a alunos cadastrados!!")
        else:
            for i in turmas:
                print(f"{i}")
    elif Flag == 5:
        if len(matriculas) == 0:
            print("Não a alunos cadastrados!!")
        else:
            for i in matriculas:
                print(f"{i}")
   
        
def atualiz(Flag): # metodo de atualizao em desenvolvimento
    print("\n===== ATUALIZAÇÃO =====")
    if Flag == 1:
        x = input("Digite o Codigo do Aluno: ")
        aux = -1 ; cont = 0
        for i,aluno in enumerate(estudantes):
            if x in aluno:
                aux = i
                break       
        if aux != -1:
            excluir(Flag,x)
            w = int(input("Digite o Codigo do Aluno Novo: "))
            y = input("Nome novo: ")
            z = input("Cpf novo: ")
            cont+= 1
            estudantes.append(f"Codigo: {w}, Nome: {y} , Cpf: {z}")
            print(f"===== ATUALIZADO!! =====\n")
        if cont == 0:        
            print("Aluno nao encontrado")
    elif Flag == 2:
        print(professores)
    elif Flag == 3:
        print(diciplinas)
    elif Flag == 4:
        print(turmas)
    elif Flag == 5:
        print(matriculas)
    

def excluir(Flag,x): # metodo de excluir dados
    if Flag == 1:
        # print(estudantes)
        remov = None
        for aluno in estudantes:
            if f"Codigo: {x}" in aluno:
                remov = aluno
                break
        if remov:
            estudantes.remove(remov)
            print("===== EXCLUINDO =====")
            # print(estudantes)
        else:
            print("Aluno com esse código não encontrado")
    elif Flag == 2:
        for i in professores:
            print(f"{i}")
    elif Flag == 3:
        for i in diciplinas:
            print(f"{i}")
    elif Flag == 4:
        for i in turmas:
            print(f"{i}")
    elif Flag == 5:
        for i in matriculas:
            print(f"{i}")
    

def dev():
    print("\n===== EM DESENVOLVIMENTO =====")   
    
def main(): # metodo da funcao principal
    while True:
        menu_pri()
        opcao = input("Informe a opção desejada: ")
        
        if opcao =="1":
            menu_estu(1)
        elif opcao == "2":
            dev()
            # menu_pro(2)
        elif opcao == "3":
            dev()
            # menu_disc(3)
        elif opcao == "4":
            dev()
            # menu_turm(4)
        elif opcao == "5":
            dev()
            # menu_matri(5)
        elif opcao == "9":
            break
        else:
            print("\nOpção Invalida. Tente novamente.\n")
            
if __name__ == "__main__":
    main()
    print("\n ===== Saindo do Programa =====\n")