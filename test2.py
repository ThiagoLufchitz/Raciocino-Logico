'''
Aluno : Thiago Dorfman Lufchitz
Curso :ADS - Analise e Desenvolvimento de Software
'''
'''
def Flag(): # flag para marcada que tipo de menu estas
    x = 0
    f = x
'''

def menu_pri():     # Menu Principal
    print("----- MENU PRINCIPAL -----")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar professores.")
    print("(3) Gerenciar disciplinas.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matriculas.")
    print("(9) Sair.")

def menu_gere(): # menu Generico
     print("(1) Incluir.")
     print("(2) Listar.")
     print("(3) Atualizar.")
     print("(4) Excluir.")
     print("(9) Voltar ao menu principal.")

def menu_estu(): # menu Estudantes 
    print("***** [ESTUDANTES] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op() 

def menu_pro(): # menu Professores
    print("***** [PROFESSORES] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op()

def menu_disc(): # menu Diciplina
    print("***** [DICIPLINAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op()
    
def menu_turm():    # menu Turma
    print("***** [TURMAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op()
    
def menu_matri(): # menu Matriculas
    print("***** [MATRICULAS] MENU DE OPERAÇÕES *****")
    menu_gere()
    menu_op()   

def menu_op(): # menu de Opcoes
     while True:
        opcao = input("Informe a opção desejada: ")
        
        if opcao == "1" or opcao == "Incluir":
            inc()
        elif opcao == "2" or opcao == "Listar":
            listar()
        elif opcao == "3" or opcao == "Atualizar":
            atualiz()
        elif opcao == "4" or opcao == "Excluir":
            excluir()
        elif opcao == "9" or  opcao =="Sair":
            menu_pri()
            break
        else:
            print("Opção Invalida. Tente novamente.")
    
def inc():
    print("===== INCLUINDO =====")

def listar():
    print("===== LISTANDO =====")
    
def atualiz():
    print("===== ATUALIZAÇÃO =====")

def excluir():
    print("===== EXCLUINDO =====")   
    
def main():
    while True:
        menu_pri()
        opcao = input("Informe a opção desejada: ")
        
        if opcao =="1":
            menu_estu()
        elif opcao == "2":
            menu_pro()
        elif opcao == "3":
            menu_disc()
        elif opcao == "4":
            menu_turm()
        elif opcao == "5":
            menu_matri()
        elif opcao == "9":
            break
        else:
            print("Opção Invalida. Tente novamente.")
            
if __name__ == "__main__":
    main()
    print("Saindo do Programa")