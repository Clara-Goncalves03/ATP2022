#Modelo: [(nome,desc,periodo,duracao,_id)]

#se tiver o ficheiro noutra pasta acima, coloco file = open("../nomedapasta/obras.csv", "r")

import csv     #para importar uma biblioteca para ler csv

def lerObras(filename):    #estou a fazer esta função para depois na aulaP6 fazr um import disto e para poder usar tudo o que está aqui
    file = open(filename, "r", encoding="UTF8")
    file.readline()
    csv_file = csv.reader(file, delimiter=";")  #agora, na linha abaixo, vamos iterar sobre isto
    lista = []
    for linha in csv_file:
        lista.append(tuple(linha))   #converter lista em tuplo
    return lista

def contaObras(obras):
    return len(obras)

def imprimeObras(obras):
    for obra in obras:
        nome, descricao, ano, periodo, compositor, duracao, id = obra
        #print(nome, descricao, compositor, ano)
        print(f"|{nome[:10]:20}  |  {descricao[:25]:10} ... | {ano:10}")

def ordenaLetras(l):
    return l[0]

def ordenaNumeros(n):
    return n[1]

def ordenaAlfabet(obras):
    for obra in obras:
        listaTuplos = []
        nome, descricao, ano, periodo, compositor, duracao, id = obra 
        listaTuplos.append((nome, ano))
        listaTuplos.sort(key = ordenaLetras)
        print(f"|{nome[:10]:20}  |  {ano[:4]:10}")

def ordenaCrescente(obras):
    for obra in obras:
        listaTuplos2 = []
        nome, descricao, ano, periodo, compositor, duracao, id = obra 
        listaTuplos2.append((nome, ano))
        listaTuplos2.sort(key = ordenaNumeros)
        print(f"|{nome[:10]:20}  |  {ano[:4]:10}")

def compositores(obras):
    for obra in obras:
        listaCompost = []
        nome, descricao, ano, periodo, compositor, duracao, id = obra
        listaCompost.append(compositor)
        listaCompost.sort()
        print(listaCompost)


def distribPeriodo(obras):
    distribuicao1 = {}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if periodo in distribuicao1:
            distribuicao1[periodo] = distribuicao1[periodo] + 1
        else:
            distribuicao1[periodo] = 1
    print(distribuicao1)


def distribAno(obras):
    distribuicao2 = {}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if periodo in distribuicao2:
            distribuicao2[ano] = distribuicao2[ano] + 1
        else:
            distribuicao2[ano] = 1
    print(distribuicao2)


def distribCompositor(obras):
    distribuicao3 = {}
    for obra in obras:
        nome, desc, ano, periodo, compositor, duracao, id = obra
        if periodo in distribuicao3:
            distribuicao3[compositor] = distribuicao3[compositor] + 1
        else:
            distribuicao3[compositor] = 1
    print(distribuicao3)


def menu():
    print("(1) Número de obras")
    print("(2) Informações sobre a obra")
    print("(3) Ordenar alfabeticamente os titulos das obras")
    print("(4) Ordenar crescentemente os anos das obras")
    print("(5) Compositores")
    print("(6) Distribuição das obras por período")
    print("(7) Distribuição das obras por ano")
    print("(8) Distribuição das obras por compositor")
    print("(0) Sair")
    return int(input("Escolhe as opções possíveis."))

 



