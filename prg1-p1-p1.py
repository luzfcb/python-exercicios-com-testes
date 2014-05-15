#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Avaliação P1

def serie1():
    '''Calcule o valor de s, a partir da seguinte série:
    s = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50
    '''
    s = 1
    numerador = 3
    denominador = 2
    while denominador <= 50:
        s = s + (numerador/denominador)
        denominador = denominador + 1
        numerador = numerador + 2
    return round(s,1)

def calcula_idade_canina(idade_humana, porte_do_cao):
    '''Calcule sua idade canina:
    - cães de porte pequeno: dividir sua idade por 5
    - cães de porte médio: dividir sua idade por 6 
    - cães grandes: dividir sua idade por 7
    '''
    if porte_do_cao == 'pequeno':
        fator = 5
    elif porte_do_cao== 'medio':
        fator = 6
    else:
        fator = 7
        
    idade_canina = int(idade_humana / fator)
    return idade_canina

def calcula_quantidade_de_equipes(quantidade_de_alunos):
    ''' 
    Dado uma quantidade de alunos em uma turma, informe quantas 
    possibilidades de tamanhos de grupos são possíveis, sendo que só 
    são aceitos tamanhos de grupos que permitam todos os grupos serem 
    do mesmo tamanho.
    Exemplo: para uma turma de 12 alunos, é possível criar 4 tamanhos 
    de grupo obedecendo a regra:
    - grupos de 2 alunos, com 6 alunos em cada um
    - grupos de 3 alunos, com 4 alunos em cada um
    - grupos de 4 alunos, com 3 alunos em cada um
    - grupos de 6 alunos, com 2 alunos em cada um
    Se não houverem possibilidades de organizar os alunos segundo essa 
    regra, a função deve retornar 0.
    '''
    tamanho_do_grupo = 2
    grupos_possiveis = 0
    while tamanho_do_grupo < (quantidade_de_alunos/2) + 1:
        if quantidade_de_alunos % tamanho_do_grupo == 0:
            grupos_possiveis += 1
        tamanho_do_grupo += 1
    return grupos_possiveis

def calcula_aumento_salario(salario_atual):
    ''' Calcule o aumento de salário de acordo com a seguinte tabela:
    - até 1 SM(inclusive): aumento de 20%
    - de 1 até 2 SM(inclusive): aumento de 15%
    - de 2 até 5 SM(inclusive): aumento de 10%
    - acima de 5 SM: aumento de 5% 
    Salário mínimo para referência: R$ 724,00
    '''
    salario_minimo = 724.00
    if salario_atual <= salario_minimo:
        percentual_aumento = 20
    elif salario_atual <= salario_minimo * 2:
        percentual_aumento = 15
    elif salario_atual <= salario_minimo * 5:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
    
    reajuste_salario = salario_atual * (percentual_aumento / 100)
    novo_salario = salario_atual + reajuste_salario
    return round(novo_salario,2)

# Área de testes: não altere desse ponto em diante!
acertos = 0
total = 0 

def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = ' Falhou.'
    else:
        prefixo = ' Passou.'
        acertos += 1
    print ('%s Esperado: %s \tObtido: %s' % (prefixo,repr(esperado), 
        repr(obtido)))

def main():
    print('Série 1:')
    test(serie1(), 95.5)

    print('Idade canina:')
    test(calcula_idade_canina(40,'pequeno'),8)
    test(calcula_idade_canina(40,'medio'),6)
    test(calcula_idade_canina(40,'grande'),5)

    print('Quantidade de equipes')
    test(calcula_quantidade_de_equipes(9), 1) 
    test(calcula_quantidade_de_equipes(12), 4) #Equipes de 2, 3, 4 e 6
    test(calcula_quantidade_de_equipes(13), 0) #Não forma equipes
    test(calcula_quantidade_de_equipes(14), 2) #Equipes de 2 e 7
    test(calcula_quantidade_de_equipes(15), 2) #Equipes de 3 e 5
    test(calcula_quantidade_de_equipes(16), 3) #Equipes de 2, 4 e 8
    test(calcula_quantidade_de_equipes(40), 6) #Equipes de 2, 4, 5, 8, 10 e 20
    
    print('Aumento salarial:')
    # até 1 SM: 20%
    test(calcula_aumento_salario(500.00), 600.00) 
    test(calcula_aumento_salario(724.00), 868.80) 
    # 1-2 SM: 15%
    test(calcula_aumento_salario(725.00), 833.75)
    test(calcula_aumento_salario(1448.00), 1665.20)
    # 2-5 SM: 10%
    test(calcula_aumento_salario(1449.00), 1593.90)
    test(calcula_aumento_salario(3620.00), 3982.00)
    # >5 SM: 5%
    test(calcula_aumento_salario(3621.00), 3802.05)
    test(calcula_aumento_salario(4000.00), 4200.00)

     
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
