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