loja_transportes = {
    'transporte': 'carroça',
    'cor': 'marrom',
    'valor': 15000,
}

#função get: método usado para acessar o valor em um dicionário
preco_carroça = loja_transportes.get('valor',15000)
print('carroça:', preco_carroça)

#função update: método usado para atualizar os valores do dicionário
loja_transportes.update({'carroça': preco_carroça + preco_carroça * 0.15})
print(loja_transportes, '#15% a mais no valor da carroça')

#função items: método de leitura de um dicionário, que separa a key e value do mesmo.
for chave, valor in loja_transportes.items():
  print(f'key:{chave}: value:{valor}')