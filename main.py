#Atribuição de Nomes (Variáveis ​​e Constantes)

my_first_variable = 1 #minha primeira variável tem o valor de 1.
my_first_variable = 2 #minha segunda variável tem o valor de 2. Agora essa variável está gravada na memória do computador, a primeira variável nao será mais usada.

print(type(my_first_variable)) #print é uma função de impressão na tela, type serve para mostrar qual a classe da variável.
print(my_first_variable) #vai imprimir na tela o valor da minha variável.

my_first_variable = "Now, i'm a string."
print(type(my_first_variable)) #mudança de classe da variável
print(my_first_variable) #agora ela é uma string (frase).

import collections
my_first_variable = collections.Counter([1,2,3,4,5,6,7,8,9]) #Agora a variável está religada a um objeto de contagem.
print(type(my_first_variable)) #vamos ver qual será o tipo da variável.

#Constantes: são atribuidas com letras maiusculas(CAPS) e _(underline), elas nunca irão mudar de valor.
MY_FIRST_CONSTANT = 40
print(MY_FIRST_CONSTANT)
MY_FIRST_CONSTANT = 50
print(MY_FIRST_CONSTANT) #nota que agora temos duas constantes com valores diferentes.
    
""" 
Não altere o valor de constates, isso pode causar problemas no seu código.
"""

#Funções: Em python, as unidades de funcionalidades são atribuidas em funções (def), que são elas próprias objetos.
#Quando funções são vinculadas a um nome de classe, elas são chamadas de métodos.
#Funções e classes relacionadas(com seus métodos) podem ser agrupadas no mesmo arquivo ou módulo e importadas parcial ou integralmente para usar em outros programas.
#A def (palavra-chave) inicia uma definição da função, cada função pode ter zero ou mais parâmetros formais entre() parenteses, seguidos de : dois pontos
#As instruções para o corpo da função para o corpo da função começam na linha a seguir def e devem ser recuadas em um bloco:

def add_two_numbers(number_one, number_two):
    total = number_one + number_two
    print(total)

add_two_numbers(4,3)


