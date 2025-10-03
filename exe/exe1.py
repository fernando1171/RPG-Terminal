loja_fruta = {
    'maca': 2.40,
    'banana': 3.60,\
    'uva': 7.60,
}

#função get: método usado para acessar o valor em um dicionário
preco_uva = loja_fruta.get('uva',{})
print('Uva:', preco_uva)

#função update: método usado para atualizar os valores do dicionário
loja_fruta.update({'uva': 8.90, 'tomate': 10})
print(loja_fruta, '#tomate adicionado')

#função pop: método para remover uma chave, específica de um dicionáiro e retornar, o valor associdado a ela.
loja_fruta.pop('tomate')
print(loja_fruta, '#tomate removido')

#função items: método de leitura de um dicionário, que separa a key e value do mesmo.
for chave, valor in loja_fruta.items():
  print(f'key:{chave}: value:{valor}')