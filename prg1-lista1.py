#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 1

def soma_dois_inteiros(numero_inteiro1,numero_inteiro2):
    ''' Recebe dois numeros inteiros, e retorna a sua soma'''
    #return soma

def metro_para_milimetros(metros):
    ''' Recebe um valor em metros, e retorna o valor em milimetros'''
#    return milimetros

def dias_para_segundos(dias,horas,minutos,segundos):
    ''' Recebe uma data em dias com horas,minutos,segundos, e retorna 
    a data em segundos'''
#    return tempo

def aumento_salarial(salario,porcentagem):
    ''' Recebe um salario e sua porcentagem de aumento, e retorna
    o novo salario'''
#    return novo_salario

def preco_com_desconto(preco,desconto):
    ''' Recebe um preço e sua porcentagem de desconto, e retorna 
    novo preço'''
#    return novo_preco

def tempo_para_percorrer_uma_distancia(distancia,velocidade):
    ''' Recebe uma distancia e a velocidade que percorreras essa 
    distancia, e retorna as horas que seriam gastas para percorrer
     em linha reta'''
#    return tempo_horas

def celsius_para_fahrenheit(celsius):
    ''' Recebe uma temperatura em celsius, e retorna a temperatura 
    em fahrenheit'''
#    return temperatura

def fahrenheit_para_celsius(fahrenheit):
    ''' Recebe uma temperatura em fahrenheit, e retorna a temperatura
     em celcius'''
#    return temperatura

def preco_aluguel_carro(dias,km):
    ''' Recebe uma quantidade de dias que o carro foi alugado e a 
    quantidade de kilometros rodados, e retorna o valor a ser pago.
    1 dia: 60 reais mais R$ 0,15 por km rodado.'''
#    return preco

def dias_perdidos_por_fumar(cigarros,anos):
    ''' Recebe uma quantidade de cigarros fumados por dia e a quantidade
     de anos que fuma, e retorna o total de dias perdidos, sabendo que
     cada cigarro reduz a vida em 10 minutos.'''
#    return dias

def dois_elevado_a_um_milhao():
    ''' Calcula dois elevado a um milhão, e retorna a quantidade de 
    algarismos'''
#    return quantidade_numeros

# Área de testes: só mexa aqui se souber o que está fazendo!
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
    print ('%s Esperado: %s \tObtido: %s' % (prefixo, repr(esperado), 
        repr(obtido)))

def main():
    print('Soma dois inteiros:')
    test(soma_dois_inteiros(0,0), 0) 
    test(soma_dois_inteiros(-1,0), -1) 
    test(soma_dois_inteiros(1,1), 2) 
    test(soma_dois_inteiros(0,-1), -1) 
    test(soma_dois_inteiros(10,10), 20) 

    print('Metros para milimetros:')
    test(metro_para_milimetros(0), 0) 
    test(metro_para_milimetros(1), 1000) 
    test(metro_para_milimetros(1.8), 1800) 
    test(metro_para_milimetros(1.81), 1810) 

    print('Dias,horas,minutos e segundos para segundos:')
    test(dias_para_segundos(10,20,59,1), 939541)
    test(dias_para_segundos(0,23,59,59), 86399)
    test(dias_para_segundos(1,1,1,1), 90061)
    test(dias_para_segundos(1,0,0,0), 86400)

    print('Aumento salarial baseado na porcentagem de aumento:')
    test(aumento_salarial(1330,20), 1596.00)
    test(aumento_salarial(1000,0), 1000.00)
    test(aumento_salarial(1000.10,123), 2230.22)
    test(aumento_salarial(0.0,200), 0.00)

    print('Desconto do preco atual baseado na porcentagem do desconto:')
    test(preco_com_desconto(1330,20), 1064.00)
    test(preco_com_desconto(1000,0), 1000.00)
    test(preco_com_desconto(1000.10,5.5), 945.09)
    test(preco_com_desconto(0.0,200), 0.00)

    print('Tempo gasto para percorrer um distancia a uma velocidade'
    'constante(linha reta):')
    test(tempo_para_percorrer_uma_distancia(1330,20), 66.50)
    test(tempo_para_percorrer_uma_distancia(1000,100), 10.00)
    test(tempo_para_percorrer_uma_distancia(1000,123), 8.13)
    test(tempo_para_percorrer_uma_distancia(100000,201), 497.51)

    print('Celsius para Fahrenheit:')
    test(celsius_para_fahrenheit(30), 86.00)
    test(celsius_para_fahrenheit(300), 572.00)
    test(celsius_para_fahrenheit(-100), -148.00)
    test(celsius_para_fahrenheit(1), 33.80)

    print('Fahrenheit para Celsius:')
    test(fahrenheit_para_celsius(30), -1.11)
    test(fahrenheit_para_celsius(300), 148.89)
    test(fahrenheit_para_celsius(-100), -73.33)
    test(fahrenheit_para_celsius(1), -17.22)

    print('Preco a pagar pelo aluguel do carro:')
    test(preco_aluguel_carro(10,100), 615.00)
    test(preco_aluguel_carro(13,133), 799.95)
    test(preco_aluguel_carro(1,0), 60.00)
    test(preco_aluguel_carro(3,79), 191.85)

    print('Total de dias que perdeu de viver por ter fumados:')
    test(dias_perdidos_por_fumar(10,10), 253.47)
    test(dias_perdidos_por_fumar(13,13), 428.37)
    test(dias_perdidos_por_fumar(0,110), 0.00)
    test(dias_perdidos_por_fumar(3,79), 600.73)

    print('Calcula a quantidade de numeros que ha em dois elevado a um'
    'milhao:')
    test(dois_elevado_a_um_milhao(), 301030)

if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
