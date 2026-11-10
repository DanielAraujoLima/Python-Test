'''EXERCÍCIO 1:'''
"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {1letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
"""


'''RESPOSTA'''

nome = input('digite seu nome: ')
idade = input('digite sua idade: ')


if nome and idade:
    print(f'seu nome é {nome}')
    print(f'sua idade é {idade}')
    print(f'seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('seu nome contém espaços')
    else:
        print('seu nome não contém espaços')    

    print(f'seu nome tem {len(nome)} letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
else:
    print('desculpe você deixou campos vazios')






'''EXERCÍCIO 2:'''
"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

'''RESPOSTA'''

numero = input('Digite um número inteiro: ')
if numero == '':
    print('Você não digitou nada')
else:
    try:
        numero = int(numero) 
        if numero % 2 == 0:
            print('Esse número é par')
        else:
            print('Esse número é ímpar')
    except ValueError:
        print('Você não digitou nenhum número inteiro')


'''OUTRA SOLUÇÃO'''

entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número {entrada_int} é {par_impar_texto}')
    else:
        print('Você não digitou um número inteiro')



'''EXERCÍCIO 3:'''
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
'''RESPOSTA'''
horario_horas = input('Que horas são? ')
try:
    horario = int(horario_horas)
    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa noite')
    else:
        print('O horário que digitou não existe')
except:
    print('Por favor, digite um número inteiro')



'''EXERCÍCIO 4:'''
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
'''RESPOSTA'''


nome = input('Digite seu nome ')
qnt_caracteres = len(nome)
if qnt_caracteres > 1:
    if qnt_caracteres <= 4:
        print('Seu nome é curto')
    elif 5 <= qnt_caracteres <= 6:
        print('Seu nome é normal')
    elif qnt_caracteres > 6:
        print('Seu nome é grande')
    else:
        print('Você não digitou seu nome')
else:
    print('Digite mais que uma letra')





'''EXERCÍCIO 5:'''
"""
Iterando strings com while
"""

'''RESPOSTA'''

#       012345678910
nome = 'Luiz Otávio'
i = 0


while i < len(nome):
    print (nome[i])
    i += 1


print('acabou')



'''OU'''



nome = 'Maria Helena'  # Iteráveis

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)







'''EXERCÍCIO 6:'''
'''calculadora usando while'''

'''RESPOSTA'''

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (+-*/): ')
    num_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        num_validos = True
    except:
        num_validos = None

    if num_validos is None:
        print('Um ou ambos os números são invalidos')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('operador invalido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue


    if operador == '+':
        resultado = num_1_float + num_2_float

        if resultado.is_integer():
            resultado = int(resultado)

        print(f'{numero_1} + {numero_2} = {resultado}')

    elif operador == '-':
        resultado = num_1_float - num_2_float

        if resultado.is_integer():
            resultado = int(resultado)

        print(f'{numero_1} - {numero_2} = {resultado}')

    elif operador == '*':
        resultado = num_1_float * num_2_float

        if resultado.is_integer():
            resultado = int(resultado)

        print(f'{numero_1} * {numero_2} = {resultado}')

    elif operador == '/':
        resultado = num_1_float / num_2_float

        if resultado.is_integer():
            resultado = int(resultado)

        print(f'{numero_1} / {numero_2} = {resultado}')

    else:
        print('Nunca deveria chegar aqui')




    sair = input('Você quer sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair is True:
        break






    '''EXERCÍCIO 7:'''
    '''INTERAÇÃO COM O WHILE, ME DIGA QUAL FOI A LETRA DESSA FRASE QUE MAIS APARECEU'''
    '''RESPOSTA'''

frase = 'O verdadeiro sucesso não está em nunca falhar, mas em aprender a levantar após cada queda com mais sabedoria.'\
'Cada desafio que enfrentamos hoje é a base para construirmos uma versão mais forte e resiliente amanhã.'\
'Portanto, valorize a sua jornada, acredite nos seus passos e nunca subestime o poder de recomeçar.'

qnt_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
i = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qnt_apareceu_mais_vezes_atual = frase.count(letra_atual)

    if qnt_apareceu_mais_vezes < qnt_apareceu_mais_vezes_atual:
        qnt_apareceu_mais_vezes = qnt_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual

    i += 1


print(
    'A letra que mais apareceu nesse texto foi'
    f' "{letra_apareceu_mais_vezes}" '
    f'que apareceu {qnt_apareceu_mais_vezes}x'
)








'''EXERCÍCIO 8:'''
"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

'''PRA VC LIMPAR O TERMINAL ANTES DE EXECUTAR O COMANDO USANDO OS COMANDOS DE IMPORTAMENTO OS E ASSIM,
PRIMEIRO C IMPORTA O OS E DPS COLOCA NO CODIGO O COMANDO QUE VC QUER DELE
CUIDADO POIS PRA LIMPAR O TERMINAL SE USA CLEAR NO MAC, LINUX E WINDOWS MAIS RECENTES
SE N FOR USASSE CLS
'''

'''RESPOSTA'''

import os


palavra_escondida = 'sabonete'
letras_digitadas = ''
total_de_tentativas = 0

while True:
    palavra_secreta = input('Digite uma letra: ').lower()

    if not palavra_secreta.isalpha():
        print('Isso não é uma letra, por favor digite uma letra')
        continue

    if len(palavra_secreta) > 1:
        print('digite apenas uma letra')
        continue

    letras_digitadas += palavra_secreta
    total_de_tentativas += 1
    palavras_formatada = ''

    for letra_palavra in palavra_escondida:
        if letra_palavra in letras_digitadas:
            palavras_formatada += letra_palavra
        else:
            palavras_formatada += '*'

    if palavras_formatada == 'sabonete':
        os.system('cls')
        print(f'Palavra formatada: "{palavras_formatada}"')
        print(f'PARABÉNS, VOCÊ ACERTOU TODAS AS LETRAS EM {total_de_tentativas} TENTATIVAS')
        letras_digitadas = ''
        total_de_tentativas = 0    

    print(f'Palavra formatada: {total_de_tentativas}x {palavras_formatada}')





'''EXERCÍCIO 9:
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
'''
'''RESPOSTA'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))





'''EXERCÍCIO 10:'''
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.


OBS: DOIS MÉTODOS DE FAZER ESSE EXERCÍCIOS UM PARA REMOVER OS ITENS USANDO INDICES AONDE USAMOS TRY E EXCEPT E O OUTRO
PARA REMOVER OS ITENS USANDO O NOME DO ITEM EXATAMENTE IGUAL DO JEITO Q ADICIONAMOS, MAS E RECOMENDADO USAR A PRIMEIRA FORMA
DO TRY E EXCEPT NO INDICES PQ E MAIS SEGURO E FACIL DE USAR
"""

'''RESPOSTA'''

import os
carrinho = []

while True:
    print('Selecione uma das opções abaixo')
    produtos = input('[i]nserir [a]pagar [l]istar: ')
    os.system('cls')

    if produtos not in ['i', 'inserir', 'a', 'apagar', 'l', 'listar']:
        print('Opção inválida!, Digite uma opção válida por favor')
        continue
    
    if produtos == 'i' or produtos == 'inserir':
        adicionar_carrinho = input('Digite o que deseja inserir: ')
        carrinho.append(adicionar_carrinho)
        print('Produto adicionado com sucesso!')
        continue
    '''if produtos == 'a' or produtos == 'apagar':
        remover_carrinho = input('Digite o que deseja remover: ')
        if remover_carrinho in carrinho:
            carrinho.remove(remover_carrinho)
            print('Produto removido com sucesso!')
        else:
            print('Produto incorreto, por favor escreva novamente o que deseja remover')
        continue'''

    try:
        if produtos == 'a' or produtos == 'apagar':
            remover_carrinho = input('Digite o indice para apagar: ')
            indice = int(remover_carrinho)
            del carrinho[indice]
    except (ValueError, IndexError):
        print('Índice inválido!')

    if produtos == 'l' or produtos == 'listar':
        print('Os seguintes produtos estão no carrinho:')
        for item, value in enumerate(carrinho):
            print(item, value)











'''EXERCÍCIO 11:'''
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

ISSO E UM EXEMPLO DE CALCULAR OS DOIS ULTIMOS DIGITOS DO CPF PRA VE SE ELE É VALIDO OU NÃO

"""


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""


'''RESPOSTA'''


cpf = input('Digite seu CPF: ')
cpf = cpf.replace(".", "").replace("-", "")
n = 10
n_2 = 11
soma = 0
soma_2 = 0

if not cpf.isdigit() or len(cpf) != 11 or cpf == cpf[0] * len(cpf):
    print('CPF inválido')
else:
    try:
        for index in range(9):
            soma += int(cpf[index]) * n
            n -= 1
        multi_final = soma * 10
        resto = multi_final % 11

        if resto > 9:
            resto = 0

        for index in range(10):
            soma_2 += int(cpf[index]) * n_2
            n_2 -= 1

        multi_final_2 = soma_2 * 10
        resto_2 = multi_final_2 % 11

        if resto_2 > 9:
            resto_2 = 0

        if resto == int(cpf[9]) and resto_2 == int(cpf[10]):
            print('CPF válido')
        else:
            print('CPF inválido')
    except ValueError:
        print('CPF inválido')






'''EXERCÍCIO 12:'''
"""
CRIADOR DE CPF/GERANDO CPF
VAMOS GERAR NUMEROS ALEATÓRIOS NO PYTHON
IMPORT RE => USADO PRA ESCOLHER APENAS NUMEROS E APAGAR QUAISQUER OUTRAS COISAS
IMPORT SYS => USADO PRA QUEBRAR O CODIGO CASO CAIA NELE
IMPORT RANDOM => USADO PRA GERAR NUMEROS ALEATÓRIOS
"""

'''RESPOSTA'''

import random

for _ in range(100):

    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10

    resultado_digito_1 = 0
    for digito in nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

    print(f'CPF gerado: {cpf_gerado_pelo_calculo}')











# EXERCÍCIO 12:
    # Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# RESPOSTA:

def multi_args(*args):
    total = 1
    for multi in args:
        total *= multi
    return total


resultado = multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(resultado)




# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# RESPOSTA

try:
    numero_digitado = input('Digite seu número: ')
    numero = int(numero_digitado)
    def par(v):
        print(f'O número {numero} é par')
        return v % 2 == 0

    def impar(v):
        print(f'O número {numero} é ímpar')
        return v % 2 != 0

    if numero % 2 == 0:
        par(numero)
    else:
        impar(numero)
except ValueError:
    print('Digite um número, por favor')


'''
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)
print(dois_e_par)
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

print(par_impar is outro_par_impar)


DARIA PRA FAZER COM ESSA LOGICA AI EM CIMA TMB MAS AI ERA PRA USAR SOMENTE A FUNÇÃO PRA VER SE E PAR OU IMPAR E APENAS A FUNÇÃO
SEM PRECISAR DE CODIGOS EXTERNOS
'''








# EXERCÍCIO 13:
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
# def duplicar(numero):
#     return numero * 2


# def triplicar(numero):
#     return numero * 3


# def quadruplicar(numero):
#     return numero * 4

#RESULTADO:

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))





'''
MULTIPLICAÇÃO ENTRE 2 VALORES
RESULTADO:
'''



def converter_numero(numero):
    numero = float(numero)

    if numero.is_integer():
        return int(numero)
    return numero


number_to_multiply = converter_numero(input('Digite seu número: '))
number_for_multiply = converter_numero(input('Digite o número para multiplicar: '))


def multiplicador(number, number_2):
    return number * number_2


resultado = multiplicador(number_to_multiply, number_for_multiply)

print(f'Resultado: {resultado}')










# EXERCÍCIO 14:
# Exercício - sistema de perguntas e respostas
# RESPOSTA:

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
total_perguntas = len(perguntas)
for pergunta in perguntas:
    qnt_opcoes = len(pergunta['Opções'])

def answer_1():
    while True:
        global acertos
        index = 0
        index_options = perguntas[0]['Opções'].index(perguntas[0]['Resposta'])
        print(f'{perguntas[0]['Pergunta']}\n')
        for valores in perguntas[0]['Opções']:
            print (f'{index}) {valores}')
            index += 1
        Question = input('Escolha uma opção: ')
        try:
            if int(Question) >= 0 and int(Question) < qnt_opcoes:
                if Question.isdigit() and int(Question) == index_options:
                    print('Acertou 👍\n')
                    acertos +=1
                    break
                else:
                    print('Errou ❌')
                    break
            else:
                print('Digite uma opção válida')
                continue
        except ValueError:
            print('Digite um número\n')


def answer_2():
    while True:
        global acertos
        index = 0
        index_options = perguntas[1]['Opções'].index(perguntas[1]['Resposta'])
        print(f'{perguntas[1]['Pergunta']}\n')
        for valores in perguntas[1]['Opções']:
            print (f'{index}) {valores}')
            index += 1
        Question = input('Escolha uma opção: ')
        try:
            if int(Question) >= 0 and int(Question) < qnt_opcoes:
                if Question.isdigit() and int(Question) == index_options:
                    print('Acertou 👍\n')
                    acertos += 1
                    break
                else:
                    print('Errou ❌')
                    break
            else:
                print('Digite uma opção válida')
                continue
        except ValueError:
            print('Digite um número\n')

def answer_3():
    while True:
        global acertos
        index = 0
        index_options = perguntas[2]['Opções'].index(perguntas[2]['Resposta'])
        print(f'{perguntas[2]['Pergunta']}\n')
        for valores in perguntas[2]['Opções']:
            print (f'{index}) {valores}')
            index += 1
        Question = input('Escolha uma opção: ')
        try:
            if int(Question) >= 0 and int(Question) < qnt_opcoes:
                if Question.isdigit() and int(Question) == index_options:
                    print('Acertou 👍\n')
                    acertos += 1
                    break
                else:
                    print('Errou ❌')
                    break
            else:
                print('Digite uma opção válida')
                continue
        except ValueError:
            print('Digite um número\n')

print('Responda as perguntas abaixo\n')
start = input('Deseja começar? Digite [s]im ou [n]ão: ').lower()
if start in ('s', 'sim'):
    answer_1()
    answer_2()
    answer_3()
    print(f'Você acertou {acertos} de {total_perguntas} perguntas')
elif start in ('n', 'não', 'nao'):
    print('Tente mais tarde')
else:
    print('Responda corretamente')





# OUTRA RESPOSTA:
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')




"""
EXERCÍCIO 15:
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1


    RESPOSTA:
"""

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
def duplicate_number(lista):
    number = set()

    for numero in lista:
        if numero in number:
            return numero
        number.add(numero)

    return -1

for lista in lista_de_listas_de_inteiros:
    resultado = duplicate_number(lista)
    print(f'Lista: {lista}')
    print(f'Primeiro duplicado: {resultado}')
    print()







# EXERCÍCIO 16:
# RESPOSTA
# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


produtos_2 = [
    {'nome': 'Produto 7', 'preco': 35.90},
    {'nome': 'Produto 8', 'preco': 47.25},
    {'nome': 'Produto 9', 'preco': 18.75},
    {'nome': 'Produto 6', 'preco': 129.50},
    {'nome': 'Produto 0', 'preco': 83.40},
]


produtos_3 = [
    {'nome': 'Produto 12', 'preco': 56.80},
    {'nome': 'Produto 13', 'preco': 91.35},
    {'nome': 'Produto 14', 'preco': 27.60},
    {'nome': 'Produto 15', 'preco': 145.90},
    {'nome': 'Produto 16', 'preco': 72.45},
]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)



# print(*produtos, sep='\n')

produtos.extend(produtos_2)
produtos.extend(produtos_3)



def aumento_de_preco():
    nova_lista = copy.deepcopy(produtos)
    for produto in nova_lista:
        produto['preco'] = round(produto['preco'] * 1.10, 2)
    return nova_lista



def produtos_ordernados_por_nome():
        nova_lista = copy.deepcopy(produtos)
        nova_lista.sort(key=lambda p: int(p['nome'].split()[-1]))
        return nova_lista


def produtos_ordenados_pelo_preco():
    nova_lista = copy.deepcopy(produtos)
    nova_lista.sort(key=lambda p: p['preco'])
    return nova_lista



print('LISTA NORMAL DOS PRODUTOS:')
print('')
print(*produtos, sep='\n')

print('')
print('')

aumento_de_preco()

print('')
print('')

print('LISTA DOS PRODUTOS ORGANIZADA PELO NOME COM 10% DE VALOR A MAIS:')
print('')
print(*produtos_ordernados_por_nome(), sep='\n')

print('')
print('')

print('LISTA DOS PRODUTOS ORGANIZADA PELO PREÇO COM 10% DE VALOR A MAIS:')
print('')
print(*produtos_ordenados_pelo_preco(), sep='\n')





# SEGUNDA FORMA DE FAZER

import copy


# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# FINAL

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')












# EXERCÍCIO 17:
# Exercício - Adiando execução de funções
# RESPOSTA:

def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    def funcao_interna(*args_internos):
        return funcao(*args, *args_internos)
    return funcao_interna


soma_da_funcao = criar_funcao(soma, 10)
multi_da_funcao = criar_funcao(multiplica, 50)


print(soma_da_funcao(10))
print(multi_da_funcao(20))