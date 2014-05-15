#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Avaliação EP1

def poupanca(saldo, quantidade_meses, juros_ao_mes):
    '''Informe o saldo inicial de uma conta poupança, a quantidade de
    meses em que o dinheiro ficará aplicado e o juro mensal a ser aplicado.
    Calcule e retorne o saldo da poupança atualizado.'''
    
def divisivel_por_7_e_9(n=1):
    '''Quais é o n-ésimo número divisível por 7 e 9?
    '''

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
    test(divisivel_por_7_e_9(), 63) 
    test(divisivel_por_7_e_9(2), 126) 
    test(divisivel_por_7_e_9(3), 189) 

    print('Número de ouro:')
    test(numero_de_ouro(1), 1.00000000000) 
    test(numero_de_ouro(2), 2.00000000000) 
    test(numero_de_ouro(3), 1.50000000000) 
    test(numero_de_ouro(4), 1.66666666667)
    test(numero_de_ouro(5), 1.60000000000)
    test(numero_de_ouro(6), 1.62500000000)
    test(numero_de_ouro(30), 1.61803398875)
  
if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" %(total, acertos,
     total-acertos, float(acertos*10)/total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")
