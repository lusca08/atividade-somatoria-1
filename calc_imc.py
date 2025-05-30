
nome = input('Digite seu nome: ')
print(f'Ok {nome} agora diga sua altura e peso')
altura = float(input('digite sua altura: '))
peso = float(input('digite seu peso: '))
imc = peso / (altura ** 2)

resultado = round(imc, 2)

print(f'{nome} seu imc é {resultado}')
print('classificação:')
if imc <= 18.5:
    print('abaixo do peso')
    print('')
elif imc < 25: 
    print('peso normal')
    print('')
elif imc < 25: 
    print('sobrepeso')
elif imc < 30: 
    print('obesidade grau 1')
elif imc < 35: 
    print('obesidade grau 2')
else: 
    print('obesidade grau 3(mórbida)')

