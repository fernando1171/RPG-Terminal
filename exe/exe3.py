#Atividades

loja_frutas ={
    'abacaxi':{
        'valor': 4.00,
    },
    'maca':{
        'valor': 5.00,
    },
    'banana':{
        'valor': 2.00,
    },
}

for k,v in loja_frutas.items():
  loja_comidas.get(k)['valor']*1.2
print(loja_comidas)

loja_frutas.update({'limao': 4.00})
print(loja_comidas,'#Limão adicionada')

for chave, valor in loja_frutas.items():
  print(f"key:{chave}: value:'{valor}")

loja_frutas.pop('maca')
print(loja_comidas, '#Maça removida')