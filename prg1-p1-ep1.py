#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Avaliação P1

def poupanca(saldo, quantidade_meses, juros_ao_mes):
    '''Informe o saldo inicial de uma conta poupança, a quantidade de
    meses em que o dinheiro ficará aplicado e o juro mensal a ser aplicado.
    Calcule e retorne o saldo da poupança atualizado.'''
    mes = 1
    while mes <= quantidade_meses:
        rendimento_mes = saldo * (juros_ao_mes / 100)
        saldo += rendimento_mes
        mes += 1
    return saldo

def pares_e_divisiveis_por_7(limite_inferior=1067, limite_superior=3627):
    '''Entre 1067 e 3627 (inclusive), quantos números são pares e 
    também divisíveis por 7? 
    '''
    numero = limite_inferior
    divisiveis = 0
    while numero <= limite_superior:
        if numero % 2 == 0 and numero % 7 == 0:
            divisiveis += 1
        numero += 1
    return divisiveis

def numero_de_ouro(n):
    '''Cálculo do número de ouro (golden ratio) através da série de Fibonacci
    O número de ouro é: 1.61803398875
    O número áureo é aproximado pela divisão do enésimo termo da 
    Série de Fibonacci (0, 1,1,2,3,5,8,13,21,34,55,89,..., pelo termo anterior. 
    Essa divisão converge para o número áureo conforme tomamos um número 
    cada vez maior. 
    Podemos ver um exemplo dessa convergência a seguir, em que a série de 
    Fibonacci está escrita até seu oitavo termo [0, 1, 1, 2, 3, 5, 8, 13]:
     2/1 = 2 
     3/2 = 1,5 
     5/3 = 1,666... 
     8/5 = 1,6 
     13/8 = 1,625
    '''
    a = 0
    b = 1
    i = 1
    while i < n:
        #a, b = b, a+b
        aux = a
        a = b
        b = aux + b
        i = i + 1
    return round(b/a,11)

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
    print ('%s Esperado: %s \tObtido: %s' % (prefixo,repr(esperado), 
        repr(obtido)))

def main():
    print('Poupança:')
    test(poupanca(1000,1,1), 1010.00) 
    test(poupanca(1000,2,1), 1020.10) 
    test(poupanca(1000,1,2), 1020.00) 
    test(poupanca(1000,2,2), 1040.40) 
    
    print('Pares e divisíveis por 7:')
    test(pares_e_divisiveis_por_7(), 183) 

    print('Número de ouro:')
    test(numero_de_ouro(2), 1.00000000000) 
    test(numero_de_ouro(3), 2.00000000000) 
    test(numero_de_ouro(4), 1.50000000000) 
    test(numero_de_ouro(5), 1.66666666667)
    test(numero_de_ouro(6), 1.60000000000)
    test(numero_de_ouro(7), 1.62500000000)
    test(numero_de_ouro(30), 1.61803398875)
  
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
