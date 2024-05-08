primeiro_valor = 4.0    
segundo_valor = 2.0
multiplicador= primeiro_valor * segundo_valor
divisao = primeiro_valor / segundo_valor
# print(multiplicador)   
# print(divisao)
# x = 18
# y = 3
# if (4 * y > x - 1):
#     print("echo")
# elif(2 * x < y):    
#     print("dot")
# elif(y > x - 10):
#     print("echo dot")
# else:
#     print("dot echo")

# print(17% (8-4) + 4 * 6)
# print(17 // 4 - 8 * 4 // 2 - 5 + 8)

# a = 23 - 25 / 5 + 3 * 4
# b = (17 - 9) * 3 / 4 - 10

# print(a + b)
# print(2 * b - a)
cont = 1
while cont < 8:
    if (cont < 5):
        print(cont + 2)
    else:
        print(cont - 1)
    cont = cont + 1
# soma = 0

# for cont in range(1, 10, 2):
#     soma = soma + cont
#     print("Contador = ", cont)
# print("Soma = ", soma)
'''
 nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")

with open(nome, 'w', encoding='utf-8') as arq:
    # CORPO DO WITH
    arq.write("    O poeta é um fingidor.      \n")
    arq.write("    Finge tão completamente     \n")
    arq.write("    Que chega a fingir que é dor\n")
    arq.write("    A dor que deveras sente.    \n")
    arq.write("                Fernando Pessoa.\n")
    
nome = "poesia.txt"    # poderia ser um input("Digite o nome do arquivo: ")

with open(nome, 'r', encoding='utf-8') as arq_entrada:
    # CORPO DO WITH
    conteudo = arq_entrada.read()

# continue o programa usando conteudo
print(conteudo)    
'''