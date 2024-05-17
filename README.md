# Raciocino-Logico
 ***Sistema de Gerenciamento Academico***

A temática de nosso projeto da disciplina será um Sistema de Gerenciamento Acadêmico, o que envolverá o cadastro de informações relacionadas aos estudantes, disciplinas, professores e turmas. Este sistema será desenvolvido incrementalmente durante a disciplina. Portanto, as funcionalidades descritas a seguir não serão implementadas ainda esta semana, mas sim aos poucos e ao decorrer da
disciplina conforme as orientações semanais. Dessa forma, veja a seguir um panorama geral das funcionalidades necessárias para o desenvolvimento completo da aplicação, que terá sua entrega final da Semana 08 da disciplina.
# Funcionalidades obrigatórias
### 1) O sistema deverá oferecer a possibilidade de cadastro dos seguintes dados:
    a. estudante;
    b. disciplina;
    c. professor;
    d. turma;
    e. matrícula.
### 2) Para cada uma das funcionalidades descritas no item 1, deve ser possível realizar as seguintes funcionalidades:
    a. incluir;
    b. listar;
    c. excluir;
    d. alterar.
### 3) Para não perder dados ao reiniciar o programa, os dados devem ser armazenados em uma lista, e posteriormente em um arquivo JSON, de forma que, ao reiniciar a aplicação, possamos recuperá-los. 

### Semana 1
- Temas: Apresentação do Python, ferramentas para desenvolvimento, introdução àprogramação,
- variáveis e constantes, operadores aritméticos, entrada e saída de dados.
- Objetivo: Criarscripts simples com entrada, processamento e saída de dados.

### Semana 2
- Temas: Estrutura condicional, operadoresrelacionais e lógicos.
- Objetivo: Criarscripts simples contendo entrada de dados, estrutura de decisão, cálculos e saída de dados.
- Início do desenvolvimento do projeto incluindo a apresentação de um menude opções para o usuário, a leitura da opção desejada e a apresentação da opção selecionada.

### Semana 3
- Temas: Estruturas de repetição e validação de dados.
- Objetivo: Criar scripts que permitam loops finitos e infinitos. Entender loops e estruturas e como utilizálos no projeto acadêmico.
- Inclusão das estruturas de repetição no projeto para permitir a execução infinita do código até que o usuário explicitamente selecione a opção de fechamento da aplicação.

### Semana 4 
- Tema: Listas.
- Objetivo: Criar scripts que permitam armazenamento de coleções de dados em uma estrutura de dados única (lista).
- Apenas a funcionalidade de incluir e listar estudantes devem ser desenvolvidas.

### Semana 5
- Temas: Tuplas e Dicionários.
- Objetivo: Criarscripts que permitam armazenamento de estruturas de dados mais complexas.
- Utilização de listas para armazenamento dos dados cadastrados pelo usuário. Cada posição da lista terá uma tupla ou dicionário representando os dados cadastrados. Desenvolvimento das funcionalidades de exclusão e edição de estudantes. 

### Semana 6
- Tema: Funções
- Objetivo: Criarscripts de maneira modular, visando uma codificação mais organizada e focando no reaproveitamento de código.
- Atividade formativa: Modularizar o sistema, inserindo as principais funcionalidades dentro de funções.

### Semana 7
- Temas: Exceção e arquivos.
- Objetivo: Criar scripts com possibilidade de escrita de dados permanente em disco, bem como o tratamento de exceções e erros.
-Implementar a gravação dos dados cadastrais que se localizam em uma lista de tuplas/dicionários usando arquivos JSON. Criar funções para a escrita e leitura de arquivos.

### Semana 8
- Objetivo: Revisartemáticas vistas nas semanas anteriores.
- Replicar o funcionamento de todas as operações (incluir, editar, listar e excluir) para as turmas, disciplinas, professores e matrícula. Evitar duplicação de código através do uso de funções